# Task 4.4
# Write a function which is capable of converting to and from many types of length and weight units

def main():
    print(conversion("cm", "m", 6))
    print(conversion("kg", "lbs", 16))
    print(conversion("kg", "m", 5))
    

def conversion(source, target, value):
    length = ["cm", "in", "m"]
    weight = ["kg", "lbs", "st"]
    if source in length and target in length:
        converted = length_conversion(source, target, value)
    elif source in weight and target in weight:
        converted = weight_conversion(source, target, value)
    else:
        return -1
    return converted    

    
def length_conversion(source, target, value):
    m_to_cm = 100
    in_to_cm = 2.54
    in_to_m = in_to_cm / m_to_cm
    
    if source == "m" and target == "cm":
        length_converted = float(value) * m_to_cm
    if source == "cm" and target == "m":
        length_converted = float(value) / m_to_cm
    if source == "in" and target == "cm":
        length_converted = float(value) * in_to_cm
    if source == "cm" and target == "in":
        length_converted = float(value) / in_to_cm
    if source == "in" and target == "m":
        length_converted = float(value) * in_to_m
    if source == "m" and target == "in":
        length_converted = float(value) / in_to_m

    return length_converted

def weight_conversion(source, target, value):
    kg_to_lbs = 2.2
    st_to_lbs = 14
    st_to_kg = 6.35

    if source == "kg" and target == "lbs":
        weight_converted = float(value) * kg_to_lbs
    if source == "lbs" and target == "kg":
        weight_converted = float(value) / kg_to_lbs
    if source == "st" and target == "lbs":
        weight_converted = float(value) * st_to_lbs
    if source == "lbs" and target == "st":
        weight_converted = float(value) / st_to_lbs
    if source == "st" and target == "kg":
        weight_converted = float(value) * st_to_kg
    if source == "kg" and target == "st":
        weight_converted = float(value) / st_to_kg

    return weight_converted
        
main()
