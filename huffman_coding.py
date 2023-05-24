import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel

"""
test program!!
"""

class TreeNodes:  
    def __init__(self, frequency, symbol, left = None, right = None):  
        """ Options of each node """
        # frequency of the symbol  
        self.frequency = frequency  
  
        # the symbol  
        self.symbol = symbol  
  
        # left and right nodes
        self.left = left    
        self.right = right  
  
        # address code of each node (0 or 1)  
        self.code = ''  
  

""" save code of each node in 'queue' dictionary """  
queue = dict()  
  
def symbol_code(node, value = ''):
    """ navigate items of queue to till reach the last leaf  """
    # a huffman code for current node  
    newValue = value + str(node.code)  
  
    if(node.left): 
        symbol_code(node.left, newValue)  
    if(node.right):  
        symbol_code(node.right, newValue)  
  
    if(not node.left and not node.right):  
        queue[node.symbol] = newValue  
           
    return queue  
    
# alireza daneshfar
def output_list(data, coding):  
    """ print the binary string of encoded data """
    binary_output = []

    for item in data:   
        binary_output.append(coding[item])  
          
    result = ''.join([str(item) for item in binary_output])      
    return result  
          
# alireza daneshfar
def compare_compression(data, coding):  
    """ compare compressed data before and after compression """
    # each element of queue takes 8 bits
    # before compression
    before_comp = len(data) * 8  

    # after compression
    after_comp = 0  

    # symbols are keys of the queue dictionary
    chosen_symbol = coding.keys()  

    for symbol in chosen_symbol:  
        count_symbols = data.count(symbol)  
    
        # required bits for compressed data  
        after_comp += count_symbols * len(coding[symbol])  

    print("Space usage before compression (in bits):", before_comp)  
    print("Space usage after compression (in bits):",  after_comp)  


def symbol_freq(data):  
    """ count frequency of each symbol """
    chosen_symbol = dict() 

    # after each repetition of element queue item val + 1 
    for item in data:  
        if chosen_symbol.get(item) == None:  
            chosen_symbol[item] = 1  
        else:   
            chosen_symbol[item] += 1     

    # return number of each symbol freq  
    return chosen_symbol  
  
  
def encoder(data):  
    """ Huffman ecnoder """
    string_symbols = symbol_freq(data)  
    chosen_symbol = string_symbols.keys()  
    freq = string_symbols.values()  

    print("symbols: ", chosen_symbol)  
    print("frequency: ", freq)  
      
    # save nodes in a list
    nodes = []  
      
    # making the huffman tree use nodes and symbols
    for symbol in chosen_symbol:  
        nodes.append(TreeNodes(string_symbols.get(symbol), symbol))  
      
    while len(nodes) > 1:  
        # sorting nodes 
        nodes = sorted(nodes, key = lambda x: x.frequency)  
        
        # small nodes  
        right = nodes[0]  
        left = nodes[1]  

        # left and right nodes code
        left.code = 0  
        right.code = 1  
      
        # create a new node. smaller node on left leaf  
        new_node = TreeNodes(left.frequency + right.frequency, left.symbol + right.symbol, left, right)  

        # delete first smallest nodes and replace them with new node
        nodes.remove(left)  
        nodes.remove(right)
        # add the new node the tree
        nodes.append(new_node)  
    
    # start the tree from first node (0 index) 
    encoder = symbol_code(nodes[0])  
    print("symbols with codes", encoder)  

    # compare compression after huffman encoding
    compare_compression(data, encoder)  
    
    # create a binary output
    encoded_data = output_list(data,encoder)  


    return encoded_data, nodes[0]  

  
def decoder(encode_data, tree):  
    """ travel the tree code till reach the last leaf and add the last leaf symbol to the decode list """
    treeHead = tree  

    decoded_data = []  
    for x in encode_data:  
        if x == '1':  
            tree = tree.right     
        elif x == '0':  
            tree = tree.left
  
        try: 
            # check if it reach the last leaf 
            if tree.left.symbol == None and tree.right.symbol == None:  
                pass  
        except AttributeError as err:  
            decoded_data.append(tree.symbol)  
            tree = treeHead  
          
    string = ''.join([str(item) for item in decoded_data])  
    
    # return the main string
    return string  
  

""" GUI """

class InputDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Dialog")

        # Create widgets
        self.input_widget = QLineEdit()
        self.ok_button = QPushButton("OK")
        self.ok_button.setDefault(True)
        self.result_label = QLabel()

        # Add widgets to layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_widget)
        layout.addWidget(self.ok_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        # Set connections
        self.ok_button.clicked.connect(self.get_input_text)

    def get_input_text(self):
        text = self.input_widget.text()
        encoding, tree = encoder(text)
        self.result_label.setText(f"Encode: {encoding}")
        self.result_label.setText(f"decode: {decoder(encoding, tree)}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = InputDialog()
    dialog.exec()

    sys.exit(app.exec())

# --=================
# data = "feshar"  
# print(data)  
# encoding, the_tree = encoder(data)  
# print("Encoded output", encoding)  
# print("Decoded Output", decoder(encoding, the_tree))  