from flask import Flask, jsonify, request
get_menu = Flask(__name__)

get_menu.debug = True

menu = [{'id':1,'meal':'Coconut Rice','Price':300},{'id':2,'meal':'Matoke','Price':350}]

@get_menu.route('/menu', methods=['GET'])
def returnAll():
	return jsonify({'menu': menu})


if __name__ == '__main__':
	get_menu.run()
