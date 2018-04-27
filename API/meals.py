from flask import Flask, jsonify, request

app = Flask(__name__)

meals = [
    {
        "name" : "Coconut Rice"
        
    },
    {
    
        "name" : "Coconut Rice"
        

    
    }

]

@app.route('/api/v1.0/meals', methods=['GET'])
def get_meals():
    return jsonify({'meals': meals})

@app.route('/api/v1.0/meals', methods=['POST'])
def add_meal():
    meal = {"name":request.json["name"]}
    meals.append(meal)
    return jsonify({'meals':meals})


@app.route('/api/v1.0/meals/<string:name>', methods=['PUT'])
def edit_meal(name):
    food = [meal for meal in meals if meal['name'] == name]
    food[0]['name'] = request.json['name']
    return jsonify({'meal':food[0]})


@app.route('/api/v1.0/meals/<string:name>', methods=['DELETE'])
def remove_meal(name):
    food = [meal for meal in meals if meal['name'] == name]
    meals.remove(food[0])
    return jsonify({'meals':meals})



if __name__ == '__main__':
    app.run(debug=True)