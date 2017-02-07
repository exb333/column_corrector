import requests
import re
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def check_API():
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	data = requests.get("https://datameer.labcorp.com:8443/rest/workbook/4611.json", auth=("bordee", "Stunner.123"),
						verify=False)

	if data.status_code != 200:
		raise IOError("Sheet Not Found" + data.status_code)

	get_column_name(data=data)


def get_column_name(data=None):
	collect_json_data = data.json()
	# print collect_json_data
	print(data.headers)



	columnStyle_names = [elem['columnStyles'] for elem in collect_json_data['sheets']]
	formulas_names = [elem['formulas'] for elem in collect_json_data['sheets'] if 'formulas' in elem]
	columnStyle_data = [item['name'] for sheet in columnStyle_names for item in sheet]
	formulas_data = [item['columnName'] for sheet in formulas_names for item in sheet]

	search_and_replace(columnStyle_data=columnStyle_data, formulas_data=formulas_data,
					   collect_json_data=collect_json_data)


def search_and_replace(columnStyle_data=None, formulas_data=None, collect_json_data=None):
	user_input = raw_input("Enter the keyword you want to search:\t")

	fetch = [i for value in (columnStyle_data, formulas_data) for i in value]

	# count=0
	# for display in fetch:
	# 	if user_input in display.upper().lower():
	# 		print display
	# 		count+=1
	#
	# print "Total matches:",count


	user_replace = raw_input("Enter the replacing word:\t")

	for index, data in enumerate(collect_json_data['sheets']):

		if 'formulas' in data:
			for i in data['formulas']:
				# if user_input == i['columnName']:
				# 	i['columnName']=user_replace
				regex = re.compile(user_input, re.IGNORECASE)
				if re.search(regex, i['columnName']):
					i['columnName']= re.sub(re.search(regex, i['columnName']).group(), user_replace, i['columnName'])
					print i['columnName'], i['columnIndex']

			print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'

			for i in data['columnStyles']:
				# if user_input == i['name']:
				# 	i['name'] = user_replace
				# 	print i['name']
				# 	print i['columnName']
				regex = re.compile(user_input, re.IGNORECASE)
				if re.search(regex, i['name']):
					i['name']= re.sub(re.search(regex, i['name']).group(), user_replace, i['name'])
					print i['name']
			print "----------------------"

	print (collect_json_data)

	# response = requests.post("https://datameer.labcorp.com:8443/rest/workbook/4611.json", json=collect_json_data,
	# 						 auth=("bordee", "Stunner.123"), verify=False)
	# resp = requests.put('https://datameer.labcorp.com:8443/rest/workbook/4611',
     #                 data=json.dumps(collect_json_data),
     #                 headers={'Content-Type':'application/json'}, auth=("bordee", "Stunner.123"), verify=False)
	# print resp.status_code

	resp = requests.put('https://datameer.labcorp.com:8443/rest/workbook/4611',
                     data=json.dumps(collect_json_data),
                     headers={'Content-Type':'application/json'}, verify=False)

	print resp.status_code
	# bash_com = 'curl -u bordee:Stunner.123 -X PUT -d @%s "https://datameer.labcorp.com:8443/rest/workbook/4611"',  collect_json_data
	# subprocess.Popen(bash_com)
	# output = subprocess.check_output(['bash','-c', bash_com])
	# print output


if __name__ == '__main__':
	check_API()
