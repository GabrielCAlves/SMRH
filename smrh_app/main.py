from flask import Flask, render_template, url_for
from pygal.style import BlueStyle
import pickle
import pygal
import os

smrh = Flask(__name__)

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

filename1 = PATH + '/smrh_app/static/data/times.p'
filename2 = PATH + '/smrh_app/static/data/readings.p'

with open(filename1, 'rb') as file:
    times = pickle.load(file)

with open(filename2, 'rb') as file:
    readings = pickle.load(file)

@smrh.route('/')
def index():
    return render_template('index.html',)

@smrh.route('/graph')
def graph1():
    graph = pygal.Line(x_title='Horário Registrado (h)', y_title='Consumo (m³)', show_legend=False, style=BlueStyle)
    graph.title = 'SMRH - Consumo de Água'
    graph.x_labels = times
    # graph.x_labels = ['10:00', '10:05', '10:10']
    graph.add('Consumo', readings)
    # graph.add('Consumo', [100, 150, 170])
    graph_data = graph.render_data_uri()
    return render_template('graph1.html', graph_data=graph_data)

if __name__ == '__main__':
    smrh.run(debug=True, host='0.0.0.0')
