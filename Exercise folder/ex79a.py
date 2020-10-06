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

insertShop("Shop In Advance", "01122", "Accra - Ridge", "Tosin Joe", "Fashion and Design")
insertShop("Accra Mall", "03322", "Spanner - Interchanger", "Top Kafu", "Multi Stores")
insertShop("Wakyie House", "08121", "Adenta - NewSite", "Naana Jane", "Food")

print(f"""

******************************** ALL SHOPPER NETWOK *******************************

        Name of shop:      {_shopNames}
        Shop Number:       {_shopNumbers}
        Shop Location:     {_shopLocations}
        Shop Admin:        {_shopAdmin}
        Shop Class:        {_shopClass}
    ...............................................................................
    ........................Designed by Ojay Technologies..........................
    _______________________________________________________________________________

""")
