from flask import Flask, render_template, request
import openpyxl

app = Flask(__name__)

# Load the workbook and select the active worksheet
workbook = openpyxl.load_workbook('your_file.xlsx')
sheet = workbook.active

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['userInput']
        result = simulate(user_input)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

def simulate(user_input):
    for row in sheet.iter_rows(min_row=2):  # Assuming the first row is the header
        if row[0].value == user_input:
            return row[1].value
    return "No match found."

if __name__ == '__main__':
    app.run(debug=True)
