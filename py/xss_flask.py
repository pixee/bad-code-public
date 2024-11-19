import os

from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    session,
    render_template_string
)
from flask.ext.session import Session
from .process import process_input

app = Flask(__name__)


execfile('flag.py')
execfile('key.py')

FLAG = flag
app.secret_key = key


@app.route("/golem", methods=["GET", "POST"])
def golem():
    if request.method != "POST":
        return redirect(url_for("index"))

    golem = request.form.get("golem") or None

    process_input(golem)
    template = None

    if session['golem'] is not None:
        template = '''{% % extends "layout.html" % %}
        {% % block body % %}
        <h1 > Golem Name < /h1 >
        <div class ="row >
        <div class = "col-md-6 col-md-offset-3 center" >
        Hello: % s, why you don't look at our <a href=' / article?name = article'> article < /a >?
        < / div >
        < / div >
        {% % endblock % %}
        ''' % session['golem']

        print

        session['golem'] = None

    return render_template_string(template)
