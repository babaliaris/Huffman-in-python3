import struct

class Node:

    '''This class is been used as a node to construct a linked list and
       the huffman tree. In the linked list, the attribute left is the next
       node, while the right is always None.'''

    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#
    def __init__(self, value = 1, text = "\0"):
        '''Constructor of Node class.'''

        #_____Class Variables_____#
        self.value = value
        self.text  = text
        self.left  = None
        self.right = None
        #_____Class Variables_____#
        
    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#





    #======================Link Left======================#
    def linkLeft(self, new_node):
        '''Link this node's left child.'''
        self.left = new_node
    #======================Link Left======================#





    #======================Link Left======================#
    def linkRight(self, new_node):
        '''Link this node's right child.'''
        self.right = new_node
    #======================Link Left======================#





    #========================Count========================#
    def count(self):
        '''Increase the value by one.'''
        self.value += 1
    #========================Count========================#





    #=======================Is Leaf=======================#
    def isLeaf(self):
        '''Return's True if this node has no children.'''
        return self.left == None and self.right == None
    #=======================Is Leaf=======================#





    #========================Write========================#
    def write(self, filename, page, left, right):
        '''Write's this node into a file:

           1 byte for the character.
           1 byte for the left child.
           1 byte for the right child.

           With only 1 byte i can represent 2**8 - 1 = 255.
           So i can only have maximum of 255 disk pages (nodes)
           inside my tree structure. This is enough for ascii code chars
           because it has 96 characters which means the huffman tree
           needs 96 + 96-1 = 191 nodes exactly. This is how i create the
           huffman structure with the minimum cost in bytes. But of course
           this algorithm will not work for any language which the alhpabet
           plus the extra keyboard symbols are more than 128 because
           128 - 127 = 255.'''

        #Open the file.
        file = open(filename, 'rb+')

        #Seek into the file.
        file.seek(page * 3)

        #Write one byte for the character.
        file.write( str.encode(self.text) )

        #Write one byte for the left child.
        file.write( struct.pack("i", left)[0:1] )

        #Write one byte for the right child.
        file.write( struct.pack("i", right)[0:1] )

        #Close the file.
        file.close()
    #========================Write========================#





    #========================Reasd========================#
    def read(self, filename, page):
        '''Read's a node from the file.'''

        #Open the file.
        file = open(filename, 'rb')

        #Seek into the file.
        file.seek(page * 3)

        #Get text.
        self.text = bytes.decode(file.read(1))

        #Get left.
        b    = file.read(1) + struct.pack("i", 0)[0:3]
        left = struct.unpack("i", b)[0]

        #Get right.
        b     = file.read(1) + struct.pack("i", 0)[0:3]
        right = struct.unpack("i", b)[0]

        return left, right
    #========================Reasd========================#
        

        


    #========================Clone========================#
    def clone(self):
        '''Return's a clone of this node.'''

        #Create a new node.
        new_node = Node(value = self.value, text = self.text)

        #Adjust children.
        new_node.left  = self.left
        new_node.right = self.right

        return new_node
    #========================Clone========================#





    #========================Print========================#
    def print(self):
        '''Just for debugging.'''
        
        print("Value\t\t:",self.value)
        print("Text\t\t:",self.text)
        print("Left Child\t:",self.left != None)
        print("Right Child\t:",self.right != None)
        print("Is Leaf\t\t:",self.isLeaf())
    #========================Print========================#
