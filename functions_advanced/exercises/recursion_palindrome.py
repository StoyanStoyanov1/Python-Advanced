def palindrome(text, start_index, end_index=-1):
    if start_index == len(text) // 2:
        return f"{text} is a palindrome"

    if text[start_index] != text[end_index]:
        return f"{text} is not a palindrome"

    return palindrome(text, start_index + 1, end_index - 1)

print(palindrome("abcba", 0))
print(palindrome("peter", 0))