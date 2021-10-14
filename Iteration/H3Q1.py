Largest = 'a'
Smallest = 'z'
for i in range(5):
    entry = input('letter')
    if ord(entry) > ord(Largest):
        Largest = entry
    # end if
    if ord(entry) < ord(Smallest):
        Smallest = entry
    # end if
# next i

print(Largest, Smallest)
