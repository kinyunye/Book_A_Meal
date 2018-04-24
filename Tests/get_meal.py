from flask import Flask, jsonify, request
get_meal = Flask(__name__)



@get_meal.route('/')
def index():
	return 'MEALS'
get_meal.debug = True

meals = [{'hello':'wolrd'}]

@get_meal.route('/meals', methods=['GET'])
def returnAll():
	return jsonify({'meals': meals})


if __name__ == '__main__':
	get_meal.run()
