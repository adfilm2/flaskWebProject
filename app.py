from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient


app = Flask(__name__)
ip ='mongodb://anti:anti1234test@15.164.50.153'
port = 27017
client = MongoClient('mongodb://anti:anti1234test@15.164.50.153', port)
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
    posters = list(db.poster.find({},{'_id':False}))
    
    return jsonify({'result':'success', 'list':posters})

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
    star = list(db.wordEx.find({},{'_id':False, 'word':True}))
    
    return jsonify({'result': 'success', 'list': star})

@app.route('/q4')
def q4():
    return render_template('question4.html')

@app.route('/submit', methods= ['POST'])
def submit():
    print('submit')
    recword1 = request.form['word1']
    recword2 = request.form['word2']
    recword3 = request.form['word3']
    print(recword1+"+"+recword2+"+"+recword3)

    find1 = list(db.wannabe.find({"word":recword1}))    
    find2 = list(db.wannabe.find({"word":recword2}))
    find3 = list(db.wannabe.find({"word":recword3}))
    print(find1)
    print(find2)
    print(find3)

    result1 = ""
    result2 = ""
    result3 = ""

    if find1:
        print('find1 is not none')
        result1 = find1[0]['path']


    if find2:
        result2 = find2[0]['path']
        print('find2 is not none')


    if find3:
        result3 = find3[0]['path']
        print('find3 is not none')


    print(result1,result2,result3)
    
    return jsonify({'result':'success','words': [result1,result2,result3]})


@app.route('/poster')
def poster():

    return render_template('poster.html')
    

@app.route('/poster/archive', methods =['POST'])
def archive():
    poster = request.form['poster']
    db.poster.insert_one({'poster':poster})
    return jsonify({'result':'success'})

@app.route('/share')
def share():
    
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


