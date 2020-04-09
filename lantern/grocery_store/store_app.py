from flask import Flask, jsonify, request

import inject


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'


class NoSuchGoodError(Exception):
    def __init__(self, good_id):
        self.message = f'No such good_id {good_id}'


class NoSuchStoreError(Exception):
    def __init__(self, store_id):
        self.message = f'No such store_id {store_id}'


app = Flask(__name__)


@app.errorhandler(NoSuchUserError)
def my_error_handler_user(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchGoodError)
def my_error_handler_good(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchStoreError)
def my_error_handler_store(e):
    return jsonify({'error': e.message}), 404


@app.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/users/<int:user_id>')
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user), 200


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = inject.instance('DB')
    db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status': 'success'}), 200


@app.route('/goods', methods=['POST'])
def add_goods():
    db = inject.instance('DB')
    goods = db.goods.add_goods_by_id(request.json)
    return jsonify({'numbers of items created': 10}), 201


@app.route('/goods/<int:good_id>', methods=['GET'])
def get_goods(good_id):
    db = inject.instance('DB')
    good = db.goods.get_goods_by_id(good_id)
    return jsonify(good), 200


@app.route("/goods/<int:good_id>", methods=["PUT"])
def update_goods(good_id):
    db = inject.instance("DB")
    db.goods.update_goods_by_id(good_id, request.json)
    return jsonify({'successfully_updated': 1}), 200


@app.route('/store', methods=['POST'])
def add_store():
    db = inject.instance('DB')
    store_id = db.stores.add_store_by_id(request.json)
    return jsonify({'store_id': store_id}), 201


@app.route('/store/<int:store_id>', methods=['GET'])
def get_store(store_id):
    db = inject.instance('DB')
    store = db.stores.get_store_by_id(store_id)
    return jsonify(store), 200


@app.route('/store/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    db = inject.instance('DB')
    db.stores.update_store_by_id(store_id, request.json)
    return jsonify({'status': 'success'}), 200
