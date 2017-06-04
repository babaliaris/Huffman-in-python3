from source_files.priority_queue import PriorityQueue
from source_files.alphabet  import Alphabet
from source_files.scanner import Scanner
from source_files.node  import Node
import struct, os



class Coder:

    '''This class supports the following operations:

       1) Create the huffman tree from a file.
       2) After the huffman creation, create the compressed file.
       3) Load a compressed file and decompressed it.'''

    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#
    def __init__(self):

        #_____Class Variables_____#
        self.error     = ""

        self.huffman   = None

        self.code      = []

        self.all_codes = {}
        #_____Class Variables_____#
    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#





    #===================Create Huffman====================#
    def __createHuffman__(self, filename):
        '''Create's the huffman tree from the alphabet.'''

        #Create the alphabet.
        alphabet = Alphabet(filename)

        #An error occured.
        if alphabet.error != "":
            self.error = alphabet.error
            return

        #Create a new priority queue object.
        queue = PriorityQueue(alphabet.size)

        #Fill the queue with the alphabet.
        while not alphabet.isEmpty():
            queue.insert( alphabet.pop() )
            pass

        #Create the huffman tree.
        while queue.size > 1:

            #Pop two nodes from the queue.
            node1 = queue.pop()
            node2 = queue.pop()

            #Create a new node.
            new_node = Node(value = node1.value + node2.value)

            #Make the links.
            new_node.linkLeft(node1)
            new_node.linkRight(node2)

            #Insert the new node into the queue.
            queue.insert(new_node)
            pass

        #Get the huffman tree root.
        self.huffman = queue.pop()

        

        #Create huffman codes.
        self.__createCodes__(self.huffman)



        #Create the file for the tree.
        file = open(filename.replace(".txt", ".htree"), 'wb')
        file.close()
        
        #Write the tree into a file.
        self.__writeTree__( self.huffman, filename.replace(".txt", ".htree") )
    #===================Create Huffman====================#





    #====================Create Codes=====================#
    def __createCodes__(self, root):
        '''Here i create the huffman codes where i store them inside
           a dictionary. I use preorder traversal to succeed this.'''

        #Return statement.
        if root == None:
            self.code = self.code[:len(self.code) - 1]
            return


        #Root is a leaf.
        elif root.isLeaf():
            self.all_codes[root.text] = self.code.copy()
            pass

        #Go left.
        self.code.append(0)
        self.__createCodes__(root.left)

        #Go right.
        self.code.append(1)
        self.__createCodes__(root.right)

        if len(self.code)-1 > -1:
            self.code = self.code[:len(self.code) - 1]
    #====================Create Codes=====================#





    #=====================Write Tree======================#
    def __writeTree__(self, root, filename):
        '''Write the huffman tree inside a file using preorder traversal.'''

        #Return statement.
        if root == None:
            return

        #Calculate the amount of pages inside the file.
        lastPage = os.path.getsize(filename) // 3

        #Root has a left child.
        if root.left != None:
            root.write(filename, lastPage, lastPage+1, 255)
            pass

        #Root do not have a left child.
        else:
            root.write(filename, lastPage, 255, 255)
            pass


        #Go to the left subtree.
        self.__writeTree__(root.left, filename)


        #Connect the right child.
        if root.right != None:

            #Calculate the update file pages.
            new_last_page = os.path.getsize(filename) // 3

            #Update the node.
            root.write(filename, lastPage, lastPage+1, new_last_page)
            pass

        #Go to the right subtree.
        self.__writeTree__(root.right, filename)
    #=====================Write Tree======================#





    #=====================Read Tree=======================#
    def __readTree__(self, root, filename):
        '''Read huffman tree from a file.'''

        #Return statement.
        if root == 255:
            return None

        #Create a new node.
        new_node = Node()

        #Read the current root.
        left, right = new_node.read(filename, root)

        #Move left.
        new_node.linkLeft ( self.__readTree__(left, filename) )

        #Move right.
        new_node.linkRight ( self.__readTree__(right, filename) )

        return new_node
    #=====================Read Tree=======================#





    #=====================Join Files======================#
    def __joinFiles__(self, filename):


        #Get the size of the huffman tree file.
        header = os.path.getsize(filename.replace(".txt", ".htree"))

        #Create the final file.
        final_file = open(filename.replace(".txt", ".huffman"), "wb")

        #Open the huffman tree file.
        huffman    = open(filename.replace(".txt", ".htree"), "rb")

        #Open the compressed file.
        compressed = open(filename.replace(".txt", ".huff"), "rb")


        #Write the header with only two bytes.
        final_file.write( struct.pack('i', header)[0:2] )
        

        #Copy huffman tree into the final file.
        final_file.write( huffman.read() )
        huffman.close()


        #Read 1mb of data.
        buffer = compressed.read(1024*1024)
        #-----Copy Compressed File Inside The Final File-----#
        while len(buffer) > 0:

            #Write the buffer to the final file.
            final_file.write(buffer)

            #Read next data.
            buffer = compressed.read(1024*1024)
            pass

        #Close compressed file.
        compressed.close()
        #-----Copy Compressed File Inside The Final File-----#

        #Remove the htree file.
        os.remove(filename.replace(".txt", ".htree"))

        #Remove the huff file.
        os.remove(filename.replace(".txt", ".huff"))

        #Close final file.
        final_file.close()
    #=====================Join Files======================#





    #====================Split Files======================#
    def __splitFiles__(self, filename):

        #Open input file.
        final_file = open(filename, "rb")

        #Create huffman tree file.
        huffman    = open(filename.replace(".huffman", '.htree'), 'wb')

        #Create compressed file.
        compressed = open(filename.replace(".huffman", '.huff'), 'wb')

        #Get the header.
        header = final_file.read(2) + struct.pack("i", 0)[0:2]
        header = struct.unpack("i", header)[0]

        #Create the huffman tree file.
        huffman.write( final_file.read(header) )
        huffman.close()

        #Read 1mb of data.
        buffer = final_file.read(1024*1024)

        #-----Create The Compressed File-----#
        while len(buffer) > 0:

            #Write the buffer.
            compressed.write(buffer)

            #Get next bytes.
            buffer = final_file.read(1024*1024)

        #Close the file.
        compressed.close()
        #-----Create The Compressed File-----#
    #====================Split Files======================#

        



    #======================Compress=======================#
    def compress(self, filename):
        '''Create the compressed file with all the bits.'''

        #Create the huffman tree.
        self.__createHuffman__(filename)

        #Create a scanner.
        scanner = Scanner(filename)

        #Error ocurred.
        if scanner.error != "":
            self.error = scanner.error
            return

        #Create the compressed file.
        file = open(filename.replace('.txt', '.huff'), 'wb')
        file.close()
        file = open(filename.replace('.txt', '.huff'), 'rb+')

        #Header for useless bytes.
        file.write( struct.pack("i", 0)[0:1] )

        #Some variables.
        number  = 0
        counter = 0

        #-------------Create The Compressed File-------------#
        while scanner.hasNext():

            #Get next characters from the file.
            for ch in scanner.next():

                #Go through all bits of current character's code.
                for bit in self.all_codes[ch]:

                    #Check.
                    if counter == 8:

                        #Get the first byte from the integer.
                        byte = struct.pack("i", number)[0:1]

                        #Write it.
                        file.write(byte)

                        #Reset.
                        number  = 0
                        counter = 0
                        pass

                    #Put the bit inside the 4 bytes of a number.
                    mask   = bit
                    mask   = mask << counter
                    number = number | mask

                    #Encrease the counter.
                    counter += 1


        #Last Check.
        if counter <= 8:
            
            #Get the first byte from the integer.
            byte = struct.pack("i", number)[0:1]

            #Write it.
            file.write(byte)
        #-------------Create The Compressed File-------------#

        #Seek at the top of the file.
        file.seek(0)

        #Write the useless amount of bytes in the header.
        file.write( struct.pack("i", 8 - counter)[0:1] )

        #Close the file.
        file.close()

        #Close scanner.
        scanner.close()

        #Join the huffman tree file and the compressed file
        #in one file.
        self.__joinFiles__(filename)
    #======================Compress=======================#





    #=====================Decompress======================#
    def decompress(self, filename, outname):
        '''Decompress a compressed file.'''


        #Split the file.
        self.__splitFiles__(filename)

        #Create the filenames.
        filename = [filename.replace(".huffman", '.huff'), filename.replace(".huffman", '.htree')]

        #Read the huffman tree from the file.
        self.huffman = self.__readTree__(0, filename[1])

        #Create the codes.
        self.__createCodes__(self.huffman)

        #Open the file.
        read_file = open(filename[0], "rb")

        #Create write file.
        write_file = open(outname, "w")

        #Read the amount of usless bytes.
        useless = read_file.read(1) + struct.pack("i", 0)[0:3]
        useless = struct.unpack("i", useless)[0]

        #Just a variable.
        mask = 1

        #Just a node object.
        node = self.huffman

        #Write buffer.
        write_buffer = ""

        for i in range( 1, os.path.getsize(filename[0]), 1024*1024):

            #Read 1 mb of data.
            buffer = read_file.read(1024*1024)

            while len(buffer) > 0:

                #Regular loop.
                loop = 8

                #Only for the last byte of the file.
                if i+1024*1024 >= os.path.getsize(filename[0]):
                    if len(buffer) == 1:
                        loop = 8 - useless + 1
                    

                #Get the next byte.
                byte = buffer[0:1]

                #Decrease the buffer by one byte.
                buffer = buffer[1:]

                #Create a 4 bytes number from the byte.
                number = byte + struct.pack("i", 0)[0:3]
                number = struct.unpack("i", number)[0]

                for i in range(loop):

                    #Destination reached!
                    if node.isLeaf():
                        write_buffer += node.text
                        node = self.huffman
                    
                    #Get the first 8 bits from this number.
                    if number != 0:

                        #Get the next bit.
                        bit = number & mask

                        #Go left.
                        if bit == 0:
                            node = node.left

                        #Go right.
                        else:
                            node = node.right

                        #Decrease this number
                        number = number >> 1


                    #Go only left.
                    else:
                        node = node.left


            #Write the write_buffer.
            write_file.write(write_buffer)
            write_buffer = ""


        #Close the files.
        read_file.close()
        write_file.close()

        #Remove the htree file.
        os.remove(filename[1])

        #Remove the huff file.
        os.remove(filename[0])
    #=====================Decompress======================#
