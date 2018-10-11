from flask import Flask
from flask import render_template
from flask import abort,request, jsonify
import json
items=[]
app = Flask(__name__,static_url_path='/files',static_folder='static',template_folder='static')

#####33#Database connect####################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
app.config['SECRET_KEY'] = "random"
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
#############################################


##### Model class ##############
class Items(db.Model):
    """A single item"""
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    item = db.Column(db.String(255))
    
    def __init__(self, item):
   	self.item = item
   	
    def __repr__(self):
    	#print self.__dict__
        return str(self.__dict__["item"])
################################



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
    global items
    data=request.json
    print data['item']
    new_item=Items(data['item'])
        
    if data['item']:
    	#items.append(data['item'])
	#####Db#########
	
	db.session.add(new_item)
        db.session.commit()
        
        items=Items.query.all()
        new_list=[ str(item) for item in items ]
        #######################
        	
	return jsonify(status=True,items=new_list)
     		 
    return jsonify(status=False,items=items)
    #return Response(data="data")

@app.route("/items")
def get_list():
    #obj=Items.query.filter_by(id=123).one() # searching one item
    global items
    items=Items.query.all()
    new_list=[ str(item) for item in items ]
    return jsonify(items=new_list)


    
if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0',port=3000,debug = True)

