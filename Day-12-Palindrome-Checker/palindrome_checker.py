print("========================================")
print("          PALINDROME CHECKER")
print("========================================")

text = input("\nEnter a word or sentence: ")

# Normalize the input by converting to lowercase
# and removing unnecessary spaces
normalized_text = "".join(text.lower().split())

if not normalized_text:
    print("\nError: Input cannot be empty.")
else:
    # Reverse the normalized text using string slicing
    reversed_text = normalized_text[::-1]

    print("\n========== PALINDROME RESULT ==========")
    print(f"Original Input : {text}")
    print(f"Normalized     : {normalized_text}")

    if normalized_text == reversed_text:
        print("Result         : It is a palindrome!")
    else:
        print("Result         : It is not a palindrome.")

    print("========================================")