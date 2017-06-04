from source_files.scanner import Scanner
from source_files.node    import Node

class Alphabet:

    '''This class is a linked list which is been constructed
       by the characters of the input file. The size of the list
       depends on the number of the different symbols that are inside
       the file.'''

    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#
    def __init__(self, filename):
        '''Constructor of Alphabet class.'''

        #_____Class Variables_____#
        self.error    = ""
        self.head     = None
        self.size     = 0
        self.scanner  = Scanner(filename)
        #_____Class Variables_____#

        #Error occured on the scanner.
        if self.scanner.error != "":
            self.error = self.scanner.error
            return


        #Create the alphabet.
        self.create()
    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#





    #========================Create=======================#
    def create(self):
        '''Create's the alphabet which is a linked list.'''

        while self.scanner.hasNext():

            #-----Go Though All Characters-----#
            
            for ch in self.scanner.next():

                #First node.
                if self.head == None:
                    self.head = Node(text = ch)
                    self.size += 1
                    pass

                #Other node.
                else:

                    #Start from the head.
                    current = self.head

                    while current != None:

                        #Ch exists in the alphabet.
                        if current.text == ch:
                            current.count()
                            break

                        #Append ch in the aplhabet.
                        if current.left == None:
                            current.linkLeft( Node(text = ch) )
                            self.size += 1
                            break

                        #Go to next node.
                        current = current.left
                        
            #-----Go Though All Characters-----#


        #Close the scanner after done.
        self.scanner.close()
    #========================Create=======================#





    #==========================Pop========================#
    def pop(self):
        '''Return's and remove's the head of the list.'''

        #Reduce the size of the list.
        if self.head != None:
            self.size -= 1

        #Keep the head node.
        temp = self.head

        #Last pop.
        if self.head.left == None:
            self.head = None      #Empty list.
            return temp           #Return the node.


        #Update the head.
        self.head = self.head.left

        #Clear the left child.
        temp.linkLeft(None)
        
        return temp
    #==========================Pop========================#





    #========================Is Empty=====================#
    def isEmpty(self):
        '''Return's True if the alphabet is empty.'''
        return self.head == None
    #========================Is Empty=====================#
        
        
