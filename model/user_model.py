import mysql.connector
import json
class user_model():
    #  for every model function we need to write the connection establishment code
        # to avoid this a constructor is created
    
    def __init__(self):
        # this constructor is automatically executed when the object is created in user_controller
            # connection establishment code
            # try:
            #    using self. can expand the scope of variable globally
               self.conn=mysql.connector.connect(host='localhost',user='root',password="123456",database='my_api')
               self.conn.autocommit=True
            #    automatically commit the executed query
               self.cur=self.conn.cursor(dictionary=True)
            #    cursor is the kind of agent to allow us to perform any operation in database
            #    print("connection successful")
            # except:
                #  print("error occurred")
            # both the python code and mysql service is in our machine so they are local to each other
            # even if they are hosted in some remote server ,they are still local to each other
    def user_getall_model(self):
        self.cur.execute("SELECT * from users")
        result=self.cur.fetchall()
        print(result)
        if len(result)>0:
         return {"payload":result}
        # to give the json response
        else:
             return "no data found"
    def user_addone_model(self,data):
        print(data)
        self.cur.execute(f"INSERT into users(name,emain,phone,role,password) VALUES('{data['name']}','{data['emain']}','{data['phone']}','{data['role']}','{data['password']}')")
        return {"msg":"user created successfully"}
    

    # by sending request and observing responses developer can test the functionality of api


    # at first we used postman to request api that is what we are creating
    # model and controller are the integral part of api handling data operation and request processing



    def user_update_model(self,data):
        print(data)
        self.cur.execute(f"UPDATE users SET name='{data['name']}', emain='{data['emain']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
         return {"msg":"user updated successfully"}
        else:
             return "no data to update"    #this is response
        
    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return {"msg":"user deleted successfully"}
        else:
            return "no available data to delete"





    # from postman we made post request to api and api make connection to database, so we accessed database through api