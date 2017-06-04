class Scanner:

    '''This class is letting you to scan all the characters of a text
       file.'''

    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#
    def __init__(self, filename):
        '''Constructor of Scanner class.'''

        #_____Class Variables_____#
        self.error      = ""
        self.eof        = None
        self.file       = None
        self.bufferSize = 1024 * 1024
        #_____Class Variables_____#

        #Try to open the file.
        try:
            self.file = open(filename, 'r')

        #FileNotFoundError.
        except FileNotFoundError:
            self.error = 'Scanner Error: File: "'+filename+'", '+\
                         'could not been found.'
            return

        #PermissionError.
        except PermissionError:
            self.error = 'Scanner Error: File: "'+filename+'", '+\
                         'is not permitted to be accessed.'
            return
    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#





    #=========================Next========================#
    def next(self):
        '''Return's a list of characters with the size of bufferSize.'''

        #Buffer.
        buffer = self.file.read(self.bufferSize)

        #End Of File Reached.
        if buffer == "":
            self.eof = ""
            return []

        #Return the buffer.
        return buffer
            
    #=========================Next========================#





    #=======================Has Next======================#
    def hasNext(self):
        '''Return's True if the End Of File was
           not reached'''
        return self.eof != ""
    #=======================Has Next======================#





    #========================Close========================#
    def close(self):
        '''Closing the file.'''
        self.file.close()
    #========================Close========================#
