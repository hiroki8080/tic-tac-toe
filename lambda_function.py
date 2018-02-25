import os
import json
from urllib.parse import parse_qs

DATA_FILE = '/'.join(['/tmp', 'data_file'])


def respond(square_list):
    return {
        'statusCode': '200',
        'body': render(square_list),
        'headers': {
            'Content-Type': 'text/html',
        },
    }


def render(square_list):
    html = '<html><body><h1>Sanmokunarabe</h1><table><form id="board-data" method="POST">'
    for i, square in enumerate(square_list):
        if i == 0 or i == 3 or i == 6:
            html += '<tr>'
        if square == '-':
            html += '<td><input type="radio" name="square" value="{}"></td>'.format(
                i+1)
        else:
            html += '<td>{}</td>'.format(square)
        if i == 2 or i == 5 or i == 8:
            html += '</tr>'
    html += '<tr><td colspan="2"><input type="submit" value="submit"><input type="checkbox" name="reset">Reset</td></tr>'
    html += '</table></form></body></html>'
    return html


def reset():
    with open(DATA_FILE, 'w+') as f:
        pass


def read():
    with open(DATA_FILE, 'r') as f:
        data = f.readline()
    return data


def write(data):
    with open(DATA_FILE, 'w') as f:
        f.write(data)


def process(square_index):
    if not os.path.isfile(DATA_FILE):
        reset()
    data = read()
    square_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    if square_index == -2 or (square_index == -1 and len(data) == 0):
        write(''.join(['B']+square_list))
    else:
        if square_index == -1:
            square_list = data[1:]
        else:
            if data.startswith('A'):
                data = ''.join(
                    [data[:square_index], 'x', data[square_index+1:]])
                square_list = data[1:]
                data = data.replace('A', 'B')
                write(data)
            else:
                data = ''.join(
                    [data[:square_index], 'o', data[square_index+1:]])
                square_list = data[1:]
                data = data.replace('B', 'A')
                write(data)
    return square_list


def lambda_handler(event, context):
    square_index = -1
    if 'body' in event:
        params = parse_qs(event['body'])
        if 'reset' in params:
            square_index = -2
        elif 'square' in params:
            square_index = int(params['square'][0])
    square_list = process(square_index)
    return respond(square_list)
