import requests
import vision_core
import urllib
import json
import os
import collage_maker
import random



def twitter_bulk(hashtag):
	url = "https://api.twitter.com/1.1/tweets/search/30day/dev.json"

	payload = {"query":hashtag+"  has:images"}
	headers = {
	    'Authorization': "Bearer AAAAAAAAAAAAAAAAAAAAAHeb9gAAAAAApqM69%2FGYiTjnkT0SC4ahaAa0DXI%3DNatdu3xMa6q7nXQiVmfHBsMFJK2kfz5NKSDnHDTUtMaUIPSmw0",
	    'Content-Type': "application/json",
	    'cache-control': "no-cache"
	     }

	response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

	data_json = response.json()

	stats_data = json.loads(open('stats.json').read())

	stats_data['count_stats']['twitter']=0
	"""
	stats_data['emotions_stats']['Joy_likelihood']          =0
	stats_data['emotions_stats']['Sorrow_likelihood']       =0
	stats_data['emotions_stats']['Anger_likelihood']        =0
	stats_data['emotions_stats']['Surprise_likelihood']     =0
	stats_data['emotions_stats']['Under_exposed_likelihood']=0
	stats_data['emotions_stats']['Blurred_likelihood']      =0
	stats_data['emotions_stats']['Headwear_likelihood']     =0
	"""

	with open('stats.json', 'w') as jsonfile:
	    json.dump(stats_data,jsonfile,indent=4)

	for tweet in data_json['results']:
		for tweet_image in tweet['entities']['media']:
			print tweet_image['media_url']
			image_url = tweet_image['media_url']
			image_name = str(tweet_image['id'])+'.JPG'
			#ccheck if id exsits already
			stats_data = json.loads(open('stats.json').read())

			urllib.urlretrieve(image_url, 'twitterimg/'+image_name)

			ai_response = vision_core.face_joy_joy_likelihood('twitterimg/'+image_name)


			stats_data['count_stats']['twitter']+= 1
			stats_data['emotions_stats']['Joy_likelihood']          += ai_response['results']['Joy_faces']
			stats_data['emotions_stats']['Sorrow_likelihood']       += ai_response['results']['Sorrow_faces']
			stats_data['emotions_stats']['Anger_likelihood']        += ai_response['results']['Anger_faces']
			stats_data['emotions_stats']['Surprise_likelihood']     += ai_response['results']['Surprise_faces']
			stats_data['emotions_stats']['Under_exposed_likelihood']+= ai_response['results']['Under_faces']
			stats_data['emotions_stats']['Blurred_likelihood']      += ai_response['results']['Blurred_faces']
			stats_data['emotions_stats']['Headwear_likelihood']     += ai_response['results']['Headwear_faces']

			with open('stats.json', 'w') as jsonfile:
			    json.dump(stats_data,jsonfile,indent=4)
	twiter_folder='twitterimg'
	collage_file = 'collage.jpg'
	files = [os.path.join(twiter_folder, fn) for fn in os.listdir(twiter_folder)]
	images = [fn for fn in files if os.path.splitext(fn)[1].lower() in ('.jpg', '.jpeg', '.png')]
	random.shuffle(images)
	collage_maker.make_collage(images, collage_file, 800, 250)
	#print images
	return collage_file

if __name__ == '__main__':
   print twitter_bulk("#ciscosaudiai")