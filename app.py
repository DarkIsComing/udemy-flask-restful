from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from security import authenticate, identity

app=Flask(__name__)
app.config["SECRET_KEY"]='123'
api=Api(app)


jwt=JWT(app, authenticate, identity)




api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')

if __name__=="__main__":
    app.run(debug=True)
    
