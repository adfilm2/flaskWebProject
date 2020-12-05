# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.dbsparta
#
# # 코딩 시작
# doc = { 'name' : 'bobby', 'age' : 21 }
# db.users.insert_one(doc)
import pymongo
from pymongo import MongoClient

ip ='localhost'
port = 27017

client = pymongo.MongoClient(ip, port)
db = client.anti


def insert():
    db.wannabe.delete_many({})
    wordlist = [
        {"word": "cool", "imgNo": 1},
        {"word": "gorgeous", "imgNo": 1},
        {"word": "awesome", "imgNo": 1},
        {"word": "rich", "imgNo": 2},
        {"word": "elegant", "imgNo": 1},
        {"word": "strong", "imgNo": 3},
        {"word": "handsome", "imgNo": 4},
        {"word": "kind", "imgNo": 1},
        {"word": "high","imgNo":4},
        {"word": "handsome", "imgNo": 4},
        {"word": "interesting", "imgNo": 2},
        {"word": "growing", "imgNo": 2}

    ]
    db.wannabe.insert_many(
        wordlist
    )
    stories = [
        {"story": "너무재밋다"},{"story":"할무니"}, {"story":"부자되세요"},{"story":"부자되세요를레이히리릴요요오로로리리ㅣ리릴리헤헤헷"}
    ]
    db.story.insert_many(stories)


insert()



