import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def crop(start, end, origin_image):
    return origin_image[start[0]:end[0]+1,start[1]:end[1]+1]

def show_img(img):
    plt.figure()
    plt.imshow(img, cmap='gray', aspect='auto')
    plt.show()

def mean_filter_new(img):
    # mean filter
    filter_ =[[1/9.0 ,1/9.0, 1/9.0],
              [1/9.0 ,1/9.0, 1/9.0],
              [1/9.0 ,1/9.0, 1/9.0]]
    # gaussian filter
    filter_ =[[1/16.0 ,2/16.0, 1/16.0],
              [2/16.0 ,4/16.0, 2/16.0],
              [1/16.0 ,2/16.0, 1/16.0]]
    
    # sobel filter row(x) direction
    filter_ =[[-1 ,0, 1],
              [-2 ,0, 2],
              [-1 ,0, 1]]
    # sobel filter col(y) direction
    """    filter_ =[[-1 ,-2, -1],
               [0 , 0, 0],
               [1 , 2, 1]]
    """
    new_img = np.zeros(img.shape)
    R, C = new_img.shape
    D = 1
    for i in xrange(R):
        for j in xrange(C):
             start = (i-D,j-D)
             end =  (i+D,j+D)
             if i-D<0 or j-D<0 or i+D>R-1 or j+D >C-1:
                 continue 
             crop_img=crop(start, end, img)
             for ii in xrange(3):
                 for jj in xrange(3):
                     new_img[i,j] +=crop_img[ii,jj]*filter_[ii][jj] 
    return new_img



def mean_filter(filter_size, img):
    new_img = np.zeros(img.shape)
    R, C = new_img.shape
    print type(R), type(C)
    D = filter_size/2
    for i in xrange(R):
        for j in xrange(C):    
             start = (i-D,j-D)
             end =  (i+D,j+D)
             if i-D<0 or j-D<0 or i+D>R-1 or j+D >C-1:
                 continue 
             crop_img=crop(start, end, img)
             new_img[i,j] = np.average(crop_img)
    return new_img
#file_name = "lena_gray.bmp"
file_name ="zelda2.bmp"
img = mpimg.imread(file_name)
#img = np.zeros((200,200))
#tem_img = np.ones((100,200))
#img[:100,:] = tem_img
plt.figure()
plt.imshow(img, cmap='gray', aspect='auto')
plt.show()
filter_size = 3

#new_img = mean_filter(filter_size,img)
new_img = mean_filter_new(img)
plt.figure()
plt.imshow(new_img, cmap='gray', aspect='auto')
plt.title("image after new mean filter with size of "+str(filter_size))
plt.show()



start =(100,100)
end =(300,300)
croped_image = crop(start, end, img)
print croped_image
show_img(croped_image)


croped_image = crop((100,100), (110,110), img)
print croped_image
show_img(croped_image)


