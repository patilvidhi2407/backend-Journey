import json

people_string = '''
{
    "people" : [
        {
            "name": "Vidhi Patil",
            "phone" : "615-892-476",
            "emails": ["patilsunil2091@gmail.com" , "vidhisunil1234@gmail.com"],
            "has_license": false
        }
        ,
        {
        "name": "vishal sharma",
        "phone": "152-789-456",
        "emails" : null,
        "has_license": true
        }
    ]
}
'''

# data = json.loads(people_string)

# print(type(data))
# print(data)
# print(type(data['people']))

# for person in data['people']:          #since people is list we can use for loop
    # print(person)
    # print(person['name'])
    # del person['phone']

# new_string = json.dumps(data)
# new_string = json.dumps(data,indent=2)      # for better visibility
# new_string = json.dumps(data,indent=2,sort_keys=True)      # it will sort the keys

# print(new_string)

###### json file to python object

#import json

# with open('states_data.json') as f:
#     data = json.load(f)

# for state in data['states']:
#     # print(state)
#     # print(state['name'],state['abbreviation'])
#     del state['area_codes']

# with open('new_states_data.json','w') as f:
#     json.dump(data,f,indent=2)


##### take data from API

#import json

from urllib.request import urlopen

with urlopen("https://api.exchangerate-api.com/v4/latest/USD") as response:
    source = response.read()


# print(source)
data = json.loads(source)
# print(data)

# print(json.dumps(data,indent=2))
# print(len(data['rates']))

usd_rates = dict()
for item,value in data['rates'].items():            # as rates is an dictionary
    # print(item,value)
    usd_rates[item] = value

print(usd_rates["INR"])