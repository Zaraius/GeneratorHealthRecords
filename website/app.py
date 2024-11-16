from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import PyPDF2
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract data from PDF
        extracted_data = extract_data_from_pdf(filepath)
        # Convert extracted data to JSON
        json_data = convert_to_json(extracted_data)

        return jsonify(json_data)

    return "Invalid file format", 400

def extract_data_from_pdf(filepath):
    # Placeholder function to extract data from PDF
    # Implement PDF extraction logic here
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def convert_to_json(data):
    # Placeholder function to convert extracted data to JSON
    # Implement conversion logic here
    return {"extracted_text": data}

if __name__ == '__main__':
    app.run(debug=True)