def year_hundred():
    hundred = 0
    if age_year < 100:
        print("Your current age is : {}".format(age_year))
        yob = 2021 - age_year
        hundred = yob + 100
        print("You will turn 100 in the year: ",hundred)
    elif 100 < age_year < 200:
        print("You are already above 100 years...")
        print("Your current age is : {}".format(age_year))
    elif 1800 < age_year < 2021:
        print("Your year of birth is: {}".format(age_year))
        age = 2021 - age_year
        print("Your current age is :",age)
        hundred = age_year + 100
        print("You will turn hundred in the year:",hundred)
    elif age_year > 2021:
        print("You have not been born!!")
    else:
        print("Invalid Input!!!")
    return hundred


age_year = int(input("Enter your age or year of birth: "))
year_hundred()



