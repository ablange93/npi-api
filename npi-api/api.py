import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>NPI Data Web Interface</h1><p>This site is a prototype API that enables users to access NPI data.</p>"

app.run()