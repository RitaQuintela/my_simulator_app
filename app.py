from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Your main route logic here
    return "Welcome to My Simulator App!"

@app.route('/get_tuition')
def get_tuition():
    # Handle the /get_tuition route
    # You can return relevant data or render an HTML template
    return "Tuition information goes here"

if __name__ == '__main__':
    app.run(debug=True)
