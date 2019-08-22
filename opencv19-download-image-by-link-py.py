# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:44:21 2019

@author: VishalK
"""

import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    
    if not os.path.exists('neg1'):
        os.makedirs('neg1')
        
    pic_num = 1
    
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i,"neg1/"+str(pic_num)+'.jpg')
            img = cv2.imread("neg1/"+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img,(100,100))
            cv2.imwrite("neg1/"+str(pic_num)+'.jpg',resized_image)
            pic_num+=1
            
        except Exception as e:
            print(str(e))
            
#store_raw_images()            


            

def find_uglies():
    for file_type in ['neg1']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies1'):
                try:
                    current_image_path = str(file_type) + '/'+str(img)
                    ugly = cv2.imread('uglies1/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    
                    if ugly.shape == question.shape and not (np.bitwise_xor(ugly,question).any()):
                        print('dayyyyummmm you ugly!')
                        print(current_image_path)
                        os.remove(current_image_path)
                        
                except Exception as e:
                    print(str(e))
                    
                    
                    
#find_uglies()
                    

def create_pos_n_neg():
    for file_type in ['neg1']:
        
        for img in os.listdir(file_type):
            if file_type == 'neg1':
                line = file_type + '/'+img+'\n'
                with open ('bg.txt','a') as f:
                    f.write(line)
                    
            elif file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
                    
create_pos_n_neg()