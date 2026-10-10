"""Choose Your Own Adventure: a mysterious forest story.

Run the game with: python3 game.py
"""


def choose_option(prompt, options):
    """Show numbered options and return the number of a valid choice."""
    print(f"\n{prompt}")
    for number, option in enumerate(options, start=1):
        print(f"  {number}. {option}")

    while True:
        answer = input("Enter the number of your choice: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer)
        print(f"Please enter a number from 1 to {len(options)}.")


def show_ending(title, message):
    """Display the ending reached by the player's choices."""
    print(f"\n--- {title} ---")
    print(message)


def play_adventure():
    """Play one journey through the mysterious forest."""
    print("\n" + "=" * 48)
    print("          CHOOSE YOUR OWN ADVENTURE")
    print("=" * 48)
    print(
        "At dusk, you discover a narrow path into the Whispering Forest. "
        "Silver leaves shimmer overhead, and something far away calls your name."
    )

    first_choice = choose_option(
        "Where will you go?",
        ["Enter a dark cave", "Cross the rushing river", "Follow a mysterious light"],
    )

    if first_choice == 1:
        print(
            "\nThe cave breathes out cool air. Blue crystals glow along its walls, "
            "and a narrow tunnel disappears into darkness."
        )
        cave_choice = choose_option(
            "What do you do?",
            ["Take one glowing crystal", "Follow the narrow tunnel"],
        )
        if cave_choice == 1:
            show_ending(
                "VICTORY: THE FOREST LIGHTS THE WAY",
                "The crystal sings in your hand. Its light reveals a hidden spring, "
                "and you carry its healing water back to the thirsty forest. "
                "By dawn, flowers cover the trail and the forest welcomes you as a friend.",
            )
        else:
            show_ending(
                "LOST IN THE CAVE",
                "The tunnel twists until every passage looks the same. Your footsteps "
                "fade beneath the mountain, and the forest keeps its secret.",
            )

    elif first_choice == 2:
        print(
            "\nThe river is cold and quick. On the far bank, a small wooden cabin "
            "glows warmly between the trees."
        )
        river_choice = choose_option(
            "How will you cross?",
            ["Step carefully across the flat stones", "Build a raft from fallen branches"],
        )
        if river_choice == 1:
            print(
                "\nYou reach the far bank safely. An old forest guardian waits "
                "beside the cabin and offers you a place by the fire."
            )
            guardian_choice = choose_option(
                "What will you tell the guardian?",
                ["Stay and learn to protect the forest", "Thank them and head home"],
            )
            if guardian_choice == 1:
                show_ending(
                    "A NEW BEGINNING",
                    "The guardian teaches you to read the stars and listen to the trees. "
                    "Years later, travelers find their way through the forest by following your lantern.",
                )
            else:
                show_ending(
                    "A SAFE JOURNEY HOME",
                    "The guardian points out a dry trail beyond the cabin. You return home "
                    "with a story no one quite believes, and a tiny silver leaf in your pocket.",
                )
        else:
            show_ending(
                "SWEPT DOWNSTREAM",
                "The current catches your raft before you can climb aboard. You grab a "
                "low branch and scramble to shore, but your supplies are gone and night is falling.",
            )

    else:
        print(
            "\nThe light dances between the trees. It belongs to a tiny fox with "
            "a star-shaped glow caught in the thorns around its paw."
        )
        light_choice = choose_option(
            "What will you do?",
            ["Gently free the fox", "Keep following the light alone"],
        )
        if light_choice == 1:
            show_ending(
                "VICTORY: A FRIEND IN THE FOREST",
                "The fox is free! It races ahead, then leads you to a hidden gate "
                "out of the forest. The grateful forest creatures cheer as you pass through.",
            )
        else:
            show_ending(
                "THE LIGHT FADES",
                "The light grows dimmer with every step until the path disappears. "
                "You find shelter beneath a great tree and promise to choose kindness next time.",
            )


def ask_to_replay():
    """Ask for a yes-or-no answer without accepting unclear input."""
    while True:
        answer = input("\nWould you like to play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def main():
    """Repeat adventures until the player chooses to stop."""
    while True:
        play_adventure()
        if not ask_to_replay():
            print("\nThanks for exploring the Whispering Forest. Goodbye!")
            break


if __name__ == "__main__":
    main()