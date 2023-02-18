import json
a = "Ford"
b = "Mustang"
c = 1964
d = "red"

thisdict =	{
  "brand": a,
  "model": b,
  "year": c
}
#print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = d
print(thisdict)

json_str = json.dumps(thisdict)
json_inp = json.loads(json_str)

# the result is a JSON string:
print(json_inp)
print(json_inp["color"])