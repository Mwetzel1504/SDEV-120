passGrade = 60

name = input("Please enter your name: ")
grade = float(input(f"Hello {name}, please enter your score: "))

if grade >= passGrade:
    print(f"Congratulations {name}! You have passed this class. - Making Decisions:8")
else:
    print(f"Sorry {name}, you have failed this class. - Making Decisions:10")
