import numpy as np
from PIL import Image, ImageFilter
#Read image
file_name =  "csi.jpg"
im = Image.open( file_name )
#Display image
im.show()
im_new = np.asarray(im)
print "first pixel of the original img", im_new[0,0,:]
print "original image shape: ", im_new.shape

print type(im_new)
r,g,b = im.split()
print r
r_new = np.asarray(r)
r_new_new = np.zeros((900,1200,3))
for i in xrange(900):
    for j in xrange(1200):
        r_new_new[i,j,0] = r_new[i,j]
img_red = Image.fromarray(r_new_new, 'RGB')
img_red.show()
g_new = np.asarray(g)
b_new = np.asarray(b)
print "red chanel shape: ", r_new.shape
print "first pixel of the red channel", r_new[0,0]
print "first pixel of the green channel", g_new[0,0]
print "first pixel of the blue channel", b_new[0,0]
r.show()
g.show()
b.show()
