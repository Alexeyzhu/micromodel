import random

from flask import Flask, jsonify

server = Flask(__name__)

counter = 0


@server.route('/colors', methods=['GET'])
def theme():
    global counter
    counter += 1
    return jsonify(dict(id=counter,
                        font_color=get_rand_color(),
                        background_color=get_rand_color()))


def get_rand_color():
    return '#%06X' % random.randint(0, 256 ** 3 - 1)
