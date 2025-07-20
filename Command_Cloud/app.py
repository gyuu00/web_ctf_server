import os
import subprocess
from flask import Flask, request, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping')
def ping():
    host = request.args.get("host", "")
    if any(x in host for x in [';', '|', '&']):
        return "Invalid characters detected."

    try:
        result = subprocess.check_output(f"ping -c 1 {host}", shell=True, stderr=subprocess.STDOUT)
        output = result.decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()

    return render_template('result.html', output=output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
