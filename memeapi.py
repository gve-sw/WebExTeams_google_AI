import unirest
import requests


class memeapi:
  def __init( self, x=0):
      self.key = x

  def get_image(self,image='',top='',bottom=''):
    print '|'+image.strip() +'|'+top+'|'+bottom+'|'

    url = "https://ronreiter-meme-generator.p.mashape.com/meme"
    headers = {'X-Mashape-Key': '7CvEmUlp7DmshvNRS3kC8SLvG9RRp1wt3dFjsnR3JMTgI1hOQB'}
    playloads={"bottom" : bottom,"font":"Impact","font_size":"50","meme":image.strip() ,"top":top}
    response = requests.get(url, headers = headers, params=playloads,stream=True)
    #print response.headers
    #print response.body
    #print response.raw_body
    """
    text_file = open("Output.png", "w")
    text_file.write(response.body)
    text_file.close()    
    return response.raw_body
    """
    return response


"""
app = urbandic()

if __name__ == '__main__':
    app.get_def("abdel")
"""

