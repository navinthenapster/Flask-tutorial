from flask import Flask
from flask import render_template
from flask import abort,request, jsonify
import json

app = Flask(__name__,static_url_path='/files',static_folder='static',template_folder='static')

items=[]

@app.route("/")
def root():
    #return render_template('index.html', items=["item1","item2","item3","item4"])
    return render_template('index.html')

@app.route('/echo', methods=['POST']) 
def echo():
    if not request.json:
        abort(400)
    print request.json
    return json.dumps(request.json)

    
@app.route("/add",methods=['POST'])
def add():       
    data=request.json
    print data['item']
    if data['item']:
    	items.append(data['item'])
    	return jsonify(status=True,items=items) 
    return jsonify(status=False,items=items)
    #return Response(data="data")

@app.route("/items")
def get_list():       
    return jsonify(items=items)


    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000,debug = True)

