def grade_in_words(grade):
    if 2.00 <= grade <= 2.99:
        print("Fail")
    elif 3.00 <= grade <= 3.49:
        print("Poor")
    elif 3.50 <= grade <= 4.49:
        print("Good")
    elif 4.50 <= grade <= 5.49:
        print("Very Good")
    elif 5.50 <= grade <= 6.00:
        print("Excellent")
    else:
        print("Invalid grade. Please enter a grade between 2.00 and 6.00.")

grade = float(input())
grade_in_words(grade)