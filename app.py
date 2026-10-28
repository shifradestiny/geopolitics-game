from flask import Flask, jsonify, render_template, request
from game_logic import Game

app = Flask(__name__)
game = Game()

# Send data from the game to the browser as JSON
@app.route("/game_state")
def game_state():
    return jsonify(game.get_board_state())

if __name__ == "__main__":
    app.run(debug=True)  # Start 