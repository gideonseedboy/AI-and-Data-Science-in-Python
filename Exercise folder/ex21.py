# Identity Operators

x = ["gideon", "0292929" "Church Father"]
y = ["Abi", "Mmiriam", "Tabita", "Grace", "Deborah"]
z = y

print(z is y) # The is Operator checks the memory alocation of the two parameters
                # Please note that the (==) operator is different from the (is) Operator

ages = [20, 30, 30]
boys = [20, 30, 30]
guys = boys
# print(f"Equality statues of ages and boys: {ages == boys}")

print(guys)
print(guys is boys)
print(guys == boys)


# is not

print(ages is not boys)
print(x is not y)
print(z is not y)

