import json
# people_string = '''{
# 	"people":[
# 		{"name":"jhon smith",
# 		"phone":"615-555-7164",
# 		"emails":["jognsmith@gmail.com", "jshonsmith@yahoo.com"],
# 		"has_licence":false},
# 		{"name":"jon doe",
# 		"phone":"605-500-7000",
# 		"emails":null,
# 		"has_licence":true}
# 	]
# }'''
# data = json.loads(people_string)
# print(type(data))
# print(type(data["people"]))
# print(data)
# for person in data["people"]:
# 	#print(person["name"])
# 	del person["phone"]
# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)
			# with open('states.json') as f:
			# 	data = json.load(f)
			# for state in data['states']:
			# 	#print(state['name'], state['abbreviation'])
			# 	del state['area_codes']
			# with open('new_states.json', 'w') as nf:
			# 	json.dump(data,nf, indent=2)
from urllib.request import urlopen
with urlopen("http://http://developer.yahoo.com/yql/console/?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22YHOO%22,%22AAPL%22,%22GOOG%22,%22MSFT%22/format=json") as response:
	source = responce.read()
print(source)
