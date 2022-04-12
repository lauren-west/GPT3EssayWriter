from flask import Flask, render_template, request
from services.essay_service import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    essay = ""
    if request.method == 'POST':
        request_copy = request.form.copy()
        essay_prompt = request_copy['essay-prompt']
        essay = write_essay(essay_prompt)
    return render_template('index.html', essay=essay)

app.run(host='0.0.0.0', port=81)