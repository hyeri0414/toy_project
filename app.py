from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/example')
def example():
    x = 37.39563962083837
    y = 127.92368802692928
    return render_template('example.html', x_data=x, y_data=y)

@app.route('/marker_text')
def marker_text():
    return render_template('marker_text.html')

@app.route('/geolocation_marker')
def geolocation_marker():
    return render_template('geolocation_marker.html')

@app.route('/olive_young')
def olive_young():
    return render_template('olive_young.html')

if __name__ == '__main__':
    app.run()