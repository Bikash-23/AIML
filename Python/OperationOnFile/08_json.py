import json

# ---------for deal with string----------------- 

# json.loads()::jsonString--> python obj 
# json.dumps()::python obj --> json string 

# json_str ='{"name":"Bikash","isTeacher":false}'
# py_obj = json.loads(json_str)

# print(type(py_obj),py_obj)

# py_obj = {
#     "name":"Bikash",
#     "isTeacher":True
# }
# json_str = json.dumps(py_obj)

# print(type(json_str),json_str)


# -------------for deal with file-------------------

# json.load() & json.dump()

# with open("Python\OperationOnFile\data.json","r") as f:
#     py_obj =  json.load(f)
#     print(py_obj)

data = {
    "name":"Bikash",
    "pin":721437,
    "ContactNo":+91232323
}
with open("Python\OperationOnFile\data.json","w") as f:
    json.dump(data,f,indent=2,sort_keys=True)