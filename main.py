from time import sleep
import requests
import matplotlib.pyplot as pyplot
import numpy as np

url = "https://cdn2.poz.com/71174_RHSP-19-004.jpg_01b83f5c-df2d-41af-90e8-12f8af59feb8.jpeg"
img_data_from_url = requests.get(url, stream=True).raw

img = pyplot.imread(img_data_from_url, format="jpeg")

pyplot.imshow(img)
pyplot.show(block=False)

pyplot.pause()

pyplot.close()
