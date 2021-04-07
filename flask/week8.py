from flask import Flask, jsonify, request
import sqlalchemy as alch

app = Flask(__name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@db/week8"
engine = alch.create_engine(SQLALCHEMY_DATABASE_URL)

@app.route('/')
def default():
    return 'Hello, Shakes!'

@app.route('/milkshakes', methods=['GET'])
def GetAllShakes():
    query = 'SELECT * FROM milkshakes'
    ResultProxy = engine.connect().execute(query)
    ResultSet = ResultProxy.fetchall()
    
    return jsonify([dict(row) for row in ResultSet])

@app.route('/milkshakes/new', methods=['POST'])
def newShake():
    shake = {
        'flavor': request.json['flavor'],
        'size': request.json['size'],
        'price': request.json['price']
    }
    
    query = "INSERT INTO milkshakes(flavor,size,price) VALUES(%s,%s,%s)"
    engine.connect().execute(query,(shake["flavor"],shake["size"],shake["price"]))
    
    return jsonify(shake)
    
    