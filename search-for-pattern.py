"""
Description: This program is to search for a pattern of characters in a text string.
If the pattern occurs in the text, then your program should output the position in
the text of the beginning of the first match.  If the pattern does not occur,
your program should output "No match".
"""


def main():

    text = input("enter a string: ")
    pattern = input("enter a pattern: ")

    FOUND = False
    for i in range(0, len(text), len(pattern)-1):
        if text[i:i+len(pattern)] == pattern:
            FOUND = True
            print(i)

    if not FOUND:
        print("No match")

main()
