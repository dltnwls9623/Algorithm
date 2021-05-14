def is_palindrome(sentence):
    sentence = sentence.lower()
    origin = [s for s in sentence if s.isalnum()]

    if origin == origin[::-1]:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    testcases = ["A man, a plan, a canal: Panama", "race a car", "12321"]
    for testcase in testcases:
        is_palindrome(testcase)