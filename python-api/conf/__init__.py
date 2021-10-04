import os

MONGODB_URI = f"mongodb://root:123456@{os.getenv('MONGODB_HOSTNAME') or 'localhost'}:27017/?authSource=admin"
