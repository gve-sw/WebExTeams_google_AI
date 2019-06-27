import requests

"""
url = 'https://api.ciscospark.com/v1/messages/'
headers = {"Authorization": "Bearer MGVjZGIxYTItZmU2OS00OTcwLWE1NjItMjVmZjM0YmZmMTlmN2VmMTQ4OTctYTY4"}
payload = {"roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vMjk0YWUyODAtOTE1NS0xMWU2LTk0YjktMTlhYzNjNGFkMTZj"}
payload2 = {"roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vMjk0YWUyODAtOTE1NS0xMWU2LTk0YjktMTlhYzNjNGFkMTZj",
             "text":"hi",
             "files":["imgl.jpeg"]}
files = {'media': open('imgl.jpeg', 'rb')}

requests.post(url, headers = headers , data=payload , files=files)
requests.post(url, headers = headers , data=payload2 ))
"""


url = "https://api.ciscospark.com/v1/messages/"

payload = {"roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vMjk0YWUyODAtOTE1NS0xMWU2LTk0YjktMTlhYzNjNGFkMTZj","text" : "hello"}
files = {'image': ('test.png', open('imgl.png', 'rb'))}
headers = {
    'authorization': "Bearer MGVjZGIxYTItZmU2OS00OTcwLWE1NjItMjVmZjM0YmZmMTlmN2VmMTQ4OTctYTY4",
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers,files=files)

print(response.text)