import json 
  
#ini_string = '{"Geek" : 1,"forGeeks" : 2}' 
  
a = '{"name":"Ram", "email":"Ram@gmail.com"},{"name":"Bob", "email":"bob32@gmail.com"}'
# b = '{ "Subjects": {"Maths":85, "Physics":90"}}'
  
#printing initial ini_string 
print ("initial strings given - \n", a) 
  
#checking for string 
try: 
    json_object1 = json.loads(a) 
    # json_object2 = json.loads(b) 
    print ("Is valid json? true") 
      
except ValueError as e: 
    print ("Is valid json? false") 
