from flask import Flask, render_template, request
import html
#import bleach #pip install

app = Flask(__name__)


@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    if request.method == 'POST':
        name = request.form["name"]
        return render_template('vulnerable.html', name=name)
    
    return render_template('vulnerable.html', name=None)
"""
<script>
  document.getElementById('output').innerHTML = "😈 You’ve been attacked! <img src='x' onerror='alert(\"Oops!\")'>";
</script>

What it does:
Finds the <div id="output">
Replaces its content with malicious HTML
Adds an image with an onerror XSS (CSS) trigger
"""

@app.route('/safe', methods=['GET', 'POST'])
def safe():
    if request.method == 'POST':
        name = request.form["name"]

        #escaped_name = html.escape(name)
        #return f"Hello World {escaped_name}"

        return render_template('safe.html', name=name)
    return render_template('safe.html', name=None)




if __name__ == '__main__':
    app.run(debug=True) 