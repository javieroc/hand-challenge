import emoji
from typing import List, Tuple, Union

'''
👉 : moves the memory pointer to the next cell
👈 : moves the memory pointer to the previous cell
👆 : increment the memory cell at the current position
👇 : decreases the memory cell at the current position.
🤜 : if the memory cell at the current position is 0, jump just after the corresponding 🤛
🤛 : if the memory cell at the current position is not 0, jump just after the corresponding 🤜
👊 : Display the current character represented by the ASCII code defined by the current position.
'''


def read_file(filename: str) -> List[str]:
    with open(filename, encoding="utf8") as file:
        emoji_string = file.read()
        emojis = [em for em in emoji_string if em in emoji.UNICODE_EMOJI['en']]
        return emojis


def get_matching_fists(emojis: List[str]) -> List[Union[str, int]]:
    result = [*emojis]
    stack = []
    for i, c in enumerate(result):
        if c == "🤜":
            stack.append(i)
        elif c == "🤛":
            result[stack[-1]] = i
            result[i] = stack.pop()
    return result


def translate(emojis: List[str]):
    memory = [0] * len(emojis)
    matching_fists = get_matching_fists(emojis)
    pointer = 0
    index = 0
    message = ''
    while index < len(emojis):
        action = emojis[index]
        if (action == '👉'):
            pointer += 1
        elif (action == '👈'):
            pointer -= 1
        elif (action == '👆'):
            memory[pointer] = 0 if memory[pointer] == 255 else memory[pointer]+1
        elif (action == '👇'):
            memory[pointer] = 255 if memory[pointer] == 0 else memory[pointer]-1
        if (memory[pointer] == 0 and action == '🤜'):
            index = matching_fists[index]
        elif (memory[pointer] != 0 and action == '🤛'):
            index = matching_fists[index]
        elif (action == '👊'):
            message = message + chr(memory[pointer])
        index = index + 1
    return message


def main():
    emojis = read_file('input.hand.txt')
    message = translate(emojis)
    print(message)

main()
