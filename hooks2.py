#!/usr/bin/python
from flask import Flask
from flask import request
import flask
import json
from sparkapi import sparkapi
from memeapi import memeapi
import shutil
import os
import unirest
import json


app = Flask(__name__)
sparkbot = sparkapi()
memegen  = memeapi()



@app.route('/hello',methods=['POST'])
def parsing():
   print "got that reqest "
   data = request.json
   print "parrsed"
   #print format(data['data']['id'])
   msg_id = data['data']['id']
   roomId = data['data']['roomId']
   print msg_id
   input_ret = sparkbot.get_msg(str(msg_id))
   #print input_list
   #print word.split()[1]
   input_ret[1] = input_ret[1].encode('ascii', 'ignore')
   print str(input_ret[1])

   if str(input_ret[1]) == 'help' :
      print "in help"
      sparkbot.post_txt_file(str(roomId),'help.txt')

   if str(input_ret[1]).startswith('abdel'):
      sparkbot.post_msg(str(roomId),"What happens on red sofa stays on red sofa !")
      sparkbot.post_file(str(roomId),'red_sofa.jpeg')
   else: 
      print "in genral "
      input_list = input_ret[1].split('|')
      url = "https://10.10.20.85/dna/intent/api/v1/template-programmer/template/deploy"
      headers = {
                 'x-auth-token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1YmU1NDBhNDA3MDBiMzAwNGMyNWVhOTgiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjViZTU0MGEzMDcwMGIzMDA0YzI1ZWE5NyJdLCJ0ZW5hbnRJZCI6IjViZTU0MGEyMDcwMGIzMDA0YzI1ZWE5NSIsImV4cCI6MTU0Mzg2MjQ1NiwidXNlcm5hbWUiOiJhZG1pbiJ9.MYAHKf9IwpGl3YLm4xbkd0q77ETWQEYpBq4uS9uADMc",
                 'content-type': "application/json",
                 'cache-control': "no-cache"
                 }
      payload = json.dumps({
                            "forcePushTemplate": "true",
                            "isComposite": "false",
                            "targetInfo": [
                                {
                                    "id": "927ccc99-68c0-4e84-b140-0a9199502f1e",
                                    "params": {"port":input_list[1],"vlanid":input_list[2]},
                                    "type": "MANAGED_DEVICE_UUID"
                                }
                            ],
                            "templateId": "2f0b2405-d0e5-482c-a4b8-ef94b0086f80"
                            })

      responseabdel = unirest.post( url, params=payload, headers=headers)

      #image_file=memegen.get_image(input_list[0],input_list[1],input_list[2])
      print  "done"


      
      print roomId
      sparkbot.post_msg(str(roomId),"got that")
      print "hello"



  

   return 'OK'

@app.route("/imgs/<path:path>")
def images(path):
    #generate_img(path)
    fullpath =  path # "./imgs/" + path
    resp = flask.make_response(open(fullpath).read())
    resp.content_type = "image/jpeg"
    return resp

@app.route("/txt/<path:path>")
def txt_files(path):
    #generate_img(path)
    fullpath =  path # "./imgs/" + path
    resp = flask.make_response(open(fullpath).read())
    resp.content_type = "text/plain"
    return resp

@app.route("/delete/<path:path>")
def removefile(path):
   try:
       os.remove(path)
   except Exception as error:
       app.logger.error("Error removing or closing downloaded file handle", error)
       print "error removing file" 
       print error
   return "OK"

if __name__ == '__main__':
   app.run()
