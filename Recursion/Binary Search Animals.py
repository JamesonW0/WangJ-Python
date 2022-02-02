# Binary Search Animals
nameList = ["baboon", "cheetah", "elephant", "giraffe", "hippo", "leopard", "lion", "mongoose", "rhino", "warthog"]

animal = "warthog"

def search(name, high, low, nameList):
    guess = (low + high) // 2
    if nameList[guess] == animal:
        return guess
    elif nameList[guess] > animal:
        return search(name, guess - 1, low, nameList)
    else:
        return search(name, high, guess + 1, nameList)

print(search(animal, len(nameList) - 1, 0, nameList))

input("\nPress ENTER to exit program ")
