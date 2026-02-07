from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_time', methods=['GET'])
def get_time():
    return {
        "time_live": time.strftime("%H:%M:%S"),
        "time_info": time.strftime("%D %B %Y")
    }

if __name__ == '__main__':
    app.run(debug=True)