import matplotlib.pyplot as plt

img = [[0,0,0,0,0] for _ in xrange(6)]
img[2][2]=1
img[3][1]=1
img[3][2]=1
img[4][1]=1
img[4][2]=1
img[4][3]=1

print img
plt.imshow(img, cmap='gray', aspect='auto')
plt.show()

def dfs(i,j,img, label =2):
    R, C = len(img), len(img[0])
    open_list, close_list =[],[]
    open_list.append((i,j))
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    while open_list:
        print "open,close",open_list, close_list
        node = open_list.pop()
        ii,jj = node
        print "popped node", node
        img[ii][jj] = label
        close_list.append(node)
        for di,dj in directions:
            if 0<=ii+di<R and 0<=jj+dj<C and img[ii+di][jj+dj]==1 and (ii+di,jj+dj) not in open_list and (ii+di,jj+dj) not in close_list:
                open_list.append((ii+di,jj+dj))
    return img
            

R, C = len(img), len(img[0])
for i in xrange(R):
    for j in xrange(C):
        if img[i][j] == 1:
            img = dfs(i,j,img)

print "img after dfs",img
