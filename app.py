from flask import Flask, render_template, request
from chargers import ChargerForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'debug'

@app.route('/')
def index():
    active = True
    return render_template('index.html')

@app.route('/index')
def index2():
    return render_template('index.html')

@app.route('/chargers', methods=['POST', 'GET'])
def chargers():
    form = ChargerForm()
    return render_template('chargers.html', form=form)


@app.route('/evbasics')
def evbasics():
    return render_template('evbasics.html')

@app.route('/cars')
def cars():
    return render_template('cars.html')

@app.route('/about')
def about():
    return render_template('about.html')