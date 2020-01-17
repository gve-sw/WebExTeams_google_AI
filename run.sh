export FLASK_APP=newhook.py
export FLASK_DEBUG=1
export GOOGLE_APPLICATION_CREDENTIALS='google_vidion.json'
export Twitter_token=''
export Webexteams_token=''
export path_to_orca='/home/ubuntu/visionai/secret-brushlands-95547/orca'
flask run --host=0.0.0.0 --port=8080
lsof -i
