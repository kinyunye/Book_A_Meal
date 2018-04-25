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

@app.route('/meals/api/v1.0/meals', methods=['GET'])
def get_meals():
    return jsonify({'meals': meals})

@app.route('/meals/api/v1.0/meals', methods=['POST'])
def add_meal():
    meal = {"name":request.json["name"]}
    meals.append(meal)
    return jsonify({'meals':meals})


@app.route('/meals/api/v1.0/meals', methods=['PUT'])
def edit_meal(meal):
    meals = [meal for meals in meals if meal['name'] == name]
    meals[0]['name'] = request.json['name']
    return jsonify({'meal':meals[0]})


if __name__ == '__main__':
    app.run(debug=True)