import flask

app = flask.Flask("serv")

@app.route("/")
def run():
    return flask.render_template_string("""
<!doctype html>
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <p>Hi there!</p>
    </body>
</html>
""")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)