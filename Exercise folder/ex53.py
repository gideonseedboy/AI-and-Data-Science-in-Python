
gender = input("Enter you Gender: ")

if gender == "female":
    print("Pick a white form!")
elif gender == "male":
    doesQualify = input("Do you have qualification? yes/no: ")
    if doesQualify == "Yes":
        print("Pick blue form")
    elif doesQualify == "no":
        haveProtocol = input("Do you have protocol? Yes/No: ")
        if haveProtocol == "yes":
            print("pick green form!")
        else:
            print("Take I.Q test")
else:
    print("gender not found")