from flask import Flask, render_template, request
import json
import bcrypt

app = Flask("serv")

@app.route("/")
def run():
    return render_template_string("""
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

@app.route("/store", methods=["POST"])
def store():
    if request.method == "POST":
        data = json.loads(request.data.decode())
        if "name" and "password" not in data:
            return 400
        
        bobj = bcrypt.gensalt()
        hashed = bcrypt.hashpw(data["password"].encode(), bobj)
        data["password"] = hashed.decode()

        with open("resources/users.json", "w+") as f:
            users = json.load(f)
            users["servers"].append(data)
    
    return 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)