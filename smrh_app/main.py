from flask import Flask, render_template
import pygal

smrh = Flask(__name__)

@smrh.route('/')
def index():
    grap = pygal.Bar()
    graph.title = 'Consumo de água'
    graph.x_labels = ['10:00', '10:05', '10:10']
    graph.add('Consumo em m³', [100, 150, 170])
    graph_data = graph.render_data_uri
    return render_template('index.html', graph_data)

if __name__ == '__main__':
    smrh.run(debug=True, host='0.0.0.0')
