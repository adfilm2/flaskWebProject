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
        {"word": "fair", "path": "../static/mapping/Fair.png"},
        {"word": "faithful", "path": "../static/mapping/Faithful.png"},
        {"word": "friendly", "path": "../static/mapping/Friendly.png"},
        {"word": "rich", "path": "../static/mapping/Rich.png"},
        {"word": "great", "path": "../static/mapping/Great.png"},
        {"word": "hip", "path": "../static/mapping/Hip.png"},
        {"word": "be loved", "path": "../static/mapping/BeLoved.png"},
        {"word": "loving", "path": "../static/mapping/Loving.png"},
        {"word": "passionate","path":"../static/mapping/Passionate.png"},
        {"word": "peaceful", "path": "../static/mapping/Peaceful.png"},
        {"word": "strong", "path": "../static/mapping/Strong.png"}
        

    ]
    db.wannabe.insert_many(
        wordlist
    )
    stories = [
        {"story": "너무재밋다"},{"story":"할무니"}, {"story":"부자되세요"},{"story":"부자되세요를레이히리릴요요오로로리리ㅣ리릴리헤헤헷"}
    ]
    db.story.insert_many(stories)


insert()



