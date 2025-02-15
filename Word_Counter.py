import string

def count_words(text):
    """Counts words"""

    if not text:
        return 0

    # 1. Replace all whitespace characters with regular spaces
    text = text.replace('\xa0', ' ')  # Non-breaking space (Unicode)
    text = text.replace('&nbsp;', ' ')  # Non-breaking space (HTML entity)
    text = text.replace(' ', ' ')  # Non-breaking space character (if copied directly)
    text = text.replace('\t', ' ')  # Tab
    text = text.replace('\n', ' ')  # Newline
    text = text.replace('\r', ' ')  # Carriage return
    # Add other whitespace characters here if needed
    text = text.replace('\v', ' ')  # Vertical tab

    # 2. Remove multiple spaces (replace with single spaces)
    while "  " in text:  # Check for double spaces
        text = text.replace("  ", " ")  # Replace double spaces with single spaces

    # 3. Remove leading/trailing spaces
    text = text.strip()

    # 4. Remove punctuation (except apostrophes within words)
    punctuation = string.punctuation.replace("'", "")  # Remove ' from punctuation
    new_text = ""
    for char in text:
        if char not in punctuation:
            new_text += char
    text = new_text

    # 5. Handle apostrophes at the beginning/end of words
    words_with_apostrophes = text.split()
    cleaned_words = []
    for word in words_with_apostrophes:
        if word.startswith("'") and word.endswith("'"):
            cleaned_words.append(word[1:-1].lower())  # Remove leading and trailing apostrophes
        elif word.startswith("'"):
            cleaned_words.append(word[1:].lower())  # Remove leading apostrophe
        elif word.endswith("'"):
            cleaned_words.append(word[:-1].lower())  # Remove trailing apostrophe
        else:
            cleaned_words.append(word.lower())  # Convert to lowercase

    # 6. Remove empty strings (if any)
    final_words = []
    for word in cleaned_words:
        if word:  # Check if the word is not empty
            final_words.append(word)

    return len(final_words)


def main():
    while True:
        text = input("Enter your text (or type 'exit' to quit): ")
        if text.lower() == "exit":
            break

        total_words = count_words(text)

        if total_words > 0:
            print(f"Total word count: {total_words}")
        else:
            print("No words found in the input.")


if __name__ == "__main__":
    main()