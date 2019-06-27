#!/usr/bin/python

import json
import requests
import unirest
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Disable Certificate warning
try:
    requests.packages.urllib3.disable_warnings()
except:
    pass
from requests.auth import HTTPBasicAuth

class sparkapi:

  def __init( self, x=0):
      self.key = 'Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

  def get_msg(self,id):
      url = "https://api.ciscospark.com/v1/messages/"+id
      payload = ""
      headers = {
          'Authorization': "Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
          'cache-control': "no-cache"
          }

      response = requests.request("GET", url, data=payload, headers=headers)

      return response.json()

  def get_file(self,file_url):
    response = requests.request("GET", url=file_url,
      headers={
        "Authorization": "Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
      }
    )
    return response

  def post_msg(self,grp,msg):
    response = unirest.post("https://api.ciscospark.com/v1/messages/",
      headers={
        "Authorization": "Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
        "Content-Type":"application/json"
      },
      params=json.dumps({"roomId":grp,"text":msg})
    )
    print response.body

  def post_msg_markdown(self,grp,msg):
    response = unirest.post("https://api.ciscospark.com/v1/messages/",
      headers={
        "Authorization": "Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
        "Content-Type":"application/json"
      },
      params=json.dumps({"roomId":grp,"markdown":msg})
    )
    print response.body
  def post_file(self,grp,file_o):
    print "me here ------------"

    response = unirest.post("https://api.ciscospark.com/v1/messages/", 
      headers={
        "Authorization": "Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
        "Content-Type":"application/json"},
      params=json.dumps({"roomId":grp,"files":["http://ec2-3-81-210-166.compute-1.amazonaws.com:8080/imgs/"+file_o]})
    ) 

  def post_rest_file(self,grp,file_o):
      m = MultipartEncoder({'roomId': grp,
                            'files': (file_o, open(file_o, 'rb'),
                            'image/png')})

      r = requests.post('https://api.ciscospark.com/v1/messages', data=m,
                        headers={'Authorization': 'Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f',
                        'Content-Type': m.content_type})



      print r.text
  def post_txt_file(self,grp,file_o):

    response = unirest.post("https://api.ciscospark.com/v1/messages/", 
      headers={
        "Authorization": "Bearer ZmZkZTJjZGItMTg4NS00MmIxLTk0N2MtZWM0YTUxMjE3ZTU4N2Q0ZjlkODgtZTI4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
        "Content-Type":"application/json"},
      params=json.dumps({"roomId":grp,"files":["https://secret-brushlands-95547.herokuapp.com/txt/"+file_o]})
    )  


"""    
app = sparkapi()

if __name__ == '__main__':
    #app.get_msg("Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYjg3Y2UyNDAtOTE0Mi0xMWU2LTk0YjktMTlhYzNjNGFkMTZj")
    app.post_msg('Y2lzY29zcGFyazovL3VzL1JPT00vMjk0YWUyODAtOTE1NS0xMWU2LTk0YjktMTlhYzNjNGFkMTZj','hellow world')

"""