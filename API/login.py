from flask import Flask, jsonify, request

app = Flask(__name__)

creds = {'client_id':'',
     'client_secret':'',
     'shard':'US'}

token = onelogin.Token(**creds)
user = onelogin.User(token)


new_user = {
    'firstname':'Foo',
    'lastname':'Bar',
    'email':'foobarfoobar@foobarz123.local',
    'username':'foobar12321'
}
@app.route('/api/v1.0/register', methods=['GET' 'POST'])
def register():
    if user.user_exists(new_user['email']):

        found_user = user.get_user_by_id(
        user.search_users(
            'email',new_user['email'])[0]['data'][0]['id']
        )
        print "Can not create user, already exists \r\n {0}".format(found_user)
    else:
    Foo = user.create_user(**new_user)
    user_id = Foo['data'][0]['id']
    print 'Created User: {0}'.format(new_user)




if __name__ == '__main__':
    app.run(debug=True)