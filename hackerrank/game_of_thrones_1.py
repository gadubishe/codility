__author__ = 'ask'

def check_palindrome(s):
    s = ''.join(sorted(s))

    prev_char = None
    middle_element = None
    # l = []

    for c in s:
        if prev_char is None:  # new set
            prev_char = c
        else:  # continue
            if c == prev_char:
                # l.append(prev_char)
                prev_char = None
            else:
                if middle_element is not None:
                    return False
                else:
                    middle_element = prev_char
                    prev_char = c
    return True

s = raw_input()
found = check_palindrome(s)

if not found:
    print("NO")
else:
    print("YES")
