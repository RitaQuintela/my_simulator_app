from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Simulated tuition data (replace with your actual data)
tuition_data = {
    'Computer Science': 10000,
    'Business Administration': 8000,
    # Add more program-tuition pairs as needed
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_tuition', methods=['POST'])
def get_tuition():
    program_name = request.form.get('programName')
    tuition = tuition_data.get(program_name, 'Program not found')
    return jsonify({'tuition': tuition})

if __name__ == '__main__':
    app.run(debug=True)
