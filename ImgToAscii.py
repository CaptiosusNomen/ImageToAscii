from PIL import Image
import os

Characters = ['·','.','*','$','#']
Output= ''
FilePath = os.path.dirname(os.path.abspath(__file__))
for files in os.listdir('{}/Images'.format(FilePath)):
    print(files)

Choose=input('\nWhat is the name of the image you want me to convert? Please include the file extenton\n ')
Ratio=input('What ratio do you want to ascii img to be made at?\n1 for no change.     2 for half size.\n3 for one third.     4 for one forth etc...\n')
Ratio=int(Ratio)


ImageUsed = Image.open('{0}/Images/{1}'.format(FilePath,Choose))
ImageUsed = ImageUsed.resize((int(ImageUsed.width//Ratio),int(ImageUsed.height//Ratio)))

for y in range(ImageUsed.height):
    for x in range(ImageUsed.width):
     #Max750//150 = 0 through 5, the amout of Characters used.
        brightness = sum(ImageUsed.getpixel((x, y)))//150
        brightness-=1
        if brightness<=0:
            brightness=0
        Output += Characters[brightness]
    Output += '\n'


openfile=open("{0}/AsciiArt/{1}:{2}.txt".format(FilePath,Choose,Ratio),"w") 
print(Output,file=openfile)
openfile.close()
