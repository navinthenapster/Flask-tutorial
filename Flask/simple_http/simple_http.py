from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__,static_url_path='/files',static_folder='static',template_folder='static')

items=[]

@app.route("/")
def root():
    #return render_template('index.html', items=["item1","item2","item3","item4"])
    return render_template('index.html')
    
@app.route("/add/form",methods=['POST'])
def add():
    #print request.data
    form=request.form
    items.append(form.get("new_data"))
    return render_template('index.html', items=items)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000,debug = True)

