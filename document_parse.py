import streamlit as st
from google.api_core.client_options import ClientOptions
from google.cloud import documentai_v1 as documentai
from PIL import Image
from io import BytesIO

# Your Google Cloud settings
PROJECT_ID = "andreassens"
LOCATION = "eu"
PROCESSOR_ID = "ddc671fa9fcf4c58"

def process_document(file):
    docai_client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
    )

    RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)
    raw_document = documentai.RawDocument(content=file.read(), mime_type=file.type)

    request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)
    result = docai_client.process_document(request=request)

    document_object = result.document
    print(document_object.entities)
    return document_object.text

st.set_page_config(layout="wide", page_title="Document Parser")

st.write("## Parse Documents to Text")
st.write("Upload a document and let Google Document AI extract the text for you.")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "jpg", "jpeg", "png", "tiff"])

if uploaded_file is not None:
    st.write("Processing the document...")
    extracted_text = process_document(uploaded_file)
    st.write("Document processing complete.")
    st.write("### Extracted Text")
    st.write(extracted_text)
else:
    st.write("Please upload a document.")
