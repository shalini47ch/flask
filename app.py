from flask import Flask,render_template,request,url_for
#render template inorder to return the entire html page
import pickle #for loading the model
import numpy as np #to convert the strings in the dataset to arrays

model=pickle.load(open('iri.pkl','rb')) #rb means return to binary

app=Flask(__name__)

@app.route('/')
def man():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])

def home():
	data1=request.form['a']
	data2=request.form['b']
	data3=request.form['c']
	data4=request.form['d']
	arr=np.array([[data1,data2,data3,data4]])
	#now performing prediction
	pred=model.predict(arr)
	return render_template('after.html',data=pred)

if __name__=="__main__":
	app.run(debug=False)
