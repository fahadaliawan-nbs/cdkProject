import json

with open('D:\\Ac_Fpo_Cross_Ref.json', 'r') as json_file:
    data = json.load(json_file)

count = 0;
simpleCount = 1
attribute = "xrefSearchKey"
length_json_list = len(data)
for x in range(length_json_list):
    item_length = len(data[x]['accountingPoList'])
    if item_length > 200:
        item_value = data[x][attribute]
        print("Largest number of objects at " + str(simpleCount) + " and count is " + str(item_length) + " with " +
              attribute + " = " + item_value)
    count = count + item_length
    simpleCount += 1

print("Total number of object counts under Json Array " + str(count))
print("Total number of objects in Json " + str(length_json_list))
