from flask import Flask, render_template
#syncing code base
app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')
if __name__ == "__main__":
    app.run(debug=True)
