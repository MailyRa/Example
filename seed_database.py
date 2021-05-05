
import os
import server
import model
import crud
import json


os.system('dropdb hellosisters')
os.system('createdb hellosisters')

model.connect_to_db(server.app)
model.db.create_all()

#creating users 
crud.create_user("test", "test@test.com", "test1" )
crud.create_user("jane", "jane@jane.com", "test")




#create blogs 
crud.create_blog("The world is yours", "Finishing school and graduating")
crud.create_blog("Go and get it!", "After graduation set yourself free")