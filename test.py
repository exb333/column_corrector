import re
import json
import requests
from itertools import izip
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
data = requests.get("https://datameer.labcorp.com:8443/rest/workbook/4611", auth=("bordee", "Stunner.123"), verify=False)

if data.status_code != 200:
	raise IOError("Sheet Not Found" + data.status_code )

collect_json=(data.json())
# print data.headers
# print collect_json

collect = json.dumps(collect_json)
print collect


# user_find = raw_input("Search Keyword")

# searched = re.compile(user_find, re.IGNORECASE)
#
# find = re.findall(searched, collect_json)
#
# for i in find:
# 	print find


# regex = r'\b' + re.escape(user_find) + r'\b'
# indices = [i for i, x in enumerate(collect_json['sheets']) if re.search(regex, x)]
# print indices

# user_replace = raw_input("Replace:")
#
# ss = re.compile(i , re.IGNORECASE)
# yy = re.findall(ss, stun)
# searched = re.search(ss, stun1)
# replaced = re.sub(searched.group(), user_replace, stun1)
# print replaced
#
# ss = re.compile(r'(^E\w+_|[^a-z]]?eliezer?)[_]?...\s?', re.IGNORECASE)
# yy = re.findall(ss, stun)
