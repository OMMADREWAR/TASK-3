from flask import Flask, render_template
import random

app = Flask(__name__)

def roll_dice():
    return random.randint(1, 6)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice')
def roll_dice_route():
    result = roll_dice()
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
