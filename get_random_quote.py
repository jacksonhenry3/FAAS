#!/usr/bin/env python3
import random
from flask import Flask, jsonify

app = Flask(__name__)


with open("fortunes") as fortunes_file:
    fortunes_list = fortunes_file.read().split('%')

num_fortunes = len(fortunes_list)


def get_fortune():
  fortune_index = random.randint(0, num_fortunes)
  return(fortunes_list[fortune_index])


@app.route("/")
def fortune():
    return jsonify(get_fortune())

app.run(host='0.0.0.0', port=8080)