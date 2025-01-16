import time


def print_with_delay(text):
    pause = 0.2
    character_limit = 50
    text2 = text.split()
    character_counter = 0

    for word in text2:
        if character_counter + len(word) > character_limit:
            print()
            character_counter = 0


        print(word, end=' ', flush=True)
        character_counter += len(word) + 1  #
        time.sleep(pause)

    print()