export FLASK_APP=newhook.py
export FLASK_DEBUG=1
export GOOGLE_APPLICATION_CREDENTIALS='/home/ubuntu/visionai/secret-brushlands-95547/google_vidion.json'
flask run --host=0.0.0.0 --port=8080
lsof -i
