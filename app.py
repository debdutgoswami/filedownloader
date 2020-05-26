import os
from flask import Flask, render_template, request, make_response, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        # caching the content for 10 min
        template = render_template('home.html')
        response = make_response(template)
        response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'

        return response
    else:
        dept, email, year = dict(request.form)['dept'], dict(request.form)['email'], dict(request.form)['year']
        try:
            return send_from_directory("certificate",f"{year} {dept}",f"{email}.pdf")
        except FileNotFoundError:
            return "file not found"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)