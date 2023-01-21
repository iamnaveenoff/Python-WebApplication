# from requests import get

# ip = get('https://api.ipify.org').text
# # print('My public IP address is: {}'.format(ip))

# getip = format(ip)
# print(getip)


import json 
  
#ini_string = '{"Geek" : 1,"forGeeks" : 2}' 
  
a = '{"name":"John", "age":31, "Salary":25000}'
b = '{ "Subjects": {"Maths":85, "Physics":90"}}'
  
#printing initial ini_string 
print ("initial strings given - \n", a, "\n", b) 
  
#checking for string 
try: 
    json_object1 = json.loads(a) 
    json_object2 = json.loads(b) 
    print ("Is valid json? true") 
      
except ValueError as e: 
    print ("Is valid json? false") 


# data =[{
#   "ip": "157.50.44.179",
#   "isp": "Reliance Jio Infocomm Ltd",
#   "org": "Reliance Jio infocomm ltd",
#   "hostname": "157.50.44.179",
#   "latitude": 13.0827,
#   "longitude": 80.2707,
#   "postal_code": "600001",
#   "city": "Chennai",
#   "country_code": "IN",
#   "country_name": "India",
#   "continent_code": "AS",
#   "continent_name": "Asia",
#   "region": "Tamil Nadu",
#   "district": "Chennai",
#   "timezone_name": "Asia/Kolkata",
#   "connection_type": "Cellular",
#   "asn_number": 55836,
#   "asn_org": "Reliance Jio Infocomm Limited",
#   "asn": "AS55836 - Reliance Jio Infocomm Limited",
#   "currency_code": "INR",
#   "currency_name": "Indian Rupee",
#   "success": true,
#   "premium": false,
#   "cached": false
# }]

# import json
# try:
#     json_string =  '{"first_name": "Anurag", "last_name":"Rana", "key3": {"key1":"key2"}}'
#     print json.loads(json_string)
# except ValueError as e:
#     print e


# import json

# json_string =  '{"first_name": "Anurag", "last_name":"Rana", "key3": {"key1":"key2"}}'

# try:
#     parsed_json = json.loads(parsed_json)
#     print(json.dumps(parsed_json, indent = 4,sort_keys=False))
# except Exception as e:
#     print(repr(e))