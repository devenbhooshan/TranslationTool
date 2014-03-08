
import csv  # for CSV files 
import goslate # Free Google Translate API http://pythonhosted.org/goslate/
import Tkinter as tk # For GUI
from tkFileDialog import askopenfilename # For file browser
from unicode import UnicodeWriter # A prebuilt class file . As CSV doenot support unicode
class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # This liss holds the output languages selected by the user
        self.LanguagesStatus = {'Afrikaans':0,'Haitian':0,'Serbian':0,'Albaniaan':0,'Hebrew':0,'Slovak':0,'Arabic':0,'Hindi':0,'Slovenian':0,'Belarusian':0,'Hungarian':0,'Spanish':0,'Bulgarian':0,'Icelandic':0,'Swahili':0,'Catalan':0,'Indonesian':0,'Swedish':0,'Chinese Si':0,'Irish':0,'Thai':0,'Chinese Tr':0,'Italian':0,'Thurkish':0,'Czech':0,'Japanese':0,'Ukrainian':0,'Danish':0,'Korean':0,'Viatnamese':0,'Dutch':0,'Latvian':0,'Welsh':0,'English':0,'Lithuanian':0,'Yiddish':0,'Estonian':0,'Macedonian':0,'Filipino':0,'Maltese':0,'Finnish':0,'Norwegian':0,'French':0,'Polish':0,'Galician':0,'Portuguese':0,'German':0,'Romanian':0,'Greek':0,'Russian':0
        }
        # This list holds the Language Codes used by the google translations API
        self.LanguagesCodes ={'Afrikaans':'af','Haitian':'ht','Serbian':'sr','Albaniaan':'sq','Hebrew':'iw','Slovak':'sk','Arabic':'ar','Hindi':'hi','Slovenian':'sl','Belarusian':'be','Hungarian':'hu','Spanish':'es','Bulgarian':'bg','Icelandic':'is','Swahili':'sw','Catalan':'ca','Indonesian':'id','Swedish':'sv','Chinese Si':'zh','Irish':'ga','Thai':'th','Chinese Tr':'zh','Italian':'it','Thurkish':'tr','Czech':'cs','Japanese':'ja','Ukrainian':'uk','Danish':'da','Korean':'ko','Viatnamese':'vi','Dutch':'nl','Latvian':'lv','Welsh':'cy','English':'en','Lithuanian':'lt','Yiddish':'yi','Estonian':'et','Macedonian':'mk','Filipino':'tl','Maltese':'mt','Finnish':'fi','Norwegian':'no','French':'fr','Polish':'pl','Galician':'gl','Portuguese':'pt','German':'de','Romanian':'ro','Greek':'el','Russian':'ru'
        }

        rowCounter=0;
        index=0;
        for key in self.LanguagesStatus:
            self.LanguagesStatus[key] = tk.IntVar()
            aCheckButton = tk.Checkbutton(self, text=key,
                                            variable=self.LanguagesStatus[key])
            if index%3 == 0:
                aCheckButton.grid(row=rowCounter ,column=1, sticky='W')
            if index%3 == 1:
                aCheckButton.grid(row=rowCounter ,column=2, sticky='W')
            if index%3 == 2:
                aCheckButton.grid(row=rowCounter ,column=3, sticky='W')    
            index=index+1
            if index%3 == 0:
                rowCounter=rowCounter+1        
        submitButton = tk.Button(self, text="Open File",command=self.open_button)
        submitButton.grid(row=rowCounter+1,column=3)

    # Reads the file and returns the firstColumn of CSV file    
    def file_Read(self):
        filename = askopenfilename()
        inputfile  = open(filename, "rb")
        reader = csv.reader(inputfile)
        index=0;
        stringValues=[]
        for row in reader:
            if row:
                stringValues.append(row[0]);
        return stringValues        

    # Writes data to CSV file     
    def file_Write(self,outputList):
        with open('translated.csv', 'wb') as files:
            writer = UnicodeWriter(files,quoting=csv.QUOTE_ALL)
            writer.writerows(outputList)

    # Wrapper Funtion for translate        
    def translate(self):
        gs = goslate.Goslate()
        stringValues=self.file_Read()
        fileoutput=[]
        index=0;
        for row in stringValues:
            fileoutput.append([])
            for key, value in self.LanguagesStatus.items():
                state = value.get()
                if state != 0:
                    fileoutput[index].append(gs.translate(row,self.LanguagesCodes[key]))
            index=index+1
        
        self.file_Write(fileoutput)
    # This function is triggered when the user clicks the select button.     
    def open_button(self):
        self.translate()
        exit()



gui = GUI()
gui.mainloop()