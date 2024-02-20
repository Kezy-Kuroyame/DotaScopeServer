from flask import Flask, request, jsonify
import json
import dataBase
from dataBase import *
import urllib.parse


# Создаем экземпляр Flask
app = Flask(__name__)

# Определяем обработчик для GET запроса на главную страницу
@app.route('/')
def index():
    return 'Привет, мир! Это серверная часть приложения.'


# Определяем обработчик для GET запроса на /hello
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.json
        insert_user(data['name'], data['password'])
        print(data)
        return data
    else:
        data = dataBase.get_users()
        result = [{'id_user': row[0], 'name': row[1], 'password': row[2]} for row in data]
        return jsonify(result)


@app.route('/users/<int:user_id>', methods=['GET'])
def user_by_id(user_id):
    data = dataBase.get_user_by_id(user_id)
    result = [{'id_user': row[0], 'name': row[1], 'password': row[2]} for row in data]
    return jsonify(result)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_name(name: str):
    data = dataBase.get_user_by_name(name)
    result = [{'id_user': row[0], 'name': row[1], 'password': row[2]} for row in data]
    return jsonify(result)


@app.route('/invokergame', methods=['GET', 'POST'])
def invoker_game():
    if request.method == 'POST':
        data = request.json
        if data['id_user'] != -1:
            insertGame(data['id_user'], data['score'])
        print(data)
        return data
    else:
        data = dataBase.get_invoker()
        result = [{'id_game': row[0], 'id_user': row[1], 'score': row[2]} for row in data]
        return jsonify(result)


@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    data = dataBase.get_leader_board()
    result = [{'name': row[0], 'score': row[1]} for row in data]
    return jsonify(result)


@app.route('/leaderboard/<int:user_id>', methods=['GET'])
def user_records(user_id: int):
    data = dataBase.get_user_records(user_id)
    result = [{'name': row[0], 'score': row[1]} for row in data]
    return jsonify(result)


if __name__ == '__main__':
    # Запускаем сервер на порту 5000
    app.run(debug=True)
