Largest = 'a'
Smallest = 'z'
for i in range(5):
    entry = input('letter')
    if ord(entry) > ord(Largest):
        Largest = entry
    if ord(entry) < ord(Smallest):
        Smallest = entry
print(Largest, Smallest)
