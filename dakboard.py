from flask import Flask, send_file
import random

from os import listdir
from os.path import isfile, join


app = Flask(__name__)


@app.route('/')
def hello():

  mypath = "./images/"

  onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  filename = mypath + random.choice(onlyfiles)
  return send_file(filename, mimetype="image/jpeg")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)