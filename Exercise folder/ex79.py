#function

_shopNames = []
_shopNumbers = []
_shopLocations = []
_shopAdmin = []
_shopClass = []


def insertShop(shopName, shopNumber, shopLocation, shopAdmin, shopClass):
    _shopNames.append(shopName)
    _shopNumbers.append(shopNumber)
    _shopLocations.append(shopLocation)
    _shopAdmin.append(shopAdmin)
    _shopClass.append(shopClass)

def displayShops():
    allShops = len(_shopNames)
    for x in range(allShops):
       
        print(f"""

        ******************************** ALL SHOPPER NETWOK *******************************

                Name of shop:      {_shopNames[x]}
                Shop Number:       {_shopNumbers[x]}
                Shop Location:     {_shopLocations[x]}
                Shop Admin:        {_shopAdmin[x]}
                Shop Class:        {_shopClass[x]}
            ...............................................................................
            ........................Designed by Ojay Technologies..........................
            _______________________________________________________________________________

        """)


nameOfShop = input("Enter Shop name: ")
numOfShop = input("Enter Shop number: ")
locationOfShop = input("Enter Shop location: ")
adminOfShop = input("Enter Shop admin: ")
classOfShop = input("Enter Shop class: ")


        

insertShop(nameOfShop,numOfShop,locationOfShop,adminOfShop,classOfShop)
displayShops() 