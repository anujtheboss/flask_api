from app import app
from model.user_model import user_model
from flask import request
obj=user_model()
@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()
@app.route('/user/addone',methods=['POST'])
def user_addone_controller():
    # print(request.form)
    return obj.user_addone_model(request.form)
# /user/addone is api endpoint


# to call the function in user model from controller first we import the class from user model and
# initiallize an object to access that function call

# we get request from postman==>controller receive and redirect to model==>model pass to database
@app.route('/user/update',methods=['PUT'])
def user_update_controller():
    return obj.user_update_model(request.form)
@app.route('/user/delete/<id>',methods=['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)
# in case of deleting we get the api request along with id in the request url