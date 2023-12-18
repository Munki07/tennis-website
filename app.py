from flask import Flask, render_template

app = Flask(__name__)

players = [
    {
        'name': 'Novak Djokovic',
        'hand': 'Right-handed',
        'titles': '98'
    },
    {
        'name': 'Rafael Nadal',
        'hand': 'Left-handed',
        'titles': '92'
    },
    {
        'name': 'Roger Federer',
        'hand': 'Right-handed',
        'titles': '103'
    },
]


@app.route("/")
def home_screen():
    return render_template("home.html", players=players, website_name='Tennis Talk')

@app.route("/chatroom")
def talk_screen():
    return("Hello")

if __name__ == "__main__":
    app.run()
