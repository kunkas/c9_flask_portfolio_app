from flask import Flask, render_template, request, redirect
import datetime
import pytz  # timezone
import requests
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')


@app.route('/<name>')
def profile(name):
    return render_template('index.html', name=name)


@app.route('/add_numbers', methods=['GET', 'POST'])
def add_numbers_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))
    if request.method == 'GET':
        return render_template('add_numbers.html')
    elif request.method == 'POST':
        print(request.form['text'].split())
        total = 0
        total2 = 1
        try:
            for str_num in request.form['text'].split():
                total += int(str_num)
                total2 = total2 * int(str_num)
            return render_template('add_numbers.html', result=str(total))
        except ValueError:
            return "Easy now! Let's keep it simple! At least 2 numbers with a space between them please"


@app.route('/multiply_numbers', methods=['GET', 'POST'])
def multiply_numbers_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))
    if request.method == 'GET':
        return render_template('add_numbers.html')
    elif request.method == 'POST':
        print(request.form['text'].split())
        total = 0
        total2 = 1
        try:
            for str_num in request.form['text'].split():
                total += int(str_num)
                total2 = total2 * int(str_num)
            return render_template('add_numbers.html', result1=str(total2))
        except ValueError:
            return "Easy now! Let's keep it simple! At least 2 numbers with a space between them please"


@app.route('/divide_numbers', methods=['GET', 'POST'])
def divide_numbers_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))
    if request.method == 'GET':
        return render_template('add_numbers.html')
    elif request.method == 'POST':
        print(request.form['text'].split())
        total = 0

        try:
            total2 = request.form['text'][0]
            for str_num in request.form['text'].split():
                total2 = int(total2) / int(str_num)
            return render_template('add_numbers.html', result=str(total2))
        except ValueError:
            return "Easy now! Let's keep it simple! At least 2 numbers with a space between them please"


shop_list = []


@app.route('/shopping_list', methods=['GET', 'POST'])
def shopping_list_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
        return render_template('shopping_list.html')
    elif request.method == 'POST':
        print(request.form['text'].split())

        try:
            for item in request.form['text'].split():
                shop_list.append(str(item))

            return render_template('shopping_list.html', result='\n'.join(shop_list))
        except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"

@app.route('/shopping_list', methods=['GET', 'POST'])
def clear_list_post():
    shop_list = []
    return shop_list


@app.route('/time', methods=['GET', 'POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))
    if request.method == 'GET':
        return render_template('time.html')
    elif request.method == 'POST':
        print(request.form['text'].split())

        for item in request.form['text'].split():
            item_str = str(item).lower()

            if item_str in (string.lower() for string in pytz.all_timezones):
                answer = (datetime.datetime.now(pytz.timezone(item_str)).strftime(
                    'Time = ' + '%H:%M:%S' + ' ' + item_str + ' TIME' + ' Year = ' + '%m-%d-%Y'))
                # answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
                # answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')
            else:
                answer = "Timezone not found. Please try another one."

            return render_template('time.html', result=answer)


@app.route('/python_apps')
def python_apps_page():
    # testing stuff
    return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run(debug=True)
