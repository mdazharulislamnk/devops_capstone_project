from flask import jsonify, request, abort
from service import app, db
from service.models import Account

@app.route('/')
def index():
    return jsonify(
        name="Account REST API Service",
        version="1.0",
        paths=f"{request.base_url}accounts"
    ), 200


@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        abort(400, description="Invalid request")
    account = Account()
    account.deserialize(data)
    db.session.add(account)
    db.session.commit()
    return jsonify(account.serialize()), 201


@app.route('/accounts', methods=['GET'])
def list_accounts():
    accounts = Account.query.all()
    results = [account.serialize() for account in accounts]
    return jsonify(results), 200


@app.route('/accounts/<int:account_id>', methods=['GET'])
def read_account(account_id):
    account = Account.query.get(account_id)
    if not account:
        abort(404, description="Account not found")
    return jsonify(account.serialize()), 200


@app.route('/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    account = Account.query.get(account_id)
    if not account:
        abort(404, description="Account not found")
    data = request.get_json()
    account.deserialize(data)
    db.session.commit()
    return jsonify(account.serialize()), 200


@app.route('/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    account = Account.query.get(account_id)
    if account:
        db.session.delete(account)
        db.session.commit()
    return '', 204
