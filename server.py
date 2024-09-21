from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weight_tracker')
def weight_tracker():
    return render_template('weight_tracking.html')

if __name__ == '__main__':
    port = 5000  # Change this variable to use a different port
    app.run(debug=True, port=port)