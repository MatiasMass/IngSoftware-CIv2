from flask import Flask, render_template

app = Flask(__name__)

message = "Flask is working!!"
# Define the root route
@app.route('/')
def index():
    return render_template('index.html', message = message)


if __name__ == '__main__':
    app.run()