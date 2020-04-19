import urllib.request

r = urllib.request.urlopen('http://localhost:5000/LAPI/V1.0/PeopleLibraries/BasicInfo')

r = r.read().decode('utf8')

print(r)

#input()
