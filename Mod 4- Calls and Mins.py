name =input("Enter customer name: ")
customerCalls = float(input("How many calls {name} made for the last month: "))
callDuration = float(input("How many minutes {name} made for the last month: "))
if customerCalls > 200 and callDuration >1000:
    print("Apply Premium Rate")
else
    print("Normal Rate")

