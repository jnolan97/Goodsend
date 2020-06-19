from goodsend import app, Message, mail
from flask import render_template, request, redirect, url_for,Flask, request, jsonify
from goodsend.forms import UserInfoForm, PostForm, LoginForm

from goodsend.models import User, Post, check_password_hash

from flask_login import login_required,login_user,current_user,logout_user

from goodsend import app,routes






@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        user_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON
        todo : Return document that matches query ID
        all_todos : Return all documents
    """
    try:
        # Check if ID was passed to URL query
        user_id = request.args.get('id')    
        if user_id:
            todo = user_ref.document(user_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_users = [doc.to_dict() for doc in user_ref.stream()]
            return jsonify(all_users), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        user_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection
    """
    try:
        # Check for ID in URL query
        user_id = request.args.get('id')
        user_ref.document(user_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"