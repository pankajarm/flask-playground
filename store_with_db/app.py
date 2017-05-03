# Import the usual suspects
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister

# Create the Flask App object
app = Flask(__name__)
app.secret_key = 'pankaj-mathur'

# Create the Api object
api = Api(app)

# Let's create JWT instance

jwt = JWT(app, authenticate, identity) #auth


# for this section we are using in memory DB as python list and dictioaries

items = []

# Create the Resource Object

# class Item def started
class Item(Resource):
    """docstring for Item."""

    # parser
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="price spelling can't be changed"
    )

    # get jwt_required so it is required to authenticate before any Item api work
    @jwt_required()
    # override get method
    def get(self, name):
        # pythonic way
        item = next(filter(lambda x: x['name'] == name, items), None)

        # non pythonic way
        # or use filter function
        # for i in items:
        #     if i['name'] == name:
        #         return i
        # return {'item': item}, 200 if item is not None else 404

        return {'item': item}, 200 if item else 404

    # get jwt_required so it is required to authenticate before any Item api work
    @jwt_required()
    # override post method
    def post(self, name):
        # check if same item exist already
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message':"An item with name '{}' already exist".format(name)}, 400

        # get data
        # data = request.get_json() # amateur way

        # More efficent way to parsing data
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # we can also return 202, which mean accepted instead of created, usually when it long time to create object

    # get jwt_required so it is required to authenticate before any Item api work
    @jwt_required()
    # override delete method
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    # get jwt_required so it is required to authenticate before any Item api work
    @jwt_required()
    # override put method
    def put(self, name):
        # get data
        # data = request.get_json() # amateur way

        # More efficent way to parsing data
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)

        return item, 201 # we can also return 202, which mean accepted instead of created, usually when it long time to create object

# class def finished

# class ITEMS def started
class Items(Resource):
    """docstring for Item."""
    # get jwt_required so it is required to authenticate before any Item api work
    # @jwt_required()
    # override get method
    def get(self):
        return {'items': items}, 200

# class def finished

# Now add all Resource class to api with end point location
api.add_resource(Item, '/item/<string:name>') #http://localhost:5000/item/iphone
api.add_resource(Items, '/items') #http://localhost:5000/items
api.add_resource(UserRegister, '/register') #http://localhost:5000/register

# Now, run the whole app on flask
app.run(port=5000, debug=True) # default port is 5000 but you can change it to any free avaialble port on your system
