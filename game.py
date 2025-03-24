import os
import random

dracula_hearts = 12
game_round = 1
num_of_burned_cards = 0
FIRST_SPACES = 8
CARD_LINES = 5
roles_list = ["van helsing", "dracula"]


def create_decree():
    decree = ["🩸", "🕯️", "⚰️", "♰"]
    random.shuffle(decree)
    return decree


def create_deck(deck: list = None):
    if deck is None:
        deck = []
        for sym in create_decree():
            for index in range(8):
                deck.append((index + 1, sym, False))
    random.shuffle(deck)
    return deck


def create_map_game():
    map_game = {}
    for num in range(4):
        map_game[num + 1] = ["  🧑  ", "  🧑  ", "  🧑  ", "  🧑  ", "  🧑  "]
    return map_game


def get_player_info(first_player_role=None):
    input_name = input("enter your name: ")
    if first_player_role is None:
        while True:
            input_rule = input("what role do you want to be (van helsing or dracula): ")
            if input_rule not in roles_list:
                print("that answer was incorrect, please say (van helsing or dracula):")
            else:
                player_data = {
                    "player_name": input_name,
                    "role": input_rule,
                }
                return player_data
    else:
        input_rule = (
            roles_list[1] if first_player_role == roles_list[0] else roles_list[0]
        )
        player_data = {
            "player_name": input_name,
            "role": input_rule,
        }
        return player_data


def print_the_board(map_game, decree, card=None, burned_card=None):
    under_line = "_"
    mines = "-"
    card_str = create_card_str(card)
    burned_card_str = create_card_str(burned_card)
    print((FIRST_SPACES) * " ", under_line * 46)
    for index, row in map_game.items():
        if index == 1:
            print(
                (FIRST_SPACES + 47) * " ",
                f"{decree[0]} = decree //// {decree[1]} > {decree[2]} > {decree[3]}",
            )
            print(FIRST_SPACES * " ", "|", " | ".join(row), "|")
            print(card_str[0], mines * 46, " ", burned_card_str[0])
        elif index == 2:
            print(card_str[1], "|", " | ".join(row), "|", " ", burned_card_str[1])
            print(card_str[2], mines * 46, " ", burned_card_str[2])
        elif index == 3:
            print(card_str[3], "|", " | ".join(row), "|", " ", burned_card_str[3])
            print(card_str[4], mines * 46, " ", burned_card_str[4])
        else:
            print(FIRST_SPACES * " ", "|", " | ".join(row), "|")
    print(FIRST_SPACES * " ", under_line * 46, "\n")


def create_card_str(card, is_turn=False):
    def symbol_to_str(symbol):
        if symbol == "♰":
            return f"|  {symbol}  | "
        return f"| {symbol}  | "

    def is_show_to_str(is_show):
        if is_show:
            return " 👁️ "
        return "    "

    line_up = "/-----\\ "
    middle_line = "|     | "
    middle_line_with_txt = "|*****| "  # کارت مخفی
    line_down = r"\-----/ "
    if card is not None:
        if is_turn or card[2]:
            return [
                line_up,
                f"|  {card[0]}  | ",
                symbol_to_str(card[1]),
                f"| {is_show_to_str(card[2])}| ",
                line_down,
            ]
    return [
        line_up,
        middle_line,
        middle_line_with_txt,
        middle_line,
        line_down,
    ]


def print_player_cards(player_cards, is_turn):
    cards_str = []
    for card in player_cards["cards"]:
        cards_str.append(create_card_str(card, is_turn))
    for line_num in range(CARD_LINES):
        print((FIRST_SPACES + 1) * " ", end=" ")
        for index in range(len(list(enumerate(cards_str)))):
            print(cards_str[index][line_num], end=" ")
        print()


def starting_game():
    # print help game
    decree = create_decree()
    deck = create_deck()
    map_game = create_map_game()
    player_one = get_player_info()
    player_one["cards"] = [deck.pop() for _ in range(5)]
    player_two = get_player_info(player_one["role"])
    player_two["cards"] = [deck.pop() for _ in range(5)]
    print_game(map_game, decree, player_one, player_two)
    return player_one, player_two, decree, deck, map_game


def print_game(map_game, decree, main_player, second_player):
    os.system("cls" if os.name == "nt" else "clear")  # پاک کردن صفحه
    print_player_cards(second_player, False)
    print_the_board(map_game, decree)  # چاپ نقشه بازی
    print_player_cards(main_player, True)


def main():
    player_one, player_two, decree, deck, map_game = starting_game()


if __name__ == "__main__":
    main()
