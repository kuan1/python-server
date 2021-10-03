import pymongo

MONGODB_URI = 'mongodb://root:123456@localhost:27017/?authSource=admin'
client = pymongo.MongoClient(MONGODB_URI)

# 选择database
bookmark_db = client.bookmark
