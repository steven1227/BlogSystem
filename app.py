from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
import time


comments = []


@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/comment',methods=['POST'])
def comment():
	comment = {'text':request.form['comment']}
	comment['id'] = comments[-1]['id']+1 if len(comments) else 1 
	comment['time'] = time.ctime()
	comments.append(comment)
	return 'it works'

@app.route('/delete',methods=['POST'])
def delete():
	pid = request.form['pid']
	global  comments
	comments = [item for item in comments if item['id']!= int(pid)]
	return 'it works'


@app.route('/home')
def home():
    return render_template('index.html',comments=comments)



@app.route('/')
def index():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)