from flask import Flask

app = Flask(__name__)
import requests
import os

import logging

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/hub/<scene_id>')
def send_to_hub(scene_id):
    logging.debug("activating scene {}".format(scene_id))
    requests.get('http://192.168.0.106/api/scenes?sceneid={}'.format(scene_id))
    return "succeeded"

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run("0.0.0.0")
