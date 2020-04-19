from urllib import request

r = request.Request(url='http://localhost:5000/LAPI/V1.0/PeopleLibraries/1/People', data='{ "Key": "Value" }')

r = request.urlopen(r)

# r = r.read()

print(r)
