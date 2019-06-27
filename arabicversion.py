#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
import flask
import json
from sparkapi import sparkapi
from memeapi import memeapi
import shutil
import os
import vision_core 
import plotty
import twitterfeeds
from logging.config import dictConfig

app = Flask(__name__)
sparkbot = sparkapi()
memegen  = memeapi()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/ubuntu/visionai/secret-brushlands-95547/google_vidion.json'



# Disable Certificate warning
try:
    requests.packages.urllib3.disable_warnings()
except:
    pass
from requests.auth import HTTPBasicAuth

@app.route('/hello',methods=['POST'])
def parsing():
    app.logger.info('New reqest ---------------------------------')
    data = request.json
    #print format(data['data']['id'])
    msg_id = data['data']['id']
    roomId = data['data']['roomId']
    app.logger.info('reqester : %s',data['data']['personEmail'])
    app.logger.info('reqester : %s',str(data['data']))

    if data['data']['personEmail']=='abdelbbot@sparkbot.io':
      return "OK"
    #image  = data['data']['files']
    app.logger.info('message id : %s',msg_id)
    app.logger.info('room id : %s',roomId)

    message_json = sparkbot.get_msg(str(msg_id))
    #print input_list
    #print word.split()[1]
    print message_json
    if "SHOW" in (message_json['text']).upper():
        #case of show stats
        stats_data = json.loads(open('stats.json').read())
        image_plot=plotty.plot_results(stats_data['emotions_stats'],stats_data['title'])
        sparkbot.post_rest_file(str(roomId),image_plot)
        sparkbot.post_msg_markdown(str(roomId),"### عدد التغريدات  :"+str(stats_data['count_stats']['twitter'])+ "\n"
                                               "### عدد الصور المحملة :"+str(stats_data['count_stats']['twitter']+stats_data['count_stats']['teams'])+ "\n"
                                                )

    elif "RESET" in (message_json['text']).upper():
        slices = message_json['text'].split('/')
        stats_data = json.loads(open('stats.json').read())
        for element in stats_data['emotions_stats']:
            element = 0

        stats_data['count_stats']['teams']=0
        stats_data['count_stats']['twitter']=0

        stats_data['emotions_stats']['Joy_likelihood']          = 0
        stats_data['emotions_stats']['Sorrow_likelihood']       = 0
        stats_data['emotions_stats']['Anger_likelihood']        = 0
        stats_data['emotions_stats']['Surprise_likelihood']     = 0
        stats_data['emotions_stats']['Under_exposed_likelihood']= 0
        stats_data['emotions_stats']['Blurred_likelihood']      = 0
        stats_data['emotions_stats']['Headwear_likelihood']     = 0

        stats_data['title']=slices[1]
        stats_data['twitter_hashtag']=slices[2]

        with open('stats.json', 'w') as jsonfile:
            json.dump(stats_data,jsonfile,indent=4)
        
    elif "FAKE" in (message_json['text']).upper():
        sparkbot.post_rest_file(str(roomId),"fake.png")
        
    elif "TWITTER" in (message_json['text']).upper():
        collage_file = twitterfeeds.twitter_bulk("#ciscosaudiai")
        sparkbot.post_rest_file(str(roomId),collage_file)

    else:
        #case of photo submition
        i=0
        for file in message_json['files']:
            
            image_file = sparkbot.get_file(file)
            image_name = str(msg_id)+'.JPG'

            open(image_name, 'wb').write(image_file.content)

            stats_data = json.loads(open('stats.json').read())

            results = vision_core.face_joy_joy_likelihood(image_name)

            

            stats_data['count_stats']['teams']+= 1
            stats_data['emotions_stats']['Joy_likelihood']          += results['results']['Joy_faces']
            stats_data['emotions_stats']['Sorrow_likelihood']       += results['results']['Sorrow_faces']
            stats_data['emotions_stats']['Anger_likelihood']        += results['results']['Anger_faces']
            stats_data['emotions_stats']['Surprise_likelihood']     += results['results']['Surprise_faces']
            stats_data['emotions_stats']['Under_exposed_likelihood']+= results['results']['Under_faces']
            stats_data['emotions_stats']['Blurred_likelihood']      += results['results']['Blurred_faces']
            stats_data['emotions_stats']['Headwear_likelihood']     += results['results']['Headwear_faces']

            
            with open('stats.json', 'w') as jsonfile:
                json.dump(stats_data,jsonfile,indent=4)
            #print results
            faces_n=len(results['faces'])
            likelihood_name = ('UNKNOWN', 'مستبعد جدا', 'مستبعد', 'محتمل','ممكن', 'ممكن جدا')
            if faces_n>=1:
                i=i+1
                analyses="### صورة: "+str(i)+ "\n"
                analyses=analyses+"#### عدد الوجوه المكتشفة : "+str(faces_n)+ "\n"
                for face in results['faces']:
                    #sparkbot.post_msg_markdown(str(roomId),"# Face: "+str(i))
                    analyses=analyses+"--- \n"
                    is_emotions=False
                    if face['joy_likelihood']>=2:
                        analyses=analyses+"#### فرح               :"+str(likelihood_name[face['joy_likelihood']])+ "\n"
                        is_emotions=True
                    if face['sorrow_likelihood']>=2:
                        analyses=analyses+"#### حزن            :"+str(likelihood_name[face['sorrow_likelihood']])+ "\n"
                        is_emotions=True
                    if face['anger_likelihood']>=2:
                        analyses=analyses+"#### غضب             :"+str(likelihood_name[face['anger_likelihood']])+ "\n"
                        is_emotions=True
                    if face['surprise_likelihood']>=2:
                        analyses=analyses+"#### تفاجئ          :"+str(likelihood_name[face['surprise_likelihood']])+ "\n"
                        is_emotions=True
                    if face['under_exposed_likelihood']>=2:
                        analyses=analyses+"#### Under exposed likelihood     :"+str(likelihood_name[face['under_exposed_likelihood']])+ "\n"
                        is_emotions=True
                    if face['blurred_likelihood']>=2:
                        analyses=analyses+"#### ضبابي            :"+str(likelihood_name[face['blurred_likelihood']])+ "\n"
                        is_emotions=True
                    if face['headwear_likelihood']>=2:
                        analyses=analyses+"#### لباس رأس          :"+str(likelihood_name[face['headwear_likelihood']])+ "\n"
                        is_emotions=True
                    if is_emotions==False:
                        analyses=analyses+"#### Nothing detected !"
                    myvar='%.2f' % (face['detection_confidence']*100)
                    #str(face['detection_confidence']*100)
                    analyses=analyses+"#### دقة التحليل   :"+myvar+ "\n"
                    

                    """
                    sparkbot.post_msg_markdown(str(roomId),
                                                           "#### Joy likelihood               :"+str(likelihood_name[face['joy_likelihood']])+ "\n"
                                                           "#### Sorrow likelihood            :"+str(likelihood_name[face['sorrow_likelihood']])+ "\n"
                                                           "#### Anger likelihood             :"+str(likelihood_name[face['anger_likelihood']])+ "\n"
                                                           "#### Surprise likelihood          :"+str(likelihood_name[face['surprise_likelihood']])+ "\n"
                                                           "#### Under exposed likelihood     :"+str(likelihood_name[face['under_exposed_likelihood']])+ "\n"
                                                           "#### Blurred likelihood           :"+str(likelihood_name[face['blurred_likelihood']])+ "\n"
                                                           "#### Headwear likelihood          :"+str(likelihood_name[face['headwear_likelihood']])+ "\n"
                                                           "#### Detection confidence         :"+str('{0:.0%}'.format(face['detection_confidence']))+ "\n"
                                                           "---"
                                                           )            
                    """    
            else:
                analyses="## No faces detceted!"
            sparkbot.post_msg_markdown(str(roomId),analyses)
            
    app.logger.info('END of reqest ---------------------------------')        

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
   app.run(host='0.0.0.0', port=8080)
