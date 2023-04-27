# Task 4.2
# Write a function to classify a student’s mark as to whether it is a first class mark, a 2(i) mark,
# a 2(ii) mark, a third class mark or a fail. The function should take as an argument a mark (a
# float between 0.0 and 100.0)

def main():
    mark = float(input("Please enter a value between 0 and 100 inclusively: "))

    print("This student is classified as "+ classification(mark) +".")


def classification(mark):
    if mark < 40:
        return "Fail"
    if mark >= 40 and mark < 50:
        return "Third"
    if mark >= 50 and mark < 60:
        return "2(ii)"
    if mark >= 60 and mark < 70:
        return "2(i)"
    if mark >= 70:
        return "First"
    
main()
