from colorama import Fore, init
from huffman import encoder
init()

# add compressed size of each item to a list
beforeCompList = []
afterCompList = []

# note.txt file include test sentences
with open('note.txt', 'r') as f:
    # each time take one line from note.txt file 
    for line in f:
        text = line.strip()
        
        encoder_tuple = encoder(text)
        beforeCompression, afterCompression = (encoder_tuple[4], encoder_tuple[5])

        # add before and after compression result to lists
        beforeCompList.append(beforeCompression)
        afterCompList.append(afterCompression)

print(Fore.CYAN + "number of sentences: " + Fore.RESET, len(beforeCompList))
print(Fore.RED + "Occupied space before compression for each text: " + Fore.RESET, *beforeCompList)
print(Fore.GREEN + "Occupied space after compression for each text: " + Fore.RESET, *afterCompList)

# calculate sum of each list items
sumBeforeComp = sum(beforeCompList)
sumAfterComp = sum(afterCompList)

# calculate the average compression rate
average = ((sumBeforeComp - sumAfterComp) / sumBeforeComp ) * 100

print(Fore.CYAN + "\nCompression average rate: " + Fore.RESET, int(average),"%")
