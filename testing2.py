import requests

url = "https://api.ciscospark.com/v1/messages/Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNTgwMDFhNzAtNDhkMC0xMWU5LWE0ZjEtZWJjYWFmM2ZhM2Vk"

payload = ""
headers = {
    'Authorization': "Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
    'cache-control': "no-cache",
    'Postman-Token': "2ff5cd45-7e51-4c7f-a43a-7e658c5f8e36"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
