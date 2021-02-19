import json
import pandas

from flask import Flask, request, abort

LIMIT = ord('h')


def run(data: dict):

    ascii_characters = data['input']

    if not ascii_characters:
        abort(400)

    s = pandas.Series(ascii_characters)
    if not pandas.api.types.is_string_dtype(s):
        abort(500)

    s = s.apply(convert_ascii_character)

    return json.dumps(
        {'output': s.tolist()}
    )


def convert_ascii_character(x: str):
    """
    Returns the ASCII character code multiplied by 10 when the character is below the LIMIT and 0 otherwise
    """
    return ord(x) * 10 if ord(x) < LIMIT else 0


app = Flask(__name__)


@app.errorhandler(400)
def empty_list(error):
    return "The requested payload cannot be converted", 400


@app.errorhandler(500)
def type_error(error):
    return "The payload does not only contain ascii characters", 500


@app.route('/convert', methods=['POST'])
def convert():
    return run(request.json)


app.run(port=8888)
