from flask import Flask, render_template, request
import json
import bcrypt
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Nivel de registro mínimo
    filename='app.log',  # Nombre del archivo de logs
    filemode='w',  # Modo de apertura del archivo ('w' para sobrescribir, 'a' para añadir)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato de registro
)

logger = logging.getLogger("WEB")

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

@app.route("/get_servers", methods=["GET"])
def get_servers():
    logger.info("Getting servers...")
    passw = request.get_json()
    with open("resources/users.json", "r") as f:
        json_file = json.load(f)
        servers = {"servers": []}
        logger.info("Removing passwords from the json file...")
        for x in json_file["servers"]:
            del x["password"]
            servers["servers"].append(x)
        logger.info("Successfuly removed passwords from the json file.")
        return servers, 200
# if x["name"] == passw["name"] and x["password"] == passw["password"]:
#     return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)