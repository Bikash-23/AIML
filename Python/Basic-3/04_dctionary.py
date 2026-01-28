# Dectionary:: key:value pairs (key:: unique)

info = {
   "name": "Bikash",
   "cgpa" : 8.75,
   "subjects": ["math","science","english"]
}
info["name"] = "bikash"
# print(info)
# print(type(info))
# print(type(info["subjects"]))

# ---------method----------
# dectionary.keys() :: return all keys
# dectionary.values() :: return all values
# dectionary.items() :: return (key,val) pairs
# dectionart.get(val) :: return val according to Key
# dectionary.update(new_item) :: adds new item to dictionary

# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("name"))
info.update({
    "ciry":"Kolkata"
})

print(info)