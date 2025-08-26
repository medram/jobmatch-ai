# Document Evaluator

A Streamlit application for evaluating documents. This application supports PDF and DOCX file formats.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd projet3
```

2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

This will install the following dependencies:

- streamlit
- pandas
- PyPDF2
- python-docx

## Running the Application

To run the application, use the following command from the project root directory:

```bash
streamlit run app/app.py --server.runOnSave true
```

The `--server.runOnSave true` flag enables automatic reloading of the application when you make changes to the source code.

Once started, the application will be available in your web browser at `http://localhost:8501` by default.
