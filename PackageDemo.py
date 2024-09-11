conversion_value = 0.450

def convert_to_pounds(weight):
    output_weight = round(weight / conversion_value, 2)
    print(f"Weight in pounds: {output_weight} lbs")


def convert_to_kgs(weight):
    output_weight = round(weight * conversion_value, 2)
    print(f"Weight in KGs: {output_weight} KGs")