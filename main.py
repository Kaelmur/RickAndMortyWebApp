import requests
import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/character", methods=["GET", "POST"])
def character():
    response = requests.get(url=f"https://rickandmortyapi.com/api/character/{random.randint(0, 826)}")
    response.raise_for_status()
    data = response.json()
    episode_url = data["episode"]
    episode_url2 = ', '.join(episode_url)
    response2 = requests.get(url=episode_url2)
    try:
        episode = response2.json()['episode']
    except KeyError:
        episode = None
    return render_template("character.html", data=data, episode=episode)


if __name__ == '__main__':
    app.run(debug=True)
