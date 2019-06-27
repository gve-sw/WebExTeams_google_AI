import shutil
import requests

url = "https://ronreiter-meme-generator.p.mashape.com/meme?bottom=Bottom+text&font=Impact&font_size=50&meme=Condescending+Wonka&top=Top+text"
headers = {'X-Mashape-Key': '7CvEmUlp7DmshvNRS3kC8SLvG9RRp1wt3dFjsnR3JMTgI1hOQB'}
response = requests.get(url, headers = headers,stream=True)
with open('imgl.jpeg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response