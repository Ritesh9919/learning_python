
items = ["Mango", "Banana", "Apple", "Banana"]

unique_item = set()


for item in items:
    if item in unique_item:
        print("Dublicate", item)
    else:
        unique_item.add(item)   
        
    print(unique_item)        
        