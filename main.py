# main.py
from library import initialize_top_players, play_game


def main():
    # Initialize the game
    initialize_top_players()

    while True:
        play_game()

        # Accept various forms of "yes"
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in {"yes", "y", "ye", "yeah", "yess"}:
            print("Thanks for playing! See you next time.")
            break


if __name__ == "__main__":
    main()
