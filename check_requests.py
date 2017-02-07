import requests
from itertools import izip
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
data = requests.get("https://datameer.labcorp.com:8443/rest/workbook/4611", auth=("bordee", "Stunner.123"), verify=False)

if data.status_code != 200:
	raise IOError("Sheet Not Found" + data.status_code )

collect_json=(data.json())
des1 = []
sheet_names = [elem['columnStyles'] for elem in collect_json['sheets']]
sheet_number = [elem['name'] for elem in collect_json['sheets']]
count=0
for sheet in sheet_names:

	print "ColumnStyle Sheet Name: ", sheet_number[count]

	print "----------------------"
	count+=1
	for i, item in enumerate(sheet):
		des1.append(item['name'])
		print i, item['name']

	print "======================="

formula_sheet_names = [i['formulas'] for i in collect_json['sheets'] if 'formulas' in i]

formula_sheet_number = [elem['name'] for elem in collect_json['sheets'] if 'formulas' in elem]
count=0
des2 = []
for sheet in formula_sheet_names:
	print "Formula Sheet Name: ", formula_sheet_number[count]

	print "********************"
	count+=1
	for i, item in enumerate(sheet):
		des2.append(item['columnName'])
		print i, item['columnName']

	print "@@@@@@@@@@@@@@@@@@@@@@@@@"

# print formula_sheet_names
user = raw_input("Enter keyword that you want to search")
# #
# # if str(user) in formula_sheet_names:
# # 	print "Found", formula_sheet_names.index()
# #
# #
# # from itertools import groupby
# # [len(list(group)) for key, group in groupby(a)]
#
for sheet_search in (formula_sheet_names):
	for i, item in enumerate(sheet_search):
		if str(user) in item['columnName']:
			print i, item['columnName']

print "++++++++++++++++++++++"

# for sheet_search in (sheet_names):
# 	for i, item in enumerate(sheet_search):
# 		if str(user) in item['name']:
# 			print i, item['name']


change = raw_input("Enter keyword that you want to change")

for sheet_search in formula_sheet_names:
	for i, item in enumerate(sheet_search):
		# print i, item['columnName']
		if str(user) in item['columnName']:
			collect_json['sheets']['columnName']

# 		if str(user) in item['columnName']:
# 			print formula_sheet_names[i] #= str(change)
# # print formula_sheet_names
# # count= 0
# # for d in izip(des1, des2):
# # 	if str(user) in d:
# #
# # 		count+=1
# print count
# for key,  in izip(formula_sheet_names,sheet_names) :
# 	for i, item in enumerate(sheet_search):
# 		if str(user) in item['columnName']:
# 			item['columnName'] = str(change)
# 			print item



#
# import json
#
#
# def remove_dots(obj):
# 	for key in obj.keys():
# 		new_key = key.replace(".", "-")
# 		if new_key != key:
# 			obj[new_key] = obj[key]
# 			del obj[key]
# 	return obj
#
#
# output = collect_json['sheets']
# new_json = json.loads(json.dumps(output), object_hook=remove_dots)
#
# print new_json
#
