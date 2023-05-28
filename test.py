from huffman_coding import runner
import random

data_list = []

alpha = "ABCD"


for i in range(0, 99):
    string = ''
    for i in range(random.randint(1,9)):
        char = random.choice(alpha)
        string = ''.join(char)
    
    data_list.append(string)

print(data_list)

# for item in data_list:
#     runner(item)

mohsnrj

