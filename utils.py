"""
utils.py
---------
Utility functions for the Movie Recommendation System.
"""

from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


def display_banner():
    """Displays the project banner."""

    print(Fore.CYAN + "=" * 65)
    print(Fore.YELLOW + "         🎬 MOVIE RECOMMENDATION SYSTEM")
    print(Fore.CYAN + "=" * 65)
    print(Fore.GREEN + "Find the perfect movie based on your favorite genre!")
    print(Fore.CYAN + "=" * 65)
    print()


def display_genres():
    """Displays all available movie genres."""

    print(Fore.MAGENTA + "Available Genres:\n")

    genres = [
        "Action",
        "Comedy",
        "Drama",
        "Horror",
        "Romance",
        "Science Fiction",
        "Animation",
        "Thriller",
        "Fantasy",
        "Adventure"
    ]

    for genre in genres:
        print(Fore.YELLOW + f"• {genre}")

    print()


def print_movies(movie_list):
    """Displays recommended movies."""

    print(Fore.GREEN + "\n🎥 Recommended Movies:\n")

    for i, movie in enumerate(movie_list, start=1):
        print(Fore.WHITE + f"{i}. {movie}")

    print()


def invalid_genre():
    """Displays an error message for invalid genres."""

    print(
        Fore.RED
        + "\n❌ Sorry! That genre is not available."
    )

    print(
        Fore.CYAN
        + "Please choose a genre from the available list.\n"
    )