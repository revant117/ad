from flask import Flask, render_template,request,url_for
import subprocess
from flask import send_file


import os

app = Flask(__name__,static_folder='static', static_url_path='')


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/file')
def file():
  

  download_filename = "test.txt"

  return(send_file(filename_or_fp = download_filename,mimetype="text",as_attachment=True))



port = int(os.environ.get('PORT', 3000))

if __name__ == '__main__':
     app.run(debug=True,port=port)