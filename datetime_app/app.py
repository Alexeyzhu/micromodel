import datetime

from flask import Flask, jsonify

server = Flask(__name__)

counter = 0


@server.route('/time', methods=['GET'])
def time():
    global counter
    counter += 1
    return jsonify(dict(id=counter,
                        time=str(datetime.datetime.now().time())))


@server.route('/date', methods=['GET'])
def date():
    global counter
    counter += 1
    return jsonify(dict(id=counter,
                        date=str(datetime.datetime.now().date())))
