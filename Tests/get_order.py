from flask import Flask, jsonify, request
get_order = Flask(__name__)



@get_order.route('/')
def index():
	return 'orders'
get_order.debug = True

orders = [{'Order No':001,'Date':24/04/2018,'Meal':'Coconut Rice','Price':300,'Quantity':1},
{'Order No':003,'Date':24/04/2018,'Meal':'Chicken Soup','Price':350,'Quantity':1}]

@get_order.route('/orders', methods=['GET'])
def returnAll():
	return jsonify({'orders': orders})


if __name__ == '__main__':
	get_order.run()
