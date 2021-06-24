import json

string_of_json_data = '{"name": "Zophie", "isCat": "true", "miceCaught:": 0, "felineIQ": null}' # json string data are
# almost like a Python dictionary. Note that json data can contain booleans, integers, floats, strings, lists and even
# dictionaries, but not WebElements nor regex, nor readers and writers. Json data also use double quotes, and it's
# booleans are written in lower case

json_data_as_python_value = json.loads(string_of_json_data) # json.loads mean json load string

python_string_data = {'isCat': True, 'mice_caught': 0, 'name': 'Zophie'}
string_of_json = json.dumps(python_string_data)  # The json dump string translate a Python value into a string of JSON
# formatted data

print(string_of_json)

