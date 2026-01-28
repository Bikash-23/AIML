with open("Python\\OperationOnFile\\cities.json","w") as f:
    json.dump(city,f,indent=3,sort_keys=True)