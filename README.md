# Document Parser with Google Document AI and Streamlit

This project demonstrates how to build a simple web application using Streamlit and Google Document AI to parse and extract information from documents. The app allows users to upload a document, process it using Google Document AI, and display the extracted text, tables, and other relevant information.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [License](#license)

## Features

- Upload and process documents in various formats, such as PDF, DOCX, and TIFF.
- Extract text, tables, and other information from the document using Google Document AI.
- Display the extracted information in a user-friendly web interface built with Streamlit.

## Prerequisites

- Python 3.6 or higher
- A Google Cloud Platform account with the Document AI API enabled
- A Google Cloud service account with access to the Document AI API

## Installation

1. Clone this repository:

```bash
git clone https://github.com/frejandreassen/document-parser.git
cd document-parser
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- **Windows**:

```bash
venv\Scripts\activate
```

- **Linux/MacOS**:

```bash
source venv/bin/activate
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Set up the environment variables:

- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your Google Cloud service account JSON key file.

- **Windows**:

```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\keyfile.json
```

- **Linux/MacOS**:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=path/to/your/keyfile.json
```

6. Update the `document_parse.py` file with your Google Cloud project information:

Replace the following placeholders with your project's information:

- `YOUR_PROJECT_ID`
- `YOUR_PROJECT_LOCATION`
- `YOUR_PROCESSOR_ID`

## Usage

1. Run the Streamlit app:

```bash
streamlit run document_parse.py
```

2. Open a web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Upload a document using the file uploader in the app.

4. View the extracted information from the document.

## Customization

You can customize the app to suit your needs by modifying the `document_parse.py` file. For example, you can add more features to display extracted tables, form fields, entities, or other information available from the Document AI API.

## License

This project is licensed under the [MIT License](LICENSE).