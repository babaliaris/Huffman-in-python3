from source_files.node import Node

class PriorityQueue:

    '''This class is a heap priority queue excactly as you know it.
       It's using an array to create a heap tree.'''


    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#
    def __init__(self, size):
        '''Constructor of PriorityQueue class.'''

        #_____Class Variables_____#
        self.array    = []
        self.size     = 0
        self.index    = 0
        #_____Class Variables_____#

        #Create the array.
        for i in range(size):
            self.array.append(None)
    #-_-_-_-_-_-_-_-_-_-_-Constructor-_-_-_-_-_-_-_-_-_-_-#





    #=======================Insert========================#  
    def insert(self, new_node):
        '''Insert a new Node object into the queue.'''

        #Insert the node at the end of the array.
        self.array[self.index] = new_node

        #Shift up to order the queue.
        self.__shiftUp__()

        #Do some adjustments.
        self.index += 1 #Increase the index pointer.
        self.size  += 1 #Increase the size of the queue.
        pass
    #=======================Insert========================#  





    #========================Pop==========================#
    def pop(self):
        '''Pop the root node.'''

        #Clone the root.
        temp = self.array[0].clone()

        #Swap the root with the last node in the array.
        self.__swap__(0, self.index-1)

        #Delete the last node in the array.
        self.array[self.index-1] = None

        #Do some adjustments.
        self.index -= 1 #Decrease the index pointer.
        self.size  -= 1 #Decrease the size of the queue.

        #Shift down the root.
        self.__shiftDown__()

        return temp
    #========================Pop==========================#





    #=====================Is Empty========================#
    def isEmpty(self):
        '''Return's True if the queue is empty.'''
        return self.index == 0
    #=====================Is Empty========================#





    #======================Shift Up=======================# 
    def __shiftUp__(self):
        '''Order the queue by checking the added with its parent
           until you reach the root or a swap failure.'''

        #Current index.
        current = self.index

        #Parent index.
        parent  = (current-1) // 2

        #----------Keep Going Until You Reach The Root----------#
        while parent > -1:

            #Swap parrent with current.
            if self.array[current].value < self.array[parent].value:
                self.__swap__(current, parent)
                pass

            #Done.
            else:
                break

            #Calculate new indexes.
            current = parent
            parent  = (current-1) // 2
        #----------Keep Going Until You Reach The Root----------#
    #======================Shift Up=======================#





    #=====================Shift Down======================#
    def __shiftDown__(self):
        '''Order the queue after the root has been poped.'''
        

        current = 0 #Current Node.
        left    = 1 #Left child.
        right   = 2 #Righ child.


        #-------------------------While Loop-------------------------#
        while current < self.index:

            #If current has two children.
            if left < self.index and right < self.index:

                #Left is less than right and less than the parent
                #so swap left with the parent.
                if self.array[left].value < self.array[right].value:
                    if self.array[left].value < self.array[current].value:
                        self.__swap__(left, current)
                        current = left

                    else:
                        break

                #Right is less or equal to left and less than then parent,
                #so swap right with his parent.
                else:
                    if self.array[right].value < self.array[current].value:
                        self.__swap__(right, current)
                        current = right

                    else:
                        break


            #Current has only a left child.
            elif left < self.index and right >= self.index:

                #Left is less than the parent
                #so swap left with the parent.
                if self.array[left].value < self.array[current].value:
                    self.__swap__(left, current)
                    current = left

                else:
                    break


            #Current has only a right child.
            elif left >= self.index and right < self.index:

                #Right is less than then parent,
                #so swap right with his parent.
                if self.array[right].value < self.array[current].value:
                    self.__swap__(right, current)
                    current = right

                else:
                    break


            #Finished.
            else:
                break
            

            #Calculate new indexes.
            left  = 2*current+1
            right = 2*current+2
        #-------------------------While Loop-------------------------#
    #=====================Shift Down======================#





    #========================Swap=========================#
    def __swap__(self, index1, index2):
        '''Swap two nodes from the queue.'''
        
        temp = self.array[index1]

        self.array[index1] = self.array[index2]

        self.array[index2] = temp
        
    #========================Swap=========================#

        
        



    #======================Preorder=======================# 
    def __preorder__(self, root):
        '''Just for debuggin.'''

        #Break statement.
        if root >= self.index:
            return

        #Print.
        print("--------|Node: "+str(root)+"|--------")
        self.array[root].print()
        print("--------|Node: "+str(root)+"|--------\n")

        #Visit other nodes.
        self.__preorder__(2*root+1) #First visit the left subtree.
        self.__preorder__(2*root+2) #Then the right subtree.


    def preorder(self):
        '''Just for debuggin.'''
        self.__preorder__(0)
    #======================Preorder=======================# 

        
