from testrail import *
import re
import pprint
import json
import base64
from collections import namedtuple
from collections import OrderedDict
import utils


client = APIClient('https://pivotusventures.testrail.io/')
client.user = 'gevorg_v@instigatemobile.com'
client.password = 'LoLt68aZAcXpob.1.q/b-DnZ.N1T.BS1zgqcvGG9Q'


case_id = '311'
run_id = '19413'
status = {'passed': '1',
          'failed': '5'
          }


case_template = 'Test case id is "{}".'
regex = re.compile(r'.(?<=Test case id is \").*(?=\".)')
# regex.search(arg)

status = namedtuple('statuses', 'count enabled color')
tup = status(count=1, enabled=True, color="red")
# print(namedtuple.__doc__)
print(tup)
# tup_dict = tup._asdict()
# print(tup_dict["color"])
print(status.__doc__)

# case = client.send_get('get_case/311')
# response = json.dumps(case, indent=4)
# # print(response)
# print('\n', case.get("custom_preconds"))
# print(type(case))
# print('\nID:\t', case.get("id"))
# print('Title:\t', case.get("title"))

print('===============================')
# result = client.send_post(
#     'add_result_for_case/19413/311',
#     {
#         'status_id': 1,
#         'comment': 'This test worked fine!'
#     }
# )
# print(json.dumps(result, indent=4))


# def encode(code_key, encoded_str):
#     enc = []
#     for i in range(len(encoded_str)):
#         key_c = code_key[i % len(code_key)]
#         enc_c = chr((ord(encoded_str[i]) + ord(key_c)) % 256)
#         enc.append(enc_c)
#     return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# def decode(code_key, encoded_str):
#     dec = []
#     encoded_str = base64.urlsafe_b64decode(encoded_str).decode()
#     for i in range(len(encoded_str)):
#         key_c = code_key[i % len(code_key)]
#         dec_c = chr((256 + ord(encoded_str[i]) - ord(key_c)) % 256)
#         dec.append(dec_c)
#     return "".join(dec)


# print(encode('testrail_api_key', client.password))
# print(decode('testrail_api_key', 'w4DDlMK_w6jCqMKZw4rDhsKgw4TDiMOZw47DjcKTwqrCosOWwqLDlsKfwqXDl8OGwo3Cr8Khwr3CjcKtwrjCqsOuw4zDpMOXw6jCqMKwwqXCsA=='))


collection_path = 'newman-collection-2019-04-15-11-43-04-445-0.json'
collection_data = utils.read_file(collection_path)
print(collection_data)
coll_json = json.loads(collection_data)
print(coll_json['item'][0]['name'])


cases_ids = OrderedDict()
cases_ids.update({'gago': 'gre'})
print(json.dumps(cases_ids, indent=4))
