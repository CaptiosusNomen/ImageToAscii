from PIL import Image
import os
import sys

class ImageToAscii:
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

    def StandAloneOptions(self):
        self.Imported=False
        import tkinter as tk
        from tkinter import filedialog
        Window = tk.Tk()
        Window.withdraw()
        print('Please press select a .jpg image.')
        self.ImageChoice= filedialog.askopenfilename(
                                          initialdir=self.FilePath,
                                          title='Select Image',
                                          filetypes=[("Image Files",".jpg .png .jpeg .bpg .tif")])
        self.NameChoice=input('Saved under what name?\n')
        print('Please select a directory to save things to.')
        self.DirectoryChoice=filedialog.askdirectory(
                                          initialdir = self.FilePath,
                                          title='Select Directory')
        self.ModeSelect=input('1 for LightMode (Dark Text on a light background) \n2 for Darkmode (Light text on a dark background)\n')
        if self.ModeSelect is '1':
            self.Characters.reverse()
            self.ModeSelect='Light'
        else:
            self.ModeSelect='Dark'
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


    def ProcessImage(self,Ratio):
        ResizedImage = self.RawImage.resize((int(self.RawImage.width//Ratio),int(self.RawImage.height//Ratio)))
        for y in range(ResizedImage.height):
            for x in range(ResizedImage.width):
             #Max750//68 = 0 through 11, the amout of Characters used.
                Brightness = sum(ResizedImage.getpixel((x, y)))//68-1
                if Brightness<=0:
                    Brightness=0
                self.Output += self.Characters[Brightness]
            self.Output += '\n'
        if self.Imported == False:
            self.MRCFile(Ratio)
            self.Output=''
        elif self.Imported == True:
            self.PayloadPacker()
            self.Output=''

        #Make Record Close, Make the file, Record to it, Close the file.
    def MRCFile(self,Ratio):
        if sys.platform == "linux" or sys.platform == "linux2":
            with open(f"{self.DirectoryChoice}/{self.NameChoice}_{Ratio}_{self.ModeSelect}.txt","w") as NewFile:
                openfile=NewFile 
                print(self.Output,file=openfile)
                print('\n\nRatio Level:{}'.format(str(Ratio)))
                print(self.Output)

        elif sys.platform == "win32" or sys.platform == "win64":
            with open(f"{self.DirectoryChoice}\\{self.NameChoice}_{Ratio}_{self.ModeSelect}.txt","w") as NewFile:
                openfile=NewFile 
                print(self.Output,file=openfile)
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
    ImageToAscii().StandAloneOptions()
else:
    pass

