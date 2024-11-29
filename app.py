from flask import Flask, render_template, jsonify
import random
import time
import threading

app = Flask(__name__)

current_letter = None
countdown_seconds = 120
is_game_running = False
countdown_thread = None

def get_random_letter():
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z']
    letter = random.choice(alph)
    return transform_letter(letter)

def transform_letter(letter):
    transformations = {
        "A": "A,Á",
        "C": "C,CS",
        "D": "D,DZ,DZS",
        "E": "E,É",
        "G": "G,GY",
        "I": "I,Í",
        "J": "J,LY",
        "N": "N,NY",
        "O": "O,Ó,Ö,Ő",
        "S": "S,SZ",
        "T": "T,TY",
        "U": "U,Ú,Ü,Ű",
        "Z": "Z,ZS"
    }
    return transformations.get(letter, letter)

def countdown():
    global is_game_running
    time.sleep(countdown_seconds)
    is_game_running = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game')
def start_game():
    global current_letter, is_game_running, countdown_thread
    current_letter = get_random_letter()
    if not is_game_running:
        is_game_running = True
        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.start()
    return jsonify({'letter': current_letter, 'running': is_game_running})

@app.route('/status')
def status():
    return jsonify({'running': is_game_running})

if __name__ == '__main__':
    app.run(debug=True)
