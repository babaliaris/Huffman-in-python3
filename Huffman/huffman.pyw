import os, sys
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from source_files.coder import Coder


'''This is the user interface.'''


class Application:

    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#
    def __init__(self, resolution, title):

        #--------Initialize TK--------#
        self.screen = Tk()
        self.screen.title(title)
        self.screen.resizable(0,0)
        #--------Initialize TK--------#

        #Current activate widgets.
        self.widgets = []

        #Check for permission.
        try:
            file = open("test", "w")
            file.close()
            os.remove("test")
            pass

        #Failed.
        except PermissionError:
            messagebox.showerror("Permission Denied!", "Please run the programm as administrator or move it in another directory which no requires admin privilege.")
            sys.exit()
            
        return
    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#





    #=======================Clear=========================#
    def clear(self):

        #Destroy all widgets.
        for widget in self.widgets:
            widget.destroy()
    #=======================Clear=========================#



    #=======================Start========================#
    def start(self):

        #Start main menu.
        self.mainMenu()

        #Screen loop.
        self.screen.mainloop()
        return
    #=======================Start========================#
    



    #=====================Main Menu======================#
    def mainMenu(self):

        #Clear current widgets.
        self.clear()
        
        #Widgets.
        compressButton   = Button(text = "Compress", width = 25, command = self.compressMenu)
        decompressButton = Button(text = "Decompress", width = 25, command = self.decompressMenu)
        exitButton       = Button(text = "Exit", width = 25, command = self.quit)

        #Griding them.
        compressButton.grid(row=0,column=0)
        decompressButton.grid(row=1,column=0)
        exitButton.grid(row=2,column=0)

        #Update current widgets.
        self.widgets = [compressButton, decompressButton, exitButton]
    #=====================Main Menu======================#




    #===================Compress Menu====================#
    def compressMenu(self):

        #Clear current widgets.
        self.clear()

        #Update current widgets.
        self.widgets = [Label(text = "Choosing File...", width = 25, fg = "red")]
        self.widgets[0].grid(row=0,column=0)

        #Ask open for file.
        filename = filedialog.askopenfilename(initialdir = os.getcwd(), filetypes = (("Text files", "*.txt")
                                                         ,("", "") ))

        #Open file canceled.
        if filename == "":
            self.mainMenu()
            return

        #Clear current widgets.
        self.clear()

        #Update current widgets.
        self.widgets = [Label(text = "Compressing, please wait...", fg = "red", width = 25)]
        self.widgets[0].grid(row=0,column=0)

        #Create a coder.
        coder = Coder()

        #Show message before compression.
        messagebox.showinfo("Info", "The compression is about to begin, this will take a while.\n\nPress OK to continue...")

        
        #Compress.
        coder.compress(filename)

        #Get sizes.
        original_size   = os.path.getsize(filename)
        compressed_size = os.path.getsize(filename.replace(".txt", ".huffman"))

        #Calculate percentage.
        percentage = int ( (original_size - compressed_size) / original_size * 100 )

        #Create info message.
        message = "The compression finished successfully!\n\nOrigina Size\t: "+str(original_size)+" bytes.\n"+\
                  "Compressed Size\t: "+str(compressed_size)+" bytes\n"+"Percentage\t: "+str(percentage)+"%"+\
                  "\n\nFile create at:\n\t"+os.path.join(os.getcwd(), filename.replace(".txt", ".huffman") )
        
        #Show success message.
        messagebox.showinfo("Compression Finished!", message)

        #Go back to main menu.
        self.mainMenu()
        return
    #===================Compress Menu====================#




    #==================Decompress Menu===================#
    def decompressMenu(self):
        

        #-------------------Start Decompression-------------------#
        def startDecompression():

            

            #Unwanted Symbols.
            unwantedSymbols = ['\n', '!', '@', '#', '$', '%','^',
                                '&', '*', '(', ')', '-', '_', '+',
                                '=', '\\', '|', '[', ']', '{', '}',
                                ';', ':', '"', ',', '<',
                                '>', '/', '?', '\t', "'"]


            #Get the name and check it.
            name = outname.get()

            #Name is empty.
            if name == "":
                messagebox.showerror("Invalid Name", "You have not enter a name.")
                return

            #Check for unwanted symbols.
            for symbol in unwantedSymbols:

                #Unwanted symbols found.
                if symbol in  name:
                    messagebox.showerror("Invalid Name", 'The character: '+symbol+'  is not permitted. Please choose another name.')
                    return


            #Clear current widgets.
            self.clear()

            #Update current widgets.
            self.widgets = [Label(text = "Choosing File...", fg = "red", width = 25)]
            self.widgets[0].grid(row=0,column=0)


            #Ask open for file.
            filename = filedialog.askopenfilename(initialdir = os.getcwd(), filetypes = (("Huffman files", "*.huffman")
                                                         ,("", "") ))


            #Process canceled.
            if filename == "":
                return

            #Update current widgets.
            self.clear()
            self.widgets = [Label(text = "Decompressing, please wait...", fg = "red", width = 25)]
            self.widgets[0].grid(row=0,column=0)


            #Create a coder object.
            coder = Coder()

            #Decompression message starting info.
            messagebox.showinfo("Info", "The decompression is about to begin, this will take a while.\n\nPress OK to continue...")
            
            #Start decompression.
            coder.decompress(filename, name+".txt")


            #Finish info.
            message = "The decompression finished successfully!\n\nFile created at:\n\t"+\
                      os.path.join(os.getcwd(), name+".txt")


            #Decompression message ended info.
            messagebox.showinfo("Decompression Finsihed!", message)

            #Go back to main menu.
            self.mainMenu()
            pass
        #-------------------Start Decompression-------------------#

            

        #Clear current widgets.
        self.clear()

        #Just a String Var object.
        outname = StringVar()

        #Label.
        label = Label(text = "Output name: ")

        space = Label(text = "")
        
        #Entry.
        entry = Entry(textvariable = outname)

        #Start button.
        startButton = Button(text = "Start", width = 25, command = startDecompression)

        #Back button.
        backButton  = Button(text = "Back", width = 25, command = self.mainMenu)


        #Grid all widgets.
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        space.grid(row=1, column=0, columnspan = 2)
        startButton.grid(row=2, column=0,columnspan = 2)
        backButton.grid(row=3, column=0, columnspan = 2)

        #Update current widgets.
        self.widgets = [label, space, entry, startButton, backButton]
        return
    #==================Decompress Menu===================#



    #========================Quit========================#
    def quit(self):
        self.screen.destroy()
    #========================Quit========================#
        
 
        


#Start the app.
if __name__ == "__main__":
    app = Application("400x400", "Huffman")
    app.start()
