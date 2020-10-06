
allShops = []


while True:
    shop = input("Enter shop name: ")

    if shop == "":
        break
    else:
        allShops.append(shop)

print(allShops)