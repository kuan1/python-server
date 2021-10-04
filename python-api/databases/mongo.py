import pymongo
import conf

client = pymongo.MongoClient(conf.MONGODB_URI)

# 选择database
bookmark_db = client.bookmark
