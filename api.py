from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import json 
from pdfminer.high_level import extract_text
app = Flask(__name__)
from PyPDF2 import PdfFileReader, PdfFileWriter

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'           #upload folder
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'       #download folder

ALLOWED_EXTENSIONS = {'pdf'}
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

#app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024       #limit upload to 8mb
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
       if 'file' not in request.files:
           print('No file attached in request')
           return redirect(request.url)
       file = request.files['file']
       if file.filename == '':
           print('No file selected')
           return redirect(request.url)
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
           return redirect(url_for('uploaded_file', filename=filename))
   return render_template('index.html')


def process_file(path, filename):
    extract_and_json(path, filename)


def extract_and_json(path, filename):
    output = PdfFileWriter()
    text_list = []
    text = extract_text(pdf)
    text.replace("\n","")
    text_list.append(text)
    dict = {'text':text_list}
    json_object = json.dumps(dictionary, indent = 4)
    output.addPage(json_object) 
    output_stream = open(app.config['DOWNLOAD_FOLDER'] + filename, 'wb')
    output.write(output_stream) 


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)    

if __name__ == '__main__':
  app.run(host='0.0.0.0')