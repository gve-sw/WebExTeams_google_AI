#!/usr/bin/python

import json
import requests
import unirest
from requests_toolbelt.multipart.encoder import MultipartEncoder

import os

webexteams_token=os.environ['Webexteams_token']


# Disable Certificate warning
try:
    requests.packages.urllib3.disable_warnings()
except:
    pass
from requests.auth import HTTPBasicAuth

class sparkapi:

  def __init( self, x=0):
      self.key = webexteams_token

  def get_msg(self,id):
      url = "https://api.ciscospark.com/v1/messages/"+id
      payload = ""
      headers = {
          'Authorization': webexteams_token,
          'cache-control': "no-cache"
          }

      response = requests.request("GET", url, data=payload, headers=headers)

      return response.json()

  def get_file(self,file_url):
    response = requests.request("GET", url=file_url,
      headers={
        "Authorization": webexteams_token
      }
    )
    return response

  def post_msg(self,grp,msg):
    response = unirest.post("https://api.ciscospark.com/v1/messages/",
      headers={
        "Authorization": webexteams_token,
        "Content-Type":"application/json"
      },
      params=json.dumps({"roomId":grp,"text":msg})
    )
    print response.body

  def post_msg_markdown(self,grp,msg):
    response = unirest.post("https://api.ciscospark.com/v1/messages/",
      headers={
        "Authorization": webexteams_token,
        "Content-Type":"application/json"
      },
      params=json.dumps({"roomId":grp,"markdown":msg})
    )
    print response.body
  def post_file(self,grp,file_o):
    print "me here ------------"

    response = unirest.post("https://api.ciscospark.com/v1/messages/", 
      headers={
        "Authorization": webexteams_token,
        "Content-Type":"application/json"},
      params=json.dumps({"roomId":grp,"files":["0.0.0.0:8080/imgs/"+file_o]}) #your host should go here
    ) 

  def post_rest_file(self,grp,file_o):
      m = MultipartEncoder({'roomId': grp,
                            'files': (file_o, open(file_o, 'rb'),
                            'image/png')})

      r = requests.post('https://api.ciscospark.com/v1/messages', data=m,
                        headers={'Authorization': webexteams_token,
                        'Content-Type': m.content_type})



      print r.text
  def post_txt_file(self,grp,file_o):

    response = unirest.post("https://api.ciscospark.com/v1/messages/", 
      headers={
        "Authorization": webexteams_token,
        "Content-Type":"application/json"},
      params=json.dumps({"roomId":grp,"files":["https://secret-brushlands-95547.herokuapp.com/txt/"+file_o]})
    )  
