from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from game_logic import Game
from database import db
import os

app = Flask(__name__)
game = Game()
app.secret_key = os.urandom(24)

# Load main page of game
@app.route("/")
def index():
    # Login before enetering main page
    if "username" not in session:
        return redirect(url_for("login"))
    
    return render_template("index.html")

# Send data from the game to the browser as JSON
@app.route("/game_state")
def game_state():
    return jsonify(game.get_board_state())

# Receive country details from the browser to start the battle 
@app.route("/attack", methods=["POST"])
def attack():
    data = request.get_json()

    attacker = game.find_country(data["attacker"])
    defender = game.find_country(data["defender"])

    battle_outcome = game.battle(attacker, defender)

    return jsonify({
        "battle_outcome": battle_outcome,
        "game_state": game.get_board_state()
    })

# Run npc turn abd return game state
@app.route("/npc_turn", methods=["POST"])
def npc_turn():
    npc_outcome = game.npc_turn()

    return jsonify({
        "npc_outcome": npc_outcome,
        "game_state": game.get_board_state()
    })

# Reset game to its original state
@app.route("/reset", methods=["POST"])
def reset():
    global game
    game = Game()

    return jsonify({
        "game_state": game.get_board_state()
    })

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if db.register_user(username, password):
            return redirect(url_for("login"))
        else:
            return "Username already being used. Please try a different username.", 400

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if db.verify_user(username, password):
            session["username"] = username
            return redirect(url_for("index"))
        else:
            return "Invalid login details.", 401

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)  # Start 