from datetime import datetime
from bson import ObjectId
from flask import request

from database import bookmark_collection
from mytools import clean_object

# 书签列表


def bookmark_list():
    page = request.args.get('page', 1, int)
    size = request.args.get('size', 20, int)
    name = request.args.get('name', '')
    href = request.args.get('href', '')
    condition = {}
    if name:
        condition['name'] = {'$regex': name}
    if href:
        condition['href'] = {'$regex': href}
    res = bookmark_collection.find(condition).skip(
        (page - 1) * size).limit(size)
    res = list(res)
    for item in res:
        item['_id'] = str(item['_id'])
    return {'success': True, 'data': res}

# 添加书签


def bookmark_add():
    name = request.values.get('name', f'书签{datetime.now()}')
    href = request.values.get('href', '')
    tag = request.values.get('tag', '')

    payload = {
        "name": name,
        "href": href,
        "tag": tag
    }

    res = bookmark_collection.insert_one(payload)
    return {'success': True, 'data': str(res.inserted_id)}


def bookmark_remove():
    id = request.values.get('id', '')
    res = bookmark_collection.remove(ObjectId(id))
    return {'success': True, 'data': res}


def bookmark_update():
    id = request.values.get('id', '')
    name = request.values.get('name')
    href = request.values.get('href')
    tag = request.values.get('tag')
    payload = {
        "name": name,
        "href": href,
        "tag": tag
    }
    print(payload)
    res = bookmark_collection.update({id: ObjectId(id)}, clean_object(payload))
    return {'success': True, 'data': res}
