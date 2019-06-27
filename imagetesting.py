import requests
import shutil

url = "https://api.ciscospark.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvODBhOTk2YTAtNDkwNi0xMWU5LWE0ZjEtZWJjYWFmM2ZhM2VkLzA"

payload = ""
headers = {
    'Authorization': "Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
    'cache-control': "no-cache",
    'Postman-Token': "382e7329-a080-42cf-b88f-6a31a91ad9cb"
    }

response = requests.request("GET", url, data=payload, headers=headers)


open('google.jpg', 'wb').write(response.content)
"""
with open("image_name.jpg", 'wb') as out_file:
  response.raw.decode_content = True
  shutil.copyfileobj(response.raw, out_file)
"""

print "done"
