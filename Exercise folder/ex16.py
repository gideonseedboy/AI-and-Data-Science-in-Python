#Replace Function


#print(word.replace(process, mathod))

x = """
According to the claim of our Lord and Savior Jesus Christ, Luke 18:1, 
men ought to pray and not to faint. At GCI  we therefore deduce
 that fainting is the opposite of praying. We therefore remind 
 ourselves always as brother Paul said, 1 Thes 5:16-18, to pray 
 in the ceaselessly dimensions. We keep it as a responsibility to 
 pray and God strengthening us we are growing daily with 
productivity in all aspects with testimonies following. 
"""


y = "I am a The Pastor of Ark of God Church Of all nations"


print(x.replace("therefore", "thus"))
print(y.replace("Pastor", "General Overseer" ))
print(y.replace("Ark of God Church Of all nations", "GODMAN CITY INCORPORATED"))

search = "dioxide" in x
search1 = "Christ" in x
search2 = "Lord" in x
#The Membership Operator (in / not in)

find = "God" not in x
find1 = "Money" not in y


print(search)
print(search1)
print(search2)
print(find)
print(find1)

# if find1 == "true":
#     print("We need to add money to the text...")
# else:
#     print("We are good to go!")

