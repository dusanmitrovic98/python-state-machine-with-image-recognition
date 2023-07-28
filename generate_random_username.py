import random

def generate_random_username():
    syllables = [
        "ba", "be", "bi", "bo", "bu",
        "ca", "ce", "ci", "co", "cu",
        "da", "de", "di", "do", "du",
        "fa", "fe", "fi", "fo", "fu",
        "ga", "ge", "gi", "go", "gu",
        "ha", "he", "hi", "ho", "hu",
        "ja", "je", "ji", "jo", "ju",
        "ka", "ke", "ki", "ko", "ku",
        "la", "le", "li", "lo", "lu",
        "ma", "me", "mi", "mo", "mu",
        "na", "ne", "ni", "no", "nu",
        "pa", "pe", "pi", "po", "pu",
        "ra", "re", "ri", "ro", "ru",
        "sa", "se", "si", "so", "su",
        "ta", "te", "ti", "to", "tu",
        "va", "ve", "vi", "vo", "vu",
        "za", "ze", "zi", "zo", "zu",
    ]
    
    numbers = [str(i) for i in range(10)]

    # Calculate the maximum number of syllables allowed to stay within 13 characters
    max_syllables = min(len(syllables), (13 - len(max(numbers, key=len))) // 2)

    # Randomly choose the number of syllables (1 to max_syllables)
    num_syllables = random.randint(1, max_syllables)

    # Generate random username
    chosen_syllables = random.choices(syllables, k=num_syllables)
    username = "".join(chosen_syllables) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers)

    # Truncate to 13 characters if necessary
    username = username[:13]
    
    return username
