from flask import Flask, render_template\
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# app を初期化
app = Flask(__name__)
# SQLAlchemy の設定
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# DB とつなぐ
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Feed モデル (=最初のテーブル)
class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)


@app.route("/")
def index():
    return "index page"


@app.route("/hello/<name>",methods=['Get'], endpoint='hello-endpoint')
def hello(name):
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
