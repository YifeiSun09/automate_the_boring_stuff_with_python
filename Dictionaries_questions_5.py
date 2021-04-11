#Fantasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total+=int(v)
    print("Total number of items: " + str(item_total))
displayInventory(stuff)



#List to Dictionary Function for Fantasy Game Inventory
def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]]=inventory[addedItems[i]+1]
        else:
            inventory.setdefault(addedItems[i],1)
    return inventory

def dissplayInventory(inventory):
    total_items=0
    for k,v in inventory.items():
        print(k+':'+str(v))
        total_items=total_items+v
    print('total num of items are:'+str(total_items))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)