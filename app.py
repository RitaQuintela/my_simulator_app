from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Your POST route logic here
        return "Welcome to My Simulator App! (POST)"
    else:
        # Your main route logic here
        return "Welcome to My Simulator App! (GET)"

@app.route('/get_tuition', methods=['POST'])
def get_tuition():
    # Handle the /get_tuition route
    # You can return relevant data or render an HTML template
    return "Tuition information goes here"

if __name__ == '__main__':
    app.run(debug=True)
