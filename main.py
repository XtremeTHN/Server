import flask

app = flask.Flask("serv")

@app.route("/")
def run():
    return flask.render_template_string("""
<!doctype html>
<html>
    <head>
        <title>Warning</title>
    </head>
    <body>
        <p>This is a api, not a website, please do not visit with your browser</p>
    </body>
</html>
""")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)