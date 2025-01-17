from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3
class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field cannot be blank.'
        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'item not found'}, 404 

  
    def post(self, name):
        if ItemModel.find_by_name(name):
            return  {'message':"item '{}' is already exists".format(name)}, 400                                        
        data= Item.parse.parse_args()
        print(data)
        item=ItemModel(name, data['price'])
        try:
            item.insert()
        except:
            return {"message":"an error occurred inserting the item."}, 500
        
        return item.json(), 201
        
    def delete(self,name):
        connection =sqlite3.connect('data.db')
        cursor=connection.cursor()

        query="DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': "Item DElETED"}

    def put(self,name):
        data= Item.parse.parse_args()

        item= ItemModel.find_by_name(name)
        update_item= ItemModel(name,data['price'])
        
        if item is None:
            try:
                update_item.insert()
            except:
                return {'message': "an error occurred inserting the item."}, 500

        else:
            try:
                update_item.update()
            except:
                return {'message': "an error occurred inserting the item."}, 500
            
        return update_item.json()


     
class ItemList(Resource):
    def get(self):
        return {'items': items}