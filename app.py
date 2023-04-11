from flask import Flask, request, render_template ## Import flask.
from flask_debugtoolbar import DebugToolbarExtension ##Import Debug toolbar from flask.
from stories import story ## Import story class from stories.py

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    
    prompts = story.prompts 
    return render_template("home.html", prompts=prompts)

@app.route('/stories')
def show_inputs():
    
    text = story.generate(request.args)
    return render_template("story.html", text=text)
    


