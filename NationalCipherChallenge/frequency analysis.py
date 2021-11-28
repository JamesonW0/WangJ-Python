file_address = input('enter the address of the file')
file = open(file_address, mode='r')
frequency = {}
text = file.read()
for i in range(0, len(text)):
    print(text[i])
    if text[i] =='\n':
        print(123)