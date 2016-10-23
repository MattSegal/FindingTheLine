from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def homepage():
    return render_template('./landing.html')

@app.route('/crew')
def crew():
    return render_template('./crew.html')

@app.route('/gallery')
def gallery():
    return render_template('./gallery.html')

@app.route('/partners')
def partners():
    return render_template('./partners.html')

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
