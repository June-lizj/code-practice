# 魔术师换牌问题
if __name__ == "__main__":
    def return_card():
        global display_cards
        global original_cards
        card = display_cards.pop()
        original_cards.insert(0,card)

    def change_order():
        global display_cards
        global original_cards
        card = original_cards.pop()
        original_cards.insert(0,card)

    def one_turn():
        global display_cards
        return_card()
        if len(display_cards) != 0:
            change_order()

    # original_cards = [1,2,3,4,5,6,7]
    display_cards = [1,3,5,7,4,2,6]
    original_cards = []
    while len(display_cards) != 0:
        one_turn()
    print(original_cards)