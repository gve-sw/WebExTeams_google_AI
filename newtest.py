import requests

url = "https://api.ciscospark.com/v1/messages"

payload = "{\n  \"files\": \"http://ec2-3-81-210-166.compute-1.amazonaws.com:8080/imgs/fig2.png\",\n  \"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vYjhmZDAzYTAtNDg5Zi0xMWU5LThlOWQtN2ZiZDJmZjZjOWUw\"\n}"
headers = {
    'Authorization': "Bearer MzdmYTM2YzEtNjI0NS00MTM0LWI5NDYtNzY0ODEyYWE0ZmZhYzczZTQ1NTEtZmZh_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "a3cffba3-9bdf-415a-9f48-cd872d138da6"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
