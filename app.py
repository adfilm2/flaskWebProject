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
    
    return render_template('home.html')

@app.route('/home/poster', methods=['GET'])
def getPoster():
    # print('getPoster()')
    # posters = list(db.poster.find({},{'_id':False}))
    
    return jsonify({'result':'success', 'list':['성공성공','둘다성공']})

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/q1')
def q1():
    return render_template('question1.html')


# q1 test
@app.route('/q1/name', methods=['GET'])
def name():
    name = request.form['name']
    db.user.insert_one({name: name })
    return jsonify({'result': 'success','msg':'성공'})

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

@app.route('/submit', methods= ['POST'])
def submit():
    recword1 = request.form['word1']
    recword2 = request.form['word2']
    recword3 = request.form['word3']

    find1 = list(db.wannabe.find({"word":recword1}))
    find2 = list(db.wannabe.find({"word":recword2}))
    find3 = list(db.wannabe.find({"word":recword3}))
    # find1 = db.wannabe.find({"word": word1},{'_id':False})
    list1 = [ find1[0]['path'], find2[0]['path'], find3[0]['path'] ]
    print(find1)
    return jsonify({'result':'success','words': list1})


@app.route('/poster')
def poster():
    #localstorage에 있는 name, wannabe 보냄
    #name, wannabe img 받아와 load
    return render_template('poster.html')
    

@app.route('/poster/save', methods =['POST'])
def save():
    #이미지 서버에 저장
    #홈화면으로 redirect
    return

@app.route('/share')
def share():
    #story list 불러오기
    return render_template('share.html')

@app.route('/share/story', methods=['GET'])
def getStory():
    print('getStory()')
    story = list(db.story.find({},{'_id':False}))
    return jsonify({'result':'success', 'list':story})


@app.route('/share/newstory', methods = ['POST'])
def newStory():
    received = request.form['story']
    db.story.insert_one({'story':received})
    return jsonify({'result':'success'})

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


