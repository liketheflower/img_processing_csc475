import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def crop(start, end, origin_image):
    return origin_image[start[0]:end[0],start[1]:end[1]]

def show_img(img):
    plt.figure()
    plt.imshow(img, cmap='gray', aspect='auto')
    plt.show()

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
#img = mpimg.imread(file_name)
img = np.zeros((100,100))
img = np.random.randint(256,size = (100,100))
#img[:,:40] = 255
#img[:,60:] = 255
print img[40,:]
plt.figure()
plt.imshow(img, cmap='gray', aspect='auto')
plt.show()
plt.close()
x = [i for i in xrange(100)]
plt.plot(x,img[40,:])
y = img[40,:]
y_derivate = [y[i]-y[i-1] for i in xrange(1,100)]

plt.show()
plt.close()
plt.plot(x[:-1],y_derivate)
plt.show()
plt.close()
filter_size = 17
new_img = mean_filter(filter_size,img)

plt.figure()
plt.imshow(new_img, cmap='gray', aspect='auto')
plt.title("image after mean filter with size of "+str(filter_size))
plt.show()



start =(100,100)
end =(300,300)
croped_image = crop(start, end, img)
print croped_image
show_img(croped_image)


croped_image = crop((100,100), (110,110), img)
print croped_image
show_img(croped_image)


