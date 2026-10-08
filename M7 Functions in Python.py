# Step 1-3: Define the greater_than functions with two parameters
def greater_than(x, y):
    if x > y:
            return True
    else:
            return False

#Main section of the program
def main():
    #1. Ask the user to input two numbers
    #We convert them to float/int so the mathmatical comparison works correctly
    a = float(input("Enter the first number (a): "))
    b = float(input( "Enter the second number (b): "))

    #2. Call the function and store the result in a variable
    result = greater_than(a, b)

    #3. Print the output statement using string concatenation as requested
    # We convert a, b, and result to str() to combine them seamlessly
    print("The statement" +str(a) + "is greater than " +str(b) + "is " + str(result))

# Run the main program
__name__ == "__main__"
main()
