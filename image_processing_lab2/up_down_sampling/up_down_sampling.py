import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def crop(start, end, origin_image):
    return origin_image[start[0]:end[0]+1,start[1]:end[1]+1]

def show_img(img):
    plt.figure()
    plt.imshow(img, cmap='gray', aspect='auto')
    plt.show()



def down_sampling(img, scale=2):
    """
    00    01   02   03
    10    11   12   13
    20    21   22   23
    30    31   32   33
    ==>
    00    02
    20    22
    #  0 2
    #  0, 1  ===>  0*2, 1*2   ====> 0, 2
    #  0, 1  ===>  0*3, 1*3   ====> 0, 3
    for i in xrange(2):
       for j in xrange(2):
    0,0   ==>   00
    0,1   ==>   02
    1,0   ==>   20
    1,1   ==>   22
    """
    new_img = np.zeros((img.shape[0]/scale,img.shape[1]/scale))
    R, C = new_img.shape
    for i in xrange(R):
        for j in xrange(C):
            new_img[i,j] = img[scale*i,scale*j]
    return new_img

def get_up_sampling_for_each_region(img):
    new_img = np.zeros((3,3))
    new_img[0,0]=img[0,0]
    new_img[0,2]=img[0,1]
    new_img[2,0]=img[1,0]
    new_img[2,2]=img[1,1]
   
    new_img[0,1]=(new_img[0,0]+new_img[0,1])/2.0
    new_img[2,1]=(new_img[2,0]+new_img[2,2])/2.0
    
    new_img[1,0]=(new_img[0,0]+new_img[2,0])/2.0
    new_img[1,2]=(new_img[0,2]+new_img[2,2])/2.0    

    new_img[1,1]=(new_img[0,1]+new_img[2,1])/2.0
    return new_img
def up_sampling(img, scale=2):
    """
    00    01   02   03
    10    11   12   13
    20    21   22   23
    30    31   32   33
    ==>
    00    02
    20    22
    #  0 2
    #  0, 1  ===>  0*2, 1*2   ====> 0, 2
    #  0, 1  ===>  0*3, 1*3   ====> 0, 3
    for i in xrange(2):
       for j in xrange(2):
    0,0   ==>   00
    0,1   ==>   02
    1,0   ==>   20
    1,1   ==>   22
    """
    new_img = np.zeros((img.shape[0]*scale,img.shape[1]*scale))
    R, C = img.shape
    for i in xrange(R-1):
        for j in xrange(C-1):
            new_img[scale*i:scale*i+3,scale*j:scale*j+3] = get_up_sampling_for_each_region(img[i:i+2,j:j+2]) 
    return new_img

file_name = "lena_gray.bmp"
file_name = "clown.bmp"
img = mpimg.imread(file_name)
down_sampled_img = down_sampling(img,4)
#img[:100,:] = tem_img
plt.figure()
plt.imshow(img, cmap='gray', aspect='auto')
plt.title("original image")
plt.show()
plt.close()

plt.figure()
plt.imshow(down_sampled_img, cmap='gray', aspect='auto')
plt.title("down sampled image")
plt.show()

up_sampled_img = up_sampling(down_sampled_img, 2)
new_up_sampled_img = up_sampling(up_sampled_img, 2)
plt.figure()
plt.imshow(new_up_sampled_img, cmap='gray', aspect='auto')
plt.title("up sampled image")
plt.show()

