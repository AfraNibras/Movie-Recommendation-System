"""
recommendation.py
-----------------
Movie Recommendation System
Developed using Python
"""

from colorama import Fore, init
from movies import MOVIES
from utils import (
    display_banner,
    display_genres,
    print_movies,
    invalid_genre,
)

# Initialize Colorama
init(autoreset=True)


def recommend_movies():

    display_banner()

    while True:

        display_genres()

        genre = input(Fore.CYAN + "🎯 Enter your favorite genre: ").strip().lower()

        if genre in MOVIES:
            print_movies(MOVIES[genre])

        else:
            invalid_genre()

        choice = input(
            Fore.YELLOW
            + "Would you like another recommendation? (yes/no): "
        ).strip().lower()

        if choice in ["no", "n"]:
            print(
                Fore.GREEN
                + "\n🎬 Thank you for using the Movie Recommendation System!"
            )
            print(Fore.GREEN + "Have a great time watching movies! 🍿\n")
            break

        elif choice not in ["yes", "y"]:
            print(
                Fore.RED
                + "\nInvalid choice. Exiting the program.\n"
            )
            break


if __name__ == "__main__":
    recommend_movies()