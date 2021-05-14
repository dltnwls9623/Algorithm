import re


def is_palindrome(sentence):
    sentence = sentence.lower()
    # 정규표현식으로 영문자, 숫자만 제외 필터링
    sentence = re.sub('[^a-z0-9]', '', sentence)
    print(sentence == sentence[::-1])


if __name__ == "__main__":
    testcases = ["A man, a plan, a canal: Panama", "race a car", "12321"]
    for testcase in testcases:
        is_palindrome(testcase)