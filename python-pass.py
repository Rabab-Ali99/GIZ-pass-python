def find_longest_palindromic_substring(string):
    result_string = ""
    result_length = 0

    for i in range(len(string)):
        # here we considering odd length so starting from the middle of string and expanding
        left_pointer = i
        right_pointer = i
        while left_pointer >= 0 and right_pointer < len(string) and string[left_pointer] == string[right_pointer]:
            # check if this is the longest Palindrome until now
            if (right_pointer - left_pointer + 1) > result_length:
                # if it is the longest store it
                result_string = string[left_pointer:right_pointer + 1]
                result_length = right_pointer - left_pointer + 1

            # after checking the left pointer will be shifting to the left
            # and the right one will be shifted to the right
            right_pointer += 1
            left_pointer -= 1

        # here we considering even length so starting from the middle of string and expanding
        left_pointer = i
        right_pointer = i + 1
        while left_pointer >= 0 and right_pointer < len(string) and string[left_pointer] == string[right_pointer]:
            if (right_pointer - left_pointer + 1) > result_length:
                result_string = string[left_pointer:right_pointer + 1]
                result_length = right_pointer - left_pointer + 1
            right_pointer += 1
            left_pointer -= 1

    print(result_string)


find_longest_palindromic_substring('babad')
find_longest_palindromic_substring('cbbd')
find_longest_palindromic_substring('a')
find_longest_palindromic_substring('ac')

