# bpl_id_system
 
Api сервер для идентификации юзеров BPL.

## Auth token

`/some_method?auth_token=<auth_token>`

## Методы


`/delete_user?user_id=<user_id>`

Returns User object in Ok.result

user_id - Integer.


`/get_user_by_id/<user_id>`

Returns User object in Ok.result

user_id - Integer.


`/get_user_by_nickname/<nickname>`

Returns User object in Ok.result

nickname - String.

`/get_user_by_tg_id/<tg_id>`

Returns User object in Ok.result

tg_id - Integer.


`/create_minecraft_user?nickname=<nickname>`

Returns User object in Ok.result

nickname - String.

`/create_minecraft_user?first_id=<first_id>&second_id=<second_id>`

Returns merged User object in Ok.result 

first_id - Integer.

second_id - Integer.

`/create_minecraft_user?nickname=<nickname>&tg_id`

Returns User object in Ok.result

nickname - String.

tg_id - Integer.


`/create_user?nickname=<nickname>&auth_method=<auth_method>&auth_string=<auth_string>`

Returns User object in Ok.result

nickname - String.

auth_method - String. (auth from auth list)

auth_string - String. (tg id, minecraft nickname, etc.)


`/set_money?user_id=<user_id>&count=<count>`

Returns Ok object.

user_id - Integer.

count - Integer.



`/inc_money?user_id=<user_id>&count=<count>`

Returns Ok object.

user_id - Integer.

count - Integer.



`/dec_money?user_id=<user_id>&count=<count>`

Returns Ok object.

user_id - Integer.

count - Integer.

## Обьекты

# User

```json
{"_id":1,
  "auth":{"email":["vezono@bpl.org"],"minecraft":["minecraft"],"phone_number":["+79631376940"],"telegram_id":["512006137"]},
  "connected_to":[],
  "money":0,
  "nickname":"Vezono2",
  "nicknames":[],
  "role":"member"}
```

# Ok
```json
{"ok": true,
"result": {}}
```

