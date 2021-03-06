from web.server import *


@app.route('/merge_users')
@require_token
def merge_users():
    first_id = request.args['first_id']
    second_id = request.args['second_id']
    if not first_id or not second_id:
        return api.errors.missing_args()
    return api.merge_users(first_id, second_id)


@app.route('/create_tg_user')
@require_token
def create_tg_user():
    nickname = request.args['nickname']
    tg_id = request.args['tg_id']
    if not nickname or not tg_id:
        return api.errors.missing_args()
    return api.create_tg_user(nickname, tg_id)


@app.route('/create_minecraft_user')
@require_token
def create_minecraft_user():
    nickname = request.args['nickname']
    if not nickname:
        return api.errors.missing_args()
    return api.create_minecraft_user(nickname)


@app.route('/create_user')
@require_token
def create_user():
    nickname = request.args['nickname']
    auth_method = request.args['auth_method']
    auth_string = request.args['auth_string']
    if not auth_string or not auth_method or not nickname:
        return api.errors.missing_args()
    return api.create_user(nickname, auth_method, auth_string)


@app.route('/add_connection')
@require_token
def add_connection():
    user_id = request.args['user_id']
    connection = request.args['connection']
    if not connection or not user_id:
        return api.errors.missing_args()
    return api.add_connection(user_id, connection)


@app.route('/add_auth')
@require_token
def add_auth():
    user_id = int(request.args['user_id'])
    auth_method = request.args['auth_method']
    auth_string = request.args['auth_string']
    if not auth_string or not auth_method or not user_id:
        return api.errors.missing_args()
    return api.add_auth(user_id, auth_method, auth_string)


@app.route('/delete_user')
@require_token
def delete_user():
    user_id = int(request.args['user_id'])
    if not user_id:
        return api.errors.missing_args()
    return api.delete_user(user_id)


@app.route('/remove_auth')
@require_token
def remove_auth():
    user_id = int(request.args['user_id'])
    auth_method = request.args['auth_method']
    auth_string = request.args['auth_string']
    if not auth_string or not auth_method or not user_id:
        return api.errors.missing_args()
    return api.remove_auth(user_id, auth_method, auth_string)


@app.route('/update_nickname')
@require_token
def update_nickname():
    nickname = request.args['nickname']
    user_id = int(request.args['user_id'])
    if not nickname or not user_id:
        return api.errors.missing_args()
    return api.update_nickname(user_id, nickname)


@app.route('/remove_nickname')
@require_token
def remove_nickname():
    nickname = request.args['nickname']
    user_id = int(request.args['user_id'])
    if not nickname or not user_id:
        return api.errors.missing_args()
    return api.remove_nickname(user_id, nickname)


@app.route('/set_money')
@require_token
def set_money():
    user_id = int(request.args['user_id'])
    count = int(request.args['count'])
    if not count or not user_id:
        return api.errors.missing_args()
    return api.set_money(user_id, count)


@app.route('/inc_money')
@require_token
def inc_money():
    user_id = int(request.args['user_id'])
    count = int(request.args['count'])
    if not count or not user_id:
        return api.errors.missing_args()
    return api.increase_money(user_id, count)


@app.route('/dec_money')
@require_token
def dec_money():
    user_id = int(request.args['user_id'])
    count = int(request.args['count'])
    if not count or not user_id:
        return api.errors.missing_args()
    return api.decrease_money(user_id, count)
