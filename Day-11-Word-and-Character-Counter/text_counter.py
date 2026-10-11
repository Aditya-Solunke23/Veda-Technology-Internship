print("========================================")
print("      WORD AND CHARACTER COUNTER")
print("========================================")

paragraph = input("\nEnter a paragraph: ").strip()

if not paragraph:
    print("\nError: The paragraph cannot be empty.")
else:
    # Count total characters
    character_count = len(paragraph)

    # Count words
    words = paragraph.split()
    word_count = len(words)

    # Count spaces
    space_count = paragraph.count(" ")

    # Count sentences using sentence-ending punctuation
    sentence_count = 0

    for character in paragraph:
        if character in ".!?":
            sentence_count += 1

    print("\n========== TEXT STATISTICS ==========")
    print(f"Characters : {character_count}")
    print(f"Words      : {word_count}")
    print(f"Sentences  : {sentence_count}")
    print(f"Spaces     : {space_count}")
    print("=====================================")