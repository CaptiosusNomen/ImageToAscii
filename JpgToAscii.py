from PIL import Image
import os
class JpgToAscii:
    def __init__(self,Image='',Mode=''):    
        self.Characters = [' ','.',',','~','+','*','=','%','$','&','#']
        self.Output=''
        self.FilePath= os.path.dirname(os.path.abspath(__file__))
        self.Payload=[]
        self.ImageChoice=Image
        self.ModeSelect=Mode
        self.Imported=True
        if self.ModeSelect.lower() is 'light':
            self.Characters.reverse()

        #for when it's run by itself. 
    def StandAloneOptions(self):
        self.Imported=False
        import tkinter as tk
        from tkinter import filedialog
        Window = tk.Tk()
        Window.withdraw()
        print('Please press select a .jpg image.')
        self.ImageChoice= filedialog.askopenfilename(
                          initialdir='/Desktop',
                          title='Select Image',
                          filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        self.NameChoice=input('Saved under what name?')
        print('Please select a directory to save things to.')
        self.DirectoryChoice=filedialog.askdirectory(
                          initialdir = 'home/user/Desktop',
                          title='Select Directory')
        print('1 for LightMode (Dark Text on a light background)')
        self.ModeSelect=input('2 for Darkmode (Light text on a dark background)\n')
        if self.ModeSelect is '1':
            self.Characters.reverse()
            self.ModeSelect='light'
        else:
            self.ModeSelect='dark'
        self.RawImage = Image.open(self.ImageChoice)
        self.Ratio()

    def FullList(self):
        self.Ratio()

    def Ratio(self):
        if self.Imported is True:
            self.RawImage = self.ImageChoice
        for Ratio in range(21):
            if Ratio is not 0:
                self.ProcessImage(Ratio)

        #turns pixels into something on the self.Characters list
    def ProcessImage(self,Ratio):
        ResizedImage = self.RawImage.resize((int(self.RawImage.width//Ratio),int(self.RawImage.height//Ratio)))
        for y in range(ResizedImage.height):
            for x in range(ResizedImage.width):
             #Max750//68 = 0 through 11, the amout of Characters used.
                Brightness = sum(ResizedImage.getpixel((x, y)))//68
                #Because arrays
                Brightness-=1
                if Brightness<=0:
                    Brightness=0
                self.Output += self.Characters[Brightness]
            self.Output += '\n'
        if self.Imported is False:
            self.MRCFile(Ratio)
            self.Output=''
        elif self.Imported is True:
            self.PayloadPacker()
            self.Output=''

        #Make Record Close, Make the file, Record to it, Close the file.
    def MRCFile(self,Ratio):
        openfile=open("{0}/{1}:{2}:{3}.txt".format(self.DirectoryChoice,self.NameChoice,Ratio,self.ModeSelect),"w") 
        print(self.Output,file=openfile)
        openfile.close()
        print('\n\nRatio Level:{}'.format(str(Ratio)))
        print(self.Output)

    def PayloadPacker(self):
        self.Payload.append(self.Output)
        print(len(self.Payload))
        print(type(len(self.Payload)))
        if len(self.Payload) == 20:
            print('return self.Payload')
            return self.Payload

    def __iter__(self):
        return iter(self.Payload)

if __name__ == "__main__":
    JpgToAscii().StandAloneOptions()
else:
    pass
