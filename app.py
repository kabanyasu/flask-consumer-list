from flask import Flask
from flask import render_template
from flask import request

# おまじない
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("input.html")

@app.route("/result",methods = ["POST"])
def file_save():
    # htmlのformで入力したexcelファイルを受け取る
    file = request.files['upload-file']
    file_name = file.filename
    file.save(f"save_csv_folder/{file_name}")
    return render_template("result.html",file_name=file_name)