from flask import Flask, request, render_template, redirect, send_file, url_for, abort, jsonify
from werkzeug.utils import secure_filename
import string
import os
import random
from settings import settings
import json
from settings import secrets
from werkzeug import exceptions

app = Flask(__name__)

folder = "pictures"

extensions = ["png", "jpg", "mp4"]


def upload(request):
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if allowed(file.filename):
            filename = random_string() + secure_filename(file.filename)
            file.save(os.path.join(folder, filename))
            return redirect(url_for("picture", picture_name=filename))



def random_string():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def normal_upload():
    print(request.files)
    upload(request)
    return render_template("upload.html")


@app.route("/api")
def api():
    return render_template("api.html")


@app.route("/api/upload", methods=['POST'])
def api_upload():
    print(json.dumps(request.form))

    #postedjson = json.loads(request.data.decode('utf-8'))
    #print(postedjson)
    #if postedjson['api_key'] == secrets.API_KEY:
    #    print("1")
    #    upload(request)
    #else:
    #    abort(418)
    return "succes"


@app.route("/<path:picture_name>")
def picture(picture_name):
    return send_file("pictures\\"+picture_name)


#@app.errorhandler(exceptions.ImATeapot)


def main():
    app.run(port=1337, debug=settings.FLASK_DEBUG, threaded=settings.FLASK_THREADED)


if __name__ == "__main__":
    main()
