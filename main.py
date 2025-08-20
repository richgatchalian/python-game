# features: add GUI, payment methods, etc
import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# get this


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# get this


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copy of all_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def display_slot(columns):
    for row in range(len(columns[0])):  # first column (must have)
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        value = input("Enter the amount to deposit: ")
        if value.isdigit():
            value = int(value)
            if value > 0:
                print(f"Deposited: {value}")
                break
            else:
                print("Deposit amount must be positive.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return value


def get_num_lines():
    while True:
        num_lines = input(
            "enter the number of lines (1 to " + str(MAX_LINES) + "): ")
        if num_lines.isdigit():
            num_lines = int(num_lines)
            if 0 < num_lines <= MAX_LINES:
                print("You have selected " + str(num_lines) + " amount of lines")
                break
            else:
                print("The value is out of bounds")
        else:
            print("Enter a numeric value")
    return num_lines


def get_bet():
    while True:
        bet = input("Enter the amount to bet: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return bet


def spins(balance):
    lines = get_num_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet < balance:
            print(
                f"You are betting {bet} on {lines} lines. The total bet is {total_bet}")
            break
        else:
            print(
                f"You do not have enough balance. Your current balance is {balance}")

    slot = get_spin(ROWS, COLS, symbols_count)
    display_slot(slot)
    winnings, winning_lines = check_winnings(slot, lines, bet, symbols_value)
    print(f"You won {winnings} on lines: {winning_lines}")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is {balance}")
        ans = input("press enter to play (x to quit)")
        if ans == "x":
            break
        balance += spins(balance)

    print(f"You left with {balance}")


main()
