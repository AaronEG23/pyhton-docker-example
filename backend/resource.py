import constant
import dataManager
import processPasiveRateHTML
import json
import http.server
import socketserver
from threading import Thread
    
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getPassiveRateAvg')
def getPassiveRateAvg():
	starYear = request.args.get('starYear')
	endYear = request.args.get('endYear')
	startMonth = request.args.get('startMonth')
	endMonth = request.args.get('endMonth')
	
	result =  dataManager.select(starYear, endYear, startMonth, endMonth)
	if (result != None):
		out =  '{ "value":'+ str(result) +' }'
	else:
		out =  '{ "value":"--" }'
	return json.loads(out)

def initialize():
	getInfoFlag = processPasiveRateHTML.process()
	if (getInfoFlag):
		app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
	initialize()


