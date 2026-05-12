from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/grifinoria")
def grifinoria():
    url = "https://hp-api.onrender.com/api/characters/house/gryffindor"
    resposta = urllib.request.urlopen(url)
    jsondata = json.loads(resposta.read())
    return render_template("apihp.html", personagens=jsondata)

@app.route("/personagenshp")
def personagenshp():
    url = "https://hp-api.onrender.com/api/characters"
    resposta = urllib.request.urlopen(url)
    jsondata = json.loads(resposta.read())
    return render_template("apipersonagenshp.html", pessoas=jsondata)

if __name__ == "__main__":
    app.run(debug=True)
