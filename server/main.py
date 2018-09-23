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

@smrh.route('/')
def index():
    return render_template('index.html',)

@smrh.route('/graph')
def graph():
    with open(filename1, 'rb') as file:
        times = pickle.load(file)

    with open(filename2, 'rb') as file:
        readings = pickle.load(file)

    graph = pygal.Line(x_title='Horário Registrado', y_title='Consumo Total (m³)', show_legend=False, style=BlueStyle, x_label_rotation=10, human_readable=True, show_y_guides=False)
    graph.title = 'SMRH - Consumo Total de Água'

    # Show last 10 readings/times
    graph.x_labels = times[-10:]
    graph.add('Consumo', readings[-10:])

    graph_data = graph.render_data_uri()
    return render_template('graph.html', graph_data=graph_data)

if __name__ == '__main__':
    smrh.run(debug=True, host='0.0.0.0')
