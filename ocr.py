import argparse
import io
import os
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw,ImageGrab
import base64
import webbrowser
ImageGrab.grab(bbox=(0,50,400,700)).save('G:\image\image2.jpg','JPEG')
def detect_text():
    client = vision.ImageAnnotatorClient()
    with io.open(first, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')
    #print('\n"{}"'.format(texts[0].description))
    print(texts[0])
    question = texts[0].description
    question = question.splitlines()
    #question = question.replace('\n',' ')
    question = question[1:len(question)-3]
    #question = question.replace('\n',' ')
    phrase = ''
    for word in question:
	phrase += word+' '
    print(phrase)
    #phrase = phrase.replace('/n',' ')
    print(question)
    newlist=texts[0].description
    newlist=newlist.replace('\n',' ')
    newlist=newlist.split(' ')
    newlist=newlist[1:len(newlist)]
    length=len(newlist)
    lengt=min(length,5)
    for i in  range(0,lengt):
	if str(newlist[i])=='ELIMINATED':
            newlist[i]=' '
    phrase1=''
    for word in newlist:
	phrase1 +=word+' '
    print(phrase1)
    query = 'https://google.com/search?q='+phrase1
    webbrowser.open(query)

        #print('bounds: {}'.format(','.join(vertices)))
f_start ='G:\image\image'
first_in = '2'
#raw_input("enter the number")
f_end =  '.jpg'
s_end = '_change.jpg'
first = f_start+first_in+f_end
second = f_start+first_in+s_end
print(first)
detect_text()
