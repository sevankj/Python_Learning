from urllib2 import urlopen
from PIL import Image
import requests
from StringIO import StringIO
import Image

#kittens = urlopen('http://placekitten.com/200/300')

#f = open('kittens.jpg', 'wb')
# f.write(kittens.read())
#f.close()

#image=Image.open(kittens)

#image.show()



response = requests.get('http://placekitten.com/200/300')
img = Image.open(StringIO(response.content))