import tkinter as tk
from huffman import encoder, decoder, cleaner

def show_result():
    # Get the data from the entry widget
    data = data_entry.get()
    
    encoding, tree, tree_queue, encode, beforeComp, afterComp = encoder(data)
    decoding = decoder(encoding, tree)

    if ' ' in tree_queue.keys():
        tree_queue['space'] = tree_queue.pop(' ')

    if ' ' in encode.keys():
        encode['sapce'] = encode.pop(' ')

    symobls = ' '.join('%s= %s,' % (k,tree_queue[k]) for k in tree_queue.keys())
    encode = ' '.join('%s= %s' % (k,encode[k]) for k in encode.keys())
    
    msg = f"""Symbols and frequency:\n{symobls}\nCode: \n{encode}\n\nSpace before compression: {beforeComp}
    Space after compression: {afterComp}\n\nEncoded result: {encoding}\n Decoding result: {decoding}\n"""
    
    # Update the label with the data
    result_label.config(text=msg, height=10, width=60, bd='4', font=("Times", "18"))
    cleaner()
# Create the main window
root = tk.Tk()

# Create the data label and entry widgets
data_label = tk.Label(root, text="Enter your data:")
data_entry = tk.Entry(root)

# Create the button widget
submit_button = tk.Button(root, text="Submit", command=show_result)

# Create the result label widget
result_label = tk.Label(root, text="")

# Pack the widgets into the window
data_label.pack()
data_entry.pack()
submit_button.pack()
result_label.pack()

# Start the main event loop
root.mainloop()
