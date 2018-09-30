from flask import Flask, render_template, url_for
from pygal.style import BlueStyle
import pickle
import pygal
import os

smrh = Flask(__name__)

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

filename1 = PATH + '/static/data/times.p'
filename2 = PATH + '/static/data/readings.p'
filename3 = PATH + '/static/data/digits.p'

@smrh.route('/')
def index():
    with open(filename1, 'rb') as temp_file:
        times = pickle.load(temp_file)

    with open(filename2, 'rb') as temp_file:
        readings = pickle.load(temp_file)

    with open(filename3, 'rb') as temp_file:
        digits = pickle.load(temp_file)

    delta_reading = readings[-1] - readings[0]
    last_digit = digits[-1]

    return render_template('index.html', FIRST_TIME=times[0], LAST_TIME=times[-1], FIRST_READING=readings[0],LAST_READING=readings[-1], DIF_READING=delta_reading, LAST_DIGIT=last_digit)

@smrh.route('/graph')
def graph():
    with open(filename1, 'rb') as temp_file:
        times = pickle.load(temp_file)

    with open(filename2, 'rb') as temp_file:
        readings = pickle.load(temp_file)

    graph = pygal.Bar(x_title='Horário Registrado', y_title='Consumo Total (litros)', style=BlueStyle, x_label_rotation=10)
    graph.title = 'SMRH - Consumo Total de Água'

    # Show last 10 readings/times
    graph.x_labels = times[-10:]
    graph.add('Consumo', readings[-10:])

    graph_data = graph.render_data_uri()
    return render_template('graph.html', graph_data=graph_data)

if __name__ == '__main__':
    smrh.run(debug=True, host='0.0.0.0')
