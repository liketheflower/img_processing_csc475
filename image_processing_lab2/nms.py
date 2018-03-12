import re
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import os
import copy
import collections
def zero_padding(input_array):
    #insert zeros to the first column and first row
    output_array=np.insert(input_array, 0, values=0, axis=1)
    output_array=np.insert(output_array, 0, values=0, axis=0)
    z = np.zeros((len(output_array[:,0]),1))
    output_array= np.append(output_array, z, axis=1)
    z = np.zeros((1, len(output_array[0,:])))
    output_array= np.append(output_array, z, axis=0)
    #print(output_array)
    return output_array

def un_zero_padding(input_array):
    p=scipy.delete(input_array, 0, 1)
    p=scipy.delete(p, -1, 1)
    p=scipy.delete(p, 0, 0)
    p=scipy.delete(p, -1, 0)
    return p

    
    
def some_filter(original_image, filter):
    #zero padding is used for the boundary
    #here the image is the image_after_zero_padding
    #print("original_image",original_image.shape)
    image=zero_padding(original_image)
    #print("image_after_zero_padding.shape",image.shape)
    image_after_filter = np.zeros(image.shape)
    #print("image_after_filter.shape",image_after_filter.shape)
    for i in range (len(image[:,0])-2):
        for j in range(len(image[0,:])-2):
            image_after_filter[i+1][j+1]=image[i][j]*filter[0][0]+image[i][j+1]*filter[0][1]+image[i][j+2]*filter[0][2]+image[i+1][j]*filter[1][0]+image[i+1][j+1]*filter[1][1]+image[i+1][j+2]*filter[1][2]+image[i+2][j]*filter[2][0]+image[i+2][j+1]*filter[2][1]+image[i+2][j+2]*filter[2][2]
    image_after_filter=un_zero_padding(image_after_filter)
    #print(image_after_filter.shape)
    return image_after_filter


def combine_x_y_edge_image(x, y):
    """This function is used to combine the x direction edge image
    and the y direction image.
    The formular used here is sqrt(x^2+y^2)"""
    com_output = np.zeros(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            com_output[i,j]=math.sqrt(x[i,j]**2+y[i,j]**2)
    return com_output

def pure_bilinear_interpola(x,y,f00,f01,f10,f11):
    a =  np.matrix((1-x, x ))
    b =  np.matrix(((f00,f01),(f10, f11)))
    c =  np.matrix(((1-y,),(y,)))
    return  float(a*b*c)
def bilinear_interpola(i,j,thine_edge,x_direction_edge,y_direction_edge):
    if int(1000*x_direction_edge[i,j])==0:
        #print "warning the dy is almost 0."
        if i<4 and j<4:
            print ("warning the dx is almost 0.")

        return thine_edge[i,j-1],thine_edge[i,j+1]
    elif int(1000*y_direction_edge[i,j])==0:
        if i<4 and j<4:
            print ("warning the dy is almost 0.")
            print (thine_edge[i-1,j],thine_edge[i+1,j])
        return thine_edge[i-1,j],thine_edge[i+1,j]

    elif int(1000*x_direction_edge[i,j]*1000*y_direction_edge[i,j])>0:
        if int(1000*abs(y_direction_edge[i,j]))>int(1000*abs(x_direction_edge[i,j])):
            x = abs(x_direction_edge[i,j])/abs(y_direction_edge[i,j])
            y = 1.0
        else:
            x = 1.0
            y = abs(y_direction_edge[i,j])/abs(x_direction_edge[i,j])
        
        neg_x = 1-x
        neg_y = 1-y
            #if i<4 and j<4:
        
        positive_direction = pure_bilinear_interpola(x     ,     y,thine_edge[i,j],thine_edge[i,j+1],thine_edge[i+1,j],thine_edge[i+1,j+1])
        if i<4 and j<4:
            print ("I am here x*y>0 positive",i,j,x     ,     y,thine_edge[i,j],thine_edge[i,j+1],thine_edge[i+1,j],thine_edge[i+1,j+1])
            print ("I am here negative",i,j,neg_x , neg_y,thine_edge[i-1,j-1],thine_edge[i-1,j],thine_edge[i,j-1],thine_edge[i,j])
        negative_direction = pure_bilinear_interpola(neg_x , neg_y,thine_edge[i-1,j-1],thine_edge[i-1,j],thine_edge[i,j-1],thine_edge[i,j])
    else:
        if int(1000*abs(y_direction_edge[i,j]))>int(1000*abs(x_direction_edge[i,j])):
            x = 1-abs(x_direction_edge[i,j])/abs(y_direction_edge[i,j])
            y = 1.0
        
        else:
            x = 0.0
            y = abs(y_direction_edge[i,j])/abs(x_direction_edge[i,j])
    

        neg_x = 1-x
        neg_y = 1-y
            
        positive_direction = pure_bilinear_interpola(x     ,     y,thine_edge[i-1,j],thine_edge[i-1,j+1],thine_edge[i,j],thine_edge[i,j+1])
        if i<4 and j<4:
            print ("I am here x*y<0 positive",i,j,x     ,     y,thine_edge[i-1,j],thine_edge[i-1,j+1],thine_edge[i,j],thine_edge[i,j+1])
            print ("I am here negative",i,j,neg_x , neg_y,thine_edge[i,j-1],thine_edge[i,j],thine_edge[i+1,j-1],thine_edge[i+1,j])
        negative_direction = pure_bilinear_interpola(neg_x , neg_y,thine_edge[i,j-1],thine_edge[i,j],thine_edge[i+1,j-1],thine_edge[i+1,j])
    if i<4 and j<4:
  
        print ("positive_direction,negative_direction",positive_direction,negative_direction)

    return positive_direction,negative_direction


def non_max(blur_edge,x_direction_edge,y_direction_edge):
    '''do the non_max compression based on the canney edge detector algo'''

    blur_edge=zero_padding(blur_edge)
    thine_edge = copy.deepcopy(blur_edge)
    
    x_direction_edge=zero_padding(x_direction_edge)
    y_direction_edge=zero_padding(y_direction_edge)
    for i in range(thine_edge.shape[0]-2):
        for j in range(thine_edge.shape[1]-2):
            positive_direction,negative_direction=bilinear_interpola(i+1,j+1,blur_edge,x_direction_edge,y_direction_edge)
            non_max_indicator=thine_edge[i+1,j+1]<=positive_direction or thine_edge[i+1,j+1]<=negative_direction
            if non_max_indicator:
                thine_edge[i+1,j+1]=0
    thine_edge=un_zero_padding(thine_edge)
    return thine_edge
