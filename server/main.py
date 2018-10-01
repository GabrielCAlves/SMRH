from flask import Flask, render_template, url_for
from pygal.style import DefaultStyle
import pickle
import pygal
import os

smrh = Flask(__name__)

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

filename1 = PATH + '/static/data/times.p'
filename2 = PATH + '/static/data/readings.p'
filename3 = PATH + '/static/data/digits.p'

@smrh.route('/delete')
def delete():
    with open(filename1, 'rb') as temp_file:
        times = pickle.load(temp_file)

    with open(filename2, 'rb') as temp_file:
        readings = pickle.load(temp_file)

    with open(filename3, 'rb') as temp_file:
        digits = pickle.load(temp_file)

    del times[-1]
    del readings[-1]
    del digits[-1]

    with open(filename1, 'wb') as temp_file:
        pickle.dump(times, temp_file)
        temp_file.close()

    with open(filename2, 'wb') as temp_file:
        pickle.dump(readings, temp_file)
        temp_file.close()

    with open(filename3, 'wb') as temp_file:
        pickle.dump(digits, temp_file)
        temp_file.close()

    return render_template('delete.html')

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

    my_style = DefaultStyle(
        background='transparent',
        font_family='sans-serif',
        title_font_size=20,
        label_font_size=14,
        value_font_size=14,
        value_label_font_size=14,
        major_label_font_size=14,
        tooltip_font_size=16,
        colors=['#00A5DD'],
    )

    graph = pygal.Line(style=my_style, print_values=True, show_y_guides=False, show_legend=False, stroke_style={'width':3})
    graph.title = 'SMRH - Medições Realizadas'
    graph.x_title = 'Horário Registrado'
    graph.y_title = 'Valor Registrado em Litros'
    graph.dots_size = 4
    graph.tooltip_border_radius = 10
    graph.width = 1100

    times = times[-10:]
    readings = readings[-10:]

    # Show last 10 readings/times
    graph.x_labels = times
    graph.add('Consumo', readings)

    graph_data = graph.render_data_uri()
    return render_template('graph.html', graph_data=graph_data)

@smrh.route('/2graph')
def graph2():
    with open(filename1, 'rb') as temp_file:
        times = pickle.load(temp_file)

    with open(filename2, 'rb') as temp_file:
        readings = pickle.load(temp_file)

    my_style = DefaultStyle(
        background='transparent',
        font_family='sans-serif',
        title_font_size=20,
        label_font_size=14,
        value_font_size=14,
        value_label_font_size=14,
        major_label_font_size=14,
        tooltip_font_size=16,
        colors=['#00A5DD'],
    )

    graph = pygal.Line(style=my_style, print_values=True, show_y_guides=False, show_legend=False, stroke_style={'width':3})
    graph.title = 'SMRH - Consumo Total de Água'
    graph.x_title = 'Horário Registrado'
    graph.y_title = 'Consumo Total em Litros'
    graph.dots_size = 4
    graph.tooltip_border_radius = 10
    graph.width = 1100

    first_reading = readings[0]

    times = times[-10:]
    readings = readings[-10:]

    for x in range(10):
        atual = readings[x]
        readings[x] = atual - first_reading

    # Show last 10 readings/times
    graph.x_labels = times
    graph.add('Consumo', readings)

    graph_data = graph.render_data_uri()
    return render_template('2graph.html', graph_data=graph_data)

@smrh.route('/3graph')
def graph3():
    with open(filename1, 'rb') as temp_file:
        times = pickle.load(temp_file)

    with open(filename2, 'rb') as temp_file:
        readings = pickle.load(temp_file)

    my_style = DefaultStyle(
        background='transparent',
        font_family='sans-serif',
        title_font_size=20,
        label_font_size=14,
        value_font_size=34,
        value_label_font_size=14,
        major_label_font_size=14,
        tooltip_font_size=16,
        value_colors=['white'],
        colors=['#00A5DD'],
    )

    Config = pygal.Config
    Config.js = ['/static/svg.jquery.js',
                 '/static/pygal-tooltips.js']

    graph = pygal.Bar(style=my_style, print_values=True, show_y_guides=False, show_legend=False, stroke_style={'width':3})
    graph.title = 'SMRH - Consumo de Água no Período'
    graph.x_title = 'Horário Registrado'
    graph.y_title = 'Consumo no Período em Litros'
    graph.dots_size = 4
    graph.tooltip_border_radius = 10
    graph.width = 1100
    graph.x_label_rotation = 15

    last = readings[-54]
    last_time = times[-54]

    times1 = times[-50:]
    times = times[-10:]

    readings1 = readings[-50:]
    readings = readings[-10:]

    y = 0
    for x in range(0, 10):
        if x != 0:
            atual = readings1[y]
            ult = readings1[y-5]
            readings[x] = atual - ult
            y = y + 5
        else:
            atual = readings1[y]
            readings[x] = atual - last
            y = y + 5

    y = 0
    for x in range(0, 10):
        if x != 0:
            atual = times1[y]
            ult = times1[y-5]
            times[x] = ult + ' - ' + atual
            y = y + 5
        else:
            atual = times1[y]
            times[x] = last_time + ' - ' + atual
            y = y + 5

    # Show last 10 readings/times
    graph.x_labels = times
    graph.add('Consumo', readings)

    graph_data = graph.render_data_uri()
    return render_template('3graph.html', graph_data=graph_data)

if __name__ == '__main__':
    smrh.run(debug=True, host='0.0.0.0')
