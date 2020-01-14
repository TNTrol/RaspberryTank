from flask import *
import time
from tank import Tank

app = Flask(__name__)
tank = Tank()

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/control/<int:state>", methods=['POST'])
def led(state):
	tank.doing(state)
	return ('', 204)

@app.route("/switch")
def switch():
	def state():
		yield 'data: {0}\n\n'.format(json.dumps({'dat':button,'act':fg}))
	time.sleep(1.0)
	return Response(state(), mimetype='text/event-stream')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, threaded=True) 
