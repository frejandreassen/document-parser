import streamlit as st
from google.api_core.client_options import ClientOptions
from google.cloud import documentai_v1 as documentai
from google.oauth2 import service_account
from PIL import Image
from io import BytesIO
import pandas as pd

# Your Google Cloud settings
PROJECT_ID = "andreassens"
LOCATION = "eu"
PROCESSOR_ID = "ddc671fa9fcf4c58"

# Create a credentials object using the service account info from the secrets
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

def process_document(file):
    docai_client = documentai.DocumentProcessorServiceClient(
        credentials=credentials,
        client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
    )

    RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)
    raw_document = documentai.RawDocument(content=file.read(), mime_type=file.type)

    request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)
    result = docai_client.process_document(request=request)

    document_object = result.document
    return document_object

st.set_page_config(page_title="Document Parser")

st.write("## Parse Documents to Text")
st.write("Upload a document and let Google Document AI extract the text for you. Perfect for Swedish invoices")

uploaded_files = st.file_uploader("Upload a document", type=["pdf", "jpg", "jpeg", "png", "tiff"], accept_multiple_files=True)

all_text = ""
all_entities = []

for uploaded_file in uploaded_files:
    if uploaded_file is not None:
        st.write(f"Processing the document: {uploaded_file.name} ...")
        document = process_document(uploaded_file)
        st.write("Document processing complete.")
        st.write(f"### Extracted Text from {uploaded_file.name}")
        st.write(document.text)
        
        all_text += "\n" + document.text
        
        types = []
        raw_values = []
        normalized_values = []
        confidence = []
        
        for entity in document.entities:
            types.append(entity.type_)
            raw_values.append(entity.mention_text)
            normalized_values.append(entity.normalized_value.text)
            confidence.append(f"{entity.confidence:.0%}")
            
            for prop in entity.properties:
                types.append(prop.type_)
                raw_values.append(prop.mention_text)
                normalized_values.append(prop.normalized_value.text)
                confidence.append(f"{prop.confidence:.0%}")
        
        all_entities.append({
            "Type": types,
            "Raw Value": raw_values,
            "Normalized Value": normalized_values,
            "Confidence": confidence,
        })

if all_text:
    st.write("### Aggregated Extracted Text")
    st.markdown(f"```{all_text}```")

# if all_entities:
#     st.write("### Aggregated Entities")
#     for i, entities in enumerate(all_entities):
#         df = pd.DataFrame(entities)
#         st.write(f"Entities from File {i + 1}")
#         st.write(df)
else:
    st.write("Please upload a document.")
