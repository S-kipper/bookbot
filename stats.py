def num_of_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["count"]


def char_appears(words):
    words = words.lower()
    counts = {}

    for char in words:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
        
    result = []

    for key, value in counts.items():
        result.append({"char": key, "count": value})
        
    result.sort(reverse=True, key=sort_on)
        
    return result
