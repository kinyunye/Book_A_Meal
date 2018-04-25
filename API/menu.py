from flask import Flask, jsonify, request

app = Flask(__name__)

menu = [
    {
        "meal" : "Coconut Rice",
        "price" : "300"
        
    },
    {
    
        "meal" : "Coconut Rice",
        "price" : "300"
    }

]

@app.route('/meals/api/v1.0/meals', methods=['GET'])
def get_menu():
    return jsonify({'meals': meals})

@app.route('/meals/api/v1.0/meals', methods=['POST'])
def add_to_menu():
    add_menu = {"meal":request.json["meal"], "price":request.json["price"]}
    menu.append(menu)
    return jsonify({'menu':menu})


@app.route('/meals/api/v1.0/meals', methods=['PUT'])
def edit_menu(menu):
    menu = [menu for menu in meals if menu['menu'] == menu]
    meals[0]['meal'] = request.json['meal']
    return jsonify({'menu':menu[0]})

if __name__ == '__main__':
    app.run(debug=True)