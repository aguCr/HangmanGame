# adds 50 lines to terminal
def clear_screen(numlines=50):
    print('\n' * numlines)


# add space between chars
def space_it_out(source, count):
    return ''.join([c + (' ' * count) for c in source]).strip()

# hang man status
def draw_eyes():
    print("|---------------")
    print("| /            |")
    print("|/          WWWWWWW")
    print("|          <| x x |>")
    print("|            \\ - /")
    print("|          --------- ")
    print("|            / | \\")
    print("|           p  |  q")
    print("|             / \\")
    print("|          __/   \\__")
    print("|")
    print("|_____")


def draw_gallows():
    print("|---------------")
    print("| /            |")
    print("|/              ")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|_____")


def draw_head():
    print("|---------------")
    print("| /            |")
    print("|/          WWWWWWW")
    print("|           |     |")
    print("|            \\   /")
    print("|              Y")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|_____")


def draw_body():
    print("|---------------")
    print("| /            |")
    print("|/          WWWWWWW")
    print("|           |     |")
    print("|            \\   /")
    print("|              Y")
    print("|              |")
    print("|              |")
    print("|")
    print("|")
    print("|")
    print("|_____")


def draw_legs():
    print("|---------------")
    print("| /            |")
    print("|/          WWWWWWW")
    print("|           |     |")
    print("|            \\   /")
    print("|              Y")
    print("|              |")
    print("|              |")
    print("|             / \\")
    print("|            /   \\")
    print("|")
    print("|_____")


def draw_feets():
    print("|---------------")
    print("| /            |")
    print("|/          WWWWWWW")
    print("|           |     |")
    print("|            \\   /")
    print("|              Y")
    print("|              |")
    print("|              |")
    print("|             / \\")
    print("|          __/   \\__")
    print("|")
    print("|_____")


def draw_arms():
    print("|---------------")
    print("| /            |")
    print("|/          WWWWWWW")
    print("|           |     |")
    print("|            \\   /")
    print("|              Y")
    print("|            / | \\")
    print("|              |")
    print("|             / \\")
    print("|          __/   \\__")
    print("|")
    print("|_____")


def draw_hands():
    print("|---------------")
    print("| /            |")
    print("|/          WWWWWWW")
    print("|           |     |")
    print("|            \\   /")
    print("|              Y")
    print("|            / | \\")
    print("|           p  |  q")
    print("|             / \\")
    print("|          __/   \\__")
    print("|")
    print("|_____")


def draw_ears():
    print("|---------------")
    print("| /            |")
    print("|/          WWWWWWW")
    print("|          <|     |>")
    print("|            \\   /")
    print("|              Y")
    print("|            / | \\")
    print("|           p  |  q")
    print("|             / \\")
    print("|          __/   \\__")
    print("|")
    print("|_____")


def draw_mouth():
    print("|---------------")
    print("| /            |")
    print("|/          WWWWWWW")
    print("|          <|     |>")
    print("|            \\ - /")
    print("|              Y")
    print("|            / | \\")
    print("|           p  |  q")
    print("|             / \\")
    print("|          __/   \\__")
    print("|")
    print("|_____")


def draw_man():
    print("   WWWWWWW")
    print("  <| x x |>")
    print("    \\ - / ")
    print("    \\ - / ")
    print("      Y")
    print("    / | \\")
    print("   p  |  q")
    print("     / \\")
    print("  __/   \\__")


def draw_hangman(hang):
    if hang == 0:
        draw_gallows()
    elif hang == 1:
        draw_head()
    elif hang == 2:
        draw_body()
    elif hang == 3:
        draw_legs()
    elif hang == 4:
        draw_feets()
    elif hang == 5:
        draw_arms()
    elif hang == 6:
        draw_hands()
    elif hang == 7:
        draw_ears()
    elif hang == 8:
        draw_mouth()
    elif hang == 9:
        draw_eyes()


# to only type one char as your guess
def check_letter_len(letter, max_len):
    if len(letter) > max_len:
        return False
    else:
        return True


# checks if input is from alphabet
def check_alpha(input_string):
    if input_string.isalpha():
        return True
    else:
        return False


# input handler
def get_letter():
    global letter
    only_one_letter = True
    while only_one_letter:
        letter = str(input("Gib einen Buchstaben an: "))
        if check_letter_len(letter, 1) is False or check_alpha(letter) is False:
            print("Nur einen Buchstaben!")
        else:
            clear_screen()
            print(f"Dein Buchstabe war: '{letter}'")
            only_one_letter = False
    return letter


# creates word to be guessed
def make_secret_word():
    is_alpha = False
    while is_alpha is False:
        secret_word = str(input("Schreibe das Wort, dass erraten werden soll: "))
        clear_screen()
        if check_alpha(secret_word) is True:
            is_alpha = True
            return secret_word
        else:
            clear_screen()
            print("Du darfst nur Buchstaben schreiben")


# start of game
if __name__ == "__main__":
    clear_screen()
    print("Willkommen bei Hang-man!")
    game_loop = True
    wrong_letters = list()
    while game_loop is True:
        wrong_letters.clear()
        secret_word = make_secret_word()
        slots = "_" * len(secret_word)
        print(f"Wort:  {space_it_out(slots, 1)} ")  # prints only slots for characters
        wrong_count = 0
        game_active = True

        while "_" in slots and game_active:
            letter = get_letter()
            count = 0
            if letter.lower() in secret_word.lower():
                if letter.lower() not in slots.lower():
                    for i in secret_word.lower():
                        if i == letter.lower():
                            correct_letter = letter.lower()
                            position = count
                            if position == 0:
                                if secret_word[0].isupper():
                                    correct_letter = correct_letter.upper()
                            slots = slots[:position] + correct_letter + slots[position + 1:]
                        count += 1
                    print(f"Falsche Buchstaben: {wrong_letters}")
                    print(f"Wort:  {space_it_out(slots, 1)}")
                else:
                    print(f"Du hast '{letter}' bereits erraten")
                    print(f"Falsche Buchstaben: {wrong_letters}")
                    print(f"Wort:  {space_it_out(slots, 1)}")
            else:
                wrong_count += 1
                # draw_hangman(wrong_count)
                print(f"Leider ist '{letter}' nicht im Wort enthalten")
                if letter not in wrong_letters:
                    wrong_letters.append(letter)
                print(f"Falsche Buchstaben: {wrong_letters}")
                print(f"Wort:  {space_it_out(slots, 1)}")
                if wrong_count >= 9:
                    game_active = False
            draw_hangman(wrong_count)
        if "_" in slots:
            print("Du hast leider verloren")
            print(f"Das Wort war '{secret_word}'")
        else:
            print(f"Gewonnen!!! du hast '{secret_word}' erraten")

        loop_leave = False
        while loop_leave is False:
            answer = input("Willst du nochmal spielen(Ja/Nein): ")
            print()
            if "ja" in answer or "Ja" in answer or "JA" in answer:
                game_loop = True
                loop_leave = True
                clear_screen()
                print("Nächste Runde!")
            elif "nein" in answer or "Nein" in answer or "NEIN" in answer:
                game_loop = False
                loop_leave = True
                clear_screen()
            else:
                print("Schreibe ja oder nein!!")

