# Ask the user the weight in either KGs or lbs and convert it to other form
import PackageDemo as methods


yes_list = ['YES','Y']
no_list = ['NO','N']
input_weight = 0

while True :
    input_type = input("Are you entering weight in KGs? (YES/NO/Y/N) : ").upper()
    if input_type not in yes_list and input_type not in no_list:
        print("You have entered invalid input, Please enter one of these values - YES/NO/Y/N \n")
        continue
    else :
        input_weight = input("Please enter your weight : ")
        try:
            input_weight = float(input_weight)
            break
        except ValueError:
            print("Weight has to be a number, Please enter correct value")



if input_type in yes_list:
    # Converting to pounds
    methods.convert_to_pounds(input_weight)
else:
    # Converting to KGs
    methods.convert_to_kgs(input_weight)

