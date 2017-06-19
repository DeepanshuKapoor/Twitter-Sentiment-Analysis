from flask import Flask,redirect,url_for,request,render_template
import csv
app=Flask(__name__)
"""
@app.route('/')
def hello():
	return "Hello Peeps"

@app.route('/<name>')
def hello_name(name):
	return "Hello"+name



@app.route("/url/<name2>")
def hello_user(name2):
	if name2=="Peeps":
		return redirect(url_for('hello'))
	else:
		return redirect(url_for('hello_name',name = name2))
"""

@app.route('/exectue')
def executefile():
	import tweet3
	return redirect(url_for("print"))




#Lets Build A Form


@app.route('/')
def hello_admin():
	return render_template('login.html')
@app.route('/<name>')
def hello_user(name):
	return "Hello"+" "+name

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=="POST":
		user=request.form["nm"]
		with open("keyword.txt","w") as fout:
			fout.write(user)
		#return 	redirect(url_for("hello_user",name=user))
		return redirect(url_for("read"))

@app.route('/read')
def read():
	import matplotlib
	matplotlib.use('TkAgg')	
	import tweepy
	import textblob
	import csv
	import matplotlib.pyplot as plt
	import pylab

	consumer_key = "yUXVJqUd36QHq6797UEX1X4kM"
	consumer_secret = "o6Pr23UFvqkrSCyAT8xarpJWQk1qQwVUXXY5tCO0BVLAgnQxDX"
	access_token = "846827615843336192-4N8GRMsDuQKxcwHwYPFgkcceMkUcucL"
	access_token_secret = "kvruasYZ3W3H2lBVfeI3yorpet6pdGCYzSjiBdTVxvAXf"

	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)

	api=tweepy.API(auth)

#Reading The File Keyword.txt to get the search Keyword
	with open("keyword.txt","r") as fin:
		x=fin.read()
	public_tweets=api.search(x)
	list1=[]
	list2=[]
	cn=0
	cp=0
	cng=0
	
	#with open("text2.csv","w",newline='') as fout:
	#	w=csv.writer(fout,delimiter=',')
	#	w.writerow([["Tweets"],["polarity"]])
	for tweet in public_tweets:
		list1.append(tweet.text)
		analysis=textblob.TextBlob(tweet.text).sentiment;
		if analysis.polarity>0.0:
			sentiments="positive"
			list2.append(sentiments)
			cp+=1
		elif analysis.polarity<0.0:
			sentiments="negative"
			list2.append(sentiments)
			cng+=1
		else:
			sentiments="neutral"
			list2.append(sentiments)
			cn+=1
	#dplt=[cp,cng,cn]
	return render_template("print.html",list=list,cp=cp,cn=cn,cng=cng,list1_list2=zip(list1,list2))


#@app.route('/print')
#def prints():
#	with open("text2.csv","r",newline="") as fin:
#		r=csv.reader(fin,delimiter=',')
#	for row in r:
#		return print(row[0])


if __name__=="__main__":
	app.run(debug=True)

#return redirect(url_for('hello_guest',guest = name))
