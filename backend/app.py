from dateparser import parse as parse_date
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def get_date_from_text():
    text = request.args.get('text')
    if not text:
        return 'You need a text parameter', 400

    timezone = request.args.get('timezone', 'US/Eastern')
    date = parse_date(text, settings={'TIMEZONE': timezone})
    if not date:
        return 'Invalid date', 400
    return str(date)


@app.route('/ping')
def ping():
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
