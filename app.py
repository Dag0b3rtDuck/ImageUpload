from flask import Flask, request, render_template, redirect, Blueprint
from werkzeug.utils import secure_filename
import string
import os
import random
from ImageUpload import settings

app = Flask(__name__)

folder = ""

extensions = ["png", "jpg", "mp4"]


@app.route("/")
def index():
    return render_template("index.html")


def random_string():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if allowed(file.filename):
            filename = random_string() + secure_filename(file.filename)
            file.save(os.path.join(folder, filename))
            return redirect(request.url)
    return render_template("upload.html")


@app.route("/api")
def api():
    return render_template("api.html")


@app.route("/<string:picture_name>")
def picture(picture_name):
    return render_template("picture.html", picture_name=picture_name)




def main():
    app.run(debug=settings.FLASK_DEBUG, threaded=settings.FLASK_THREADED)

if __name__ == "__main__":
    main()