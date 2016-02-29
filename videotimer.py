from flask import Flask, redirect
app = Flask(__name__, static_folder="static")
import requests

import logging


@app.route('/hub/<scene_id>')
def send_to_hub(scene_id):
    logging.debug("activating scene {}".format(scene_id))
    requests.get('http://192.168.0.106/api/scenes?sceneid={}'.format(scene_id))
    return "succeeded"


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run("0.0.0.0")
