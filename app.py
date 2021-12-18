from bmi import BMI 
from flask import Flask, jsonify, request

# initiate flask object 
app = Flask('__name__')

@app.route('/',methods=['GET','POST'])
def get_input():
    
    packet = request.get_json(force=True)
    height = packet['height']
    weight = packet['weight']

    bmi = BMI(height,weight)

    return jsonify(packet,bmi)
    

app.run()
