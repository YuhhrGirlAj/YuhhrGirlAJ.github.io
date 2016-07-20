from PIL import Image

# im=Image.open("emoji.png")

# data=im.getdata()
# data_list=list(data)
# print(      data_list)				

# x=spectrum+print(elem)


# def colors(r,g,b):
    # red(r)
    # green(g)
    # blue(b)
    # return(colors)

# colors(x)
# spectrum=[tuples]
# for elem in spectrum:
    # print(elem)
	
	
	
darkblue=(0,51,76)
red=(217,26,33)
lightblue=(112,150,158)
yellow=(252,227,166)
white=(255,255,255)

im=Image.open("dragon.jpg")
data=im.getdata()
data_list=list(data)
#print(data_list)

list=[]	


for data in data_list:
    r=data[0]
    g=data[1]
    b=data[2]
    x=r+g+b
    if x<=182:
	    color=darkblue
    if 182<x<=364:
        color=red
    if 364<x<=546:
        color=lightblue
    if x>546:
        color=yellow
    list.append(color)
	
im.putdata(list)
im.show()
	