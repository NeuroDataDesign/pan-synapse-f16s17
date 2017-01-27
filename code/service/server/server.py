from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        print "I got it"
        return redirect('http://localhost:5000/analyze')

@app.route('/analyze', methods = ['GET', 'POST'])
def analyze():
    if request.method == 'GET':
        return render_template('brain.html')

if __name__ == '__main__':
    app.run(debug=True)
