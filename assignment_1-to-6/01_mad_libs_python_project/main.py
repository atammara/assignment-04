import random

def get_word(prompt):
    while True:
        word = input(prompt).strip()
        if word:
            return word
        print("Please enter a word!")

def mad_libs_enhanced():
    print("""
    ███╗   ███╗ █████╗ ██████╗     ██╗     ██╗██████╗ ███████╗
    ████╗ ████║██╔══██╗██╔══██╗    ██║     ██║██╔══██╗██╔════╝
    ██╔████╔██║███████║██║  ██║    ██║     ██║██████╔╝███████╗
    ██║╚██╔╝██║██╔══██║██║  ██║    ██║     ██║██╔══██╗╚════██║
    ██║ ╚═╝ ██║██║  ██║██████╔╝    ███████╗██║██████╔╝███████║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝╚═════╝ ╚══════╝
    """)
    
    stories = [
        {
            "title": "Space Adventure",
            "template": """
            Today we're going to {verb} to {place} in our {adjective} spaceship! 
            Our mission is to find {noun} and bring back {food} for the {animal}s.
            """
        },
        {
            "title": "Pirate Story",
            "template": """
            'Arrr!' said the {adjective} pirate as he {verb} {adverb} toward the {noun}.
            'I'll trade ye this {food} for that treasure map,' said the {animal}.
            """
        }
    ]
    
    # Let user choose a story
    print("Choose a story theme:")
    for i, story in enumerate(stories, 1):
        print(f"{i}. {story['title']}")
    
    choice = input("Enter number (or random): ").strip()
    if choice.lower() == "random":
        story = random.choice(stories)
    else:
        try:
            story = stories[int(choice)-1]
        except:
            story = stories[0]
    
    print(f"\nSelected: {story['title']}")
    print("Please provide the following words:")
    
    # Get words needed for this story
    words = {}
    if "{adjective}" in story["template"]:
        words["adjective"] = get_word("Enter an adjective: ")
    if "{noun}" in story["template"]:
        words["noun"] = get_word("Enter a noun: ")
    if "{verb}" in story["template"]:
        words["verb"] = get_word("Enter a verb: ")
    if "{adverb}" in story["template"]:
        words["adverb"] = get_word("Enter an adverb: ")
    if "{animal}" in story["template"]:
        words["animal"] = get_word("Enter an animal: ")
    if "{food}" in story["template"]:
        words["food"] = get_word("Enter a food: ")
    if "{place}" in story["template"]:
        words["place"] = get_word("Enter a place: ")
    
    # Fill in the story
    result = story["template"].format(**words)
    
    print("\nHere's your Mad Libs story:")
    print("="*50)
    print(result)
    print("="*50)

if __name__ == "__main__":
    while True:
        mad_libs_enhanced()
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break