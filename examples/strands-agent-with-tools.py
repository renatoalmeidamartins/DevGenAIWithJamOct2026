from strands import Agent, tool
from strands.vended_tools import file_editor
from strands_tools import generate_image

@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())

agent = Agent(tools=[letter_counter, file_editor, generate_image])
agent('How are you doing today?')
agent('Draw me a Breaking-bad inspired image of a dog wearing sunglasses')
agent('How many letter R\'s are in the word "strawberry"? Write the answer to answer.txt.')