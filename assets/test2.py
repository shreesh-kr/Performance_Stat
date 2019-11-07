import json

dic = {'2019-11-03':[2,12]}
path = '/home/shreesh/Project/Performance-Stat/assets/data_json.json'
'''json_file = open(path, 'a')
json.dump(dic, json_file)
json_file.close()
'''
with open(path) as f:
  data = json.load(f)

print(len(data))