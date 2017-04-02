from flask import Flask
from flask import request
from flask import render_template
from forcast import fetchWeather, sortData

app = Flask(__name__)
listH = []

@app.route('/', methods=['POST', 'GET'])
def getWeather():
	if request.method == 'POST':
		listA = []
		key = request.form['key']
		data = fetchWeather(key, 1)

		if 'status' in data:
			return render_template('main.html',
				weather='No result. Need Help?')
		else:
			a = sortData(data, key, 1)
			listH.append(a[0])
			listA.append(a[0].split(' '))
			listA=listA[0]
			del listA[0]
			return render_template('main.html',
				city=listA[0],
				weather=listA[1],
				temp=listA[2],
				wind=listA[3])

	elif request.method == 'GET':

		if request.args.get('button') == 'Help':
			return render_template('main.html',
				help=' ')
		elif request.args.get('button') == 'History':
			return render_template('main.html',
				history=set(listH))
		else:
			return render_template('main.html')		

if __name__ == '__main__':
	app.run(port='0.0.0.0')
