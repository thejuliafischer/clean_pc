import os, shutil

lis=[]

i=1

destinationdir='/Users/NAME/Desktop/Everything'

while os.path.exists(destinationdir):

    destinationdir+=str(i)

    i+=1

os.makedirs(destinationdir)


lis=os.listdir('/Users/NAME/Desktop')

for x in lis:

    print x

    if x==__file__:

        continue

    shutil.move(x,destinationdir)
