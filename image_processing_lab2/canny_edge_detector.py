import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def crop(start, end, origin_image):
    return origin_image[start[0]:end[0]+1,start[1]:end[1]+1]

def show_img(img):
    plt.figure()
    plt.imshow(img, cmap='gray', aspect='auto')
    plt.show()


def sobel_filter(img, x= True):
    
    # sobel filter row(x) direction
    if x:
        filter_ =[[-1 ,0, 1],
              [-2 ,0, 2],
              [-1 ,0, 1]]
    else:
    # sobel filter col(y) direction
        filter_ =[[-1 ,-2, -1],
               [0 , 0, 0],
               [1 , 2, 1]]
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

def distance(x,y):
    return (x**2+y**2)**0.5


def get_magnitude(x, y):

    new_img = np.zeros(x.shape)
    R, C = new_img.shape
    for i in xrange(R):
        for j in xrange(C):
            new_img[i,j] = distance(x[i,j],y[i,j])
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
file_name = "lena_gray.bmp"
#file_name ="zelda2.bmp"
#file_name = "./../../DM/ID13_YANGJUYING_OD01/Intensity/ID13_YANGJUYING_OD01_0.bmp"
file_name = "clown.bmp"
img = mpimg.imread(file_name)
#img = np.zeros((200,200))
#tem_img = np.ones((100,200))
#img[:100,:] = tem_img
plt.figure()
plt.imshow(img, cmap='gray', aspect='auto')
plt.show()
filter_size = 3

# show the sobel x and sobel y images
new_img_x = sobel_filter(img)
plt.figure()
plt.imshow(new_img_x, cmap='gray', aspect='auto')
plt.title("sobel x ")
plt.show()

new_img_y = sobel_filter(img,False)
plt.figure()
plt.imshow(new_img_y, cmap='gray', aspect='auto')
plt.title("sobel y ")
plt.show()

magnitude_img = get_magnitude(new_img_x, new_img_y)
# show the magnitude
plt.figure()
plt.imshow(magnitude_img, cmap='gray', aspect='auto')
plt.title("magnitude image ")
plt.show()

def get_sharp(img, magnitude_img):
    new_img = np.zeros(img.shape)
    R, C = new_img.shape
    for i in xrange(R):
        for j in xrange(C):
            new_img[i,j] = img[i,j]+magnitude_img[i,j]
    return new_img


sharp_img = get_sharp(img, magnitude_img)
plt.figure()
plt.imshow(sharp_img, cmap='gray', aspect='auto')
plt.title("sharp image ")
plt.show()

start =(100,100)
end =(300,300)
croped_image = crop(start, end, img)
print croped_image
show_img(croped_image)


croped_image = crop((100,100), (110,110), img)
print croped_image
show_img(croped_image)


