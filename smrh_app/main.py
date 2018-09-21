from flask import Flask, render_template, url_for
from pygal.style import BlueStyle
import pygal

smrh = Flask(__name__)

@smrh.route('/')
def index():
    return render_template('index.html',)

@smrh.route('/graph')
def graph1():
    graph = pygal.Line(x_title='Horario Registrado (h)', y_title='Consumo (m3)', show_legend=False, style=BlueStyle)
    graph.title = 'SMRH - Consumo de agua'
    graph.x_labels = ['10:00', '10:05', '10:10']
    graph.add('Consumo', [100, 150, 170])
    graph_data = graph.render_data_uri()
    return render_template('graph1.html', graph_data=graph_data)

if __name__ == '__main__':
    smrh.run(debug=True, host='0.0.0.0')
