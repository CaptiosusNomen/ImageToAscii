from PIL import Image
import os
class I2A:
    def __init__(self):    
        self.Characters = [' ','.',',','~','*','+','=','%','$','&','#']
        self.Output= ''
        self.FilePath = os.path.dirname(os.path.abspath(__file__))

        self.Options()

    def Options(self):
        for files in os.listdir('{}/Images'.format(self.FilePath)):
            print(files)
        self.ImageChoice=input("\nWhat is the name of the image you want me to convert?\n Mind you, I'm picky and only like .jpg\n")
        ModeSelect=input('1 for LightMode(Dark Text on a light background)\n2 for Darkmode(Light text on a dark background)\n')
        if ModeSelect is '1':
            self.Characters.reverse()
        self.RawImage = Image.open('{0}/Images/{1}.jpg'.format(self.FilePath,self.ImageChoice))
        self.RatioRange()

    def RatioRange(self):
        for Ratio in range(10):
            if Ratio is not 0:
                self.ProcessImage(Ratio)

    def ProcessImage(self,Ratio):
        ResizedImage = self.RawImage.resize((int(self.RawImage.width//Ratio),int(self.RawImage.height//Ratio)))
        for y in range(ResizedImage.height):
            for x in range(ResizedImage.width):
             #Max750//75 = 0 through 10, the amout of Characters used.
                Brightness = sum(ResizedImage.getpixel((x, y)))//68
                Brightness-=1
                if Brightness<=0:
                    Brightness=0
                self.Output += self.Characters[Brightness]
            self.Output += '\n'
        self.MRCFile(Ratio)
        self.Output=''
    def MRCFile(self,Ratio):
        openfile=open("{0}/AsciiArt/{1}:{2}.txt".format(self.FilePath,self.ImageChoice,Ratio),"w") 
        print(self.Output,file=openfile)
        openfile.close()
        print('\n\nRatio Level:{}'.format(str(Ratio)))
        print(self.Output)
I2A()
