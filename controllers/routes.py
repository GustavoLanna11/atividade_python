from flask import render_template

def init_app(app):
    @app.route("/")
    def index():
        universo = "Marvel"
        heroi = "iron man"
        return render_template("index.html", **locals())