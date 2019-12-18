class Node():

    # My character
    char = None
    nodes = []

    def __init__(self, charr):
        self.char = charr
        return None

    def get_element(self, pos):
        return self.nodes[pos]

    def get_list(self):
        return None

    def link(self, node):
        pos = None
        if node in self.nodes:
            pos = self.nodes.index(node)
        else:
            self.nodes.append(node)
            pos = self.nodes.index(node)

        return pos

class Node_list():

    # Holds dictionary for char to node
    list_of_nodes = {}
    
    current_node  = None
    previous_node = None

    def __init__(self):
        return None

    def exists(self, charr):
        if charr in self.list_of_nodes:
            return True
        else:
            return False

    def seed(self, charr):
        self.create_node(charr)
        self.current_node = self.list_of_nodes[charr]
        return None

    def create_node(self, charr):
        if self.exists(charr):
            raise ValueError('Attempting to create node that exists :(')
        else:
            self.list_of_nodes[charr] = Node(charr)

    def link(self, charr):
        self.previous_node = self.current_node
        self.current_node = self.list_of_nodes[charr]

        pos = self.previous_node.link(self.current_node)

        return pos

    # Used to add charrs to the structure
    def add(self, charr):
        ## Handle New chars
        # Check if char has been seen before
        if not self.exists(charr):
            self.create_node(charr)
        else:
            # Do nothing atm
            hi = 3

        ## Do mapping logic A --> B 
        pos = self.link(charr)
        
        #print(charr)
        return pos

    # Will eventually be used to dump the data needed to reconstruct the original text
    def dump(self, p_list):
        arr = []
        self.current_node  = None
        self.previous_node = None

        self.current_node = self.list_of_nodes['start']

        for i in p_list:
            node = self.current_node.get_element(i)
            arr.append(node.comp())
            print(node.char)
            self.current_node = node

        return arr

    # Will eventually be used to construct the data to text
    def pull(self, p_list):
        self.current_node  = None
        self.previous_node = None

        self.current_node = self.list_of_nodes['start']

        for i in p_list:
            node = self.current_node.get_element(i)
            print(node.char)
            self.current_node = node

        return None


def main():
    myBrain = Node_list()
    myBrain.seed('start')

    p_list = []
    
    try:
        # Work with data
        with open("small-data") as infile:
            for line in infile:
                for i in line:
                    p = myBrain.add(i)
                    p_list.append(p)

        # Output bitstream array
        arr = myBrain.dump(p_list)

        # Test reconstruction
        myBrain.pull(p_list)

    except Exception as e:
        print(e)

if __name__== "__main__":
  main()





