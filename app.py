from flask import Flask, render_template, request
from services.essay_service import *

port = int(os.environ.get('PORT', 5000))
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    essay = ""
    if request.method == 'POST':
        request_copy = request.form.copy()
        essay_prompt = request_copy['essay-prompt']
        paragraph_count = request_copy['paragraph-count']
        essay = write_essay(essay_prompt, paragraph_number=paragraph_count)
    return render_template('index.html', essay=essay)

if __name__ == '__main__':
    app.run(port=port)