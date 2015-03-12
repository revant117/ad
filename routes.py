from flask import Flask, render_template,request,url_for
import subprocess
from flask import send_file


import os

app = Flask(__name__,static_folder='static', static_url_path='')


@app.route('/')
def home():
  return render_template('index.html')





@app.route('/shedule')
def file():
	download_filename = "IGNITE 2015 Guidelines final.pdf"
	return(send_file(filename_or_fp = download_filename,mimetype="text",as_attachment=True))

@app.route('/guide')
def file2():
	download_filename = "IGNITE 2015 Registration form.pdf"
	return(send_file(filename_or_fp = download_filename,mimetype="text",as_attachment=True))

@app.route('/register')
def file3():
	download_filename = "IGNITE 2015 REGISTRATION FORM.pdf"
	return(send_file(filename_or_fp = download_filename,mimetype="text",as_attachment=True))
  

  

  








port = int(os.environ.get('PORT', 3000))

if __name__ == '__main__':
     app.run(debug=True,port=port)