# fantasy game inventory

sample = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    print("Inventory: ")
    item_total = 0
    for k, v in inv.items():
        print(v, k)
        item_total += 1
    print("Total number of items: " + str(item_total))


displayInventory(sample)

orcloot = ['torch', 'mace', 'earlobes', 'gold coin']

def addToInvenotry(inv, addedItems):
    for loot in addedItems:
        inv.setdefault(loot, 0) # if inventory doesnt contain the item add its and then set count to 0
        inv[loot] += 1 #increments the item in the inventory
    return(inv)

addToInvenotry(sample, orcloot)
displayInventory(sample)

emptydict = {}

emptydict.setdefault('gun', '1')

displayInventory(emptydict)
