# Photo Emotions Analyses
This is a prototype for a webext teams bot useing Google vision API to analyze emotions on pictures submitted trough webexteams or collected from twitter. the created bot will allow the user to submitt photos and get emotions analyses based on the response from google vision API, the bot can crowl twiiter hashatge and get back an anlyis of the shared photos.

![Wiring photo][flow]

[flow]:./flow.png "Wiring photo"

## Install:

#### Clone the repo :
```
$ git clone https://github.com/gve-sw/DNAC_usecase
```

#### Install dependencies :

```
$ pip install flask
$ pip install plotty
$ pip install unirest
$ pip install requests_toolbelt
$ pip install google-cloud-vision
```

install ORCA and keep note of the excutable path to create the envirenemont varibale path_to_orca https://github.com/plotly/orca
```
$export path_to_orca='/home/ubuntu/visionai/secret-brushlands-95547/orca'
```

## setup :
set up webexteams , twitter and google api accounts:
#### webex :
you can create a free account in webexteams [here](), once created you can follow the documentation [here](https://webexteamssdk.readthedocs.io/en/latest/user/quickstart.html) to create your first BOT, take note of the bot token as it will need to put it in an envirenemnt variable:
```
$ export Webexteams_token="Bearer your_token_here"
```
note : once online you need to setup a webhook for your bot : https://developer.webex.com/docs/api/v1/webhooks

#### Google vision API
Set up your google GCP console for authentication of your app and grab google application credentials file
https://cloud.google.com/vision/docs/libraries#client-libraries-install-python
export the path to your application credentials file :
```
$ export GOOGLE_APPLICATION_CREDENTIALS="/PATH/TO/YOUR/FILE/[FILE_NAME].json"
```

#### twitter API
twitter api used for this prototype is a premieum you will need to purshase a plan to be able to run the code, setup your developer account at twiiter and create the app for this project then genrate Bearer token : https://developer.twitter.com/en/docs/basics/authentication/guides/bearer-tokens

```
$ export Twitter_token="Bearer your_token_here"
```

#### Hosting :
you can host the code on a VM accsible on the internet or use Ngrok to route back to the code 

## Usage:
run the flask server :
```
$ python server.py 
```

creat a webexteams space and add the bot , start a conevrsation by mentioning the bot with the comand SHOW.
if you submitt a photo the bot will respond back with the emotional analyses :
![Wiring photo][photo]

[photo]:./Photo_bot.png "Wiring photo"

the bot will responde to the flowing comands :
RESET / title gose here / twtter hashtag goes here : this will set the bot for a round of emotion analyses it will capture from the photos published using the hashtag
TWITTER : this will run the emotion analyses on the photos collected from twitter and responde back with a collage of the photos
SHOW : this will show a pie shart reprentaing the emotional analyses from all the photos submitted
| Tables                 | Are                      | Cool                  |
| -----------------------| ------------------------ | --------------------- |
| ![Wiring photo][reset] | ![Wiring photo][twitter] | ![Wiring photo][show] |
 

[reset]:./Reset_bot.png "Wiring photo"
[twitter]:./Twitter_bot.png "Wiring photo"
[show]:./Show_bot.png "Wiring photo"


