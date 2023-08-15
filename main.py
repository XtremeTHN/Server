from flask import Flask, render_template, request
import json
import bcrypt

app = Flask("serv")

PASSWORD="$2b$12$xXTfDqK.cS6xkXObO7ypluljUd8u//FO6dCG2bGmSWg2OFqMgp4ta"

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
        data = request.get_json()
        if "name" not in data or "password" not in data:
            return "Bad Request", 400
        
        bobj = bcrypt.gensalt()
        hashed = bcrypt.hashpw(data["password"].encode(), bobj)
        data["password"] = hashed.decode()

        with open("resources/users.json", "r+") as f:
            users = json.load(f)
            users["servers"].append(data)
            f.seek(0)
            json.dump(users, f, indent=4)
            f.truncate()
    return "OK", 200

@app.route("/get_users", methods=["GET"])
def get_users():
    passw = request.get_json()
    if bcrypt.checkpw(passw["password"].encode() if "password" in passw else "0".encode(), PASSWORD.encode()):
        return "Access Denied", 403
    with open("resources/users.json", "r") as f:
        return f.read(), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)