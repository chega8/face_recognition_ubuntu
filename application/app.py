import flask
import json
#import sys
#sys.path.append('/home/chega/Рабочий стол/face_recognition/indor-face_recognition/application')
from controllers.FrameController import FrameController

import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# disables JSON pretty-printing in flask.jsonify
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

frame_controller = FrameController()

app = flask.Flask(__name__)


def to_json(data):
    return json.dumps(data) + "\n"


def resp(code, data):
    return flask.Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )


def frame_validate():
    errors = []
    js = flask.request.get_json()
    if js is None:
        errors.append(
            "No JSON sent. Did you forget to set Content-Type header" +
            " to application/json?")
        return (None, errors)

    for field_name in ['frame']:
        if type(js.get(field_name)) is not list:
            errors.append(
                "Field '{}' is missing or is not a list".format(field_name))

    return (js, errors)


def affected_num_to_code(cnt):
    code = 200
    if cnt == 0:
        code = 404
    return code


@app.route('/')
def root():
    return flask.redirect('/api/1.0/frames')


# e.g. failed to parse json
@app.errorhandler(400)
def page_not_found(e):
    return resp(400, {})


@app.errorhandler(404)
def page_not_found(e):
    return resp(404, {})


@app.errorhandler(405)
def page_not_found(e):
    return resp(405, {})


@app.route('/api/1.0/frames', methods=['POST'])
def post_frame():
    (js, errors) = frame_validate()
    if errors:  # list is not empty
        return resp(400, {"errors": errors})

    names = frame_controller.post_frame(js)
    return resp(200, {"known_names": names})


if __name__ == '__main__':
    app.debug = False  # enables auto reload during development
    app.run()
