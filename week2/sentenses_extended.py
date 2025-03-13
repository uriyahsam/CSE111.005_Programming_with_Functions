import random

# Function to get a determiner (single/plural)
def get_determiner(quantity):
    """Return a randomly chosen determiner."""
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

# Function to get a noun (single/plural)
def get_noun(quantity):
    """Return a randomly chosen noun."""
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", 
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", 
                 "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

# Function to get a verb based on quantity and tense
def get_verb(quantity, tense):
    """Return a randomly chosen verb."""
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think",
                     "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    return random.choice(words)

# Exceeding Requirement: Adding an adjective to describe the noun
def get_adjective():
    """Return a randomly chosen adjective."""
    words = ["beautiful", "quick", "happy", "sad", "tall", "short", 
             "brave", "clever", "angry", "lazy"]
    return random.choice(words)

# Exceeding Requirement: Adding an adverb to describe the verb
def get_adverb():
    """Return a randomly chosen adverb."""
    words = ["quickly", "silently", "bravely", "happily", "sadly", 
             "lazily", "angrily", "eagerly", "elegantly", "calmly"]
    return random.choice(words)

# Function to get a preposition
def get_preposition():
    """Return a randomly chosen preposition."""
    words = ["about", "above", "across", "after", "along", "around", 
             "at", "before", "behind", "below", "beyond", "by", 
             "despite", "except", "for", "from", "in", "into", 
             "near", "of", "off", "on", "onto", "out", "over", 
             "past", "to", "under", "with", "without"]
    return random.choice(words)

# Function to construct a prepositional phrase
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()  # Exceeding Requirement: Adding adjective to prepositional phrase
    return f"{preposition} {determiner} {adjective} {noun}"

# Function to construct a sentence
def make_sentence(quantity, tense):
    """
    Build and return a sentence with a determiner, noun, verb, adjective, adverb, 
    and two prepositional phrases.
    """
    determiner = get_determiner(quantity)
    adjective = get_adjective()  # Exceeding Requirement: Adding adjective to main noun
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adverb = get_adverb()  # Exceeding Requirement: Adding adverb to describe the verb
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)  # Exceeding Requirement: Adding second prepositional phrase
    
    # Constructing the sentence with all components
    sentence = (f"{determiner.capitalize()} {adjective} {noun} {verb} {adverb} "
                f"{prepositional_phrase1} {prepositional_phrase2}.")
    return sentence

# Main function to generate sentences
def main():
    # Generate and print six sentences with required and exceeded features
    print(make_sentence(1, "past"))      # single, past
    print(make_sentence(1, "present"))  # single, present
    print(make_sentence(1, "future"))   # single, future
    print(make_sentence(2, "past"))     # plural, past
    print(make_sentence(2, "present"))  # plural, present
    print(make_sentence(2, "future"))   # plural, future

# Call the main function
if __name__ == "__main__":
    main()
