from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient


app = Flask(__name__)
ip ='localhost'
port = 27017
client = MongoClient(ip, port)
db = client.anti

@app.route('/')
def index():
    return render_template('enter.html')

@app.route('/home', methods= ['GET'])
def home():
    #posters 받아오기
    return render_template('home.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/q1')
def q1():
    return render_template('question1.html')

@app.route('/q2')
def q2():
    return render_template('question2.html')


@app.route('/q3')
def q3():
    return render_template('question3.html')

@app.route('/q3/list', methods= ['GET'])
def getWord():
    print('getWord()')
    star = list(db.wannabe.find({},{'_id':False, 'word':True}))
    print(star)
    return jsonify({'result': 'success', 'list': star})

@app.route('/poster', methods= ['POST'])
def poster():
    #localstorage에 있는 name, wannabe 보냄
    #name, wannabe img 받아와 load
    return render_template('poster.html')
    

@app.route('/poster/save', methods =['POST'])
def save():
    #이미지 서버에 저장
    #홈화면으로 redirect
    return

@app.route('/share', methods = ['GET'])
def share():
    #story list 불러오기
    return render_template('share.html')

@app.route('/share/story', methods = ['POST'])
def newStory():
    #new story 추가
    return 

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


