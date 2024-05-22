import random
import sys

def main():
    creatures = [
        ["Minotaur", "gored", 7, 1, 6, 2, "Giant rat", "bit", 1, 4, 0],
        ["Gremlin", "speared", 1, 8, 5, "Ghoul", "touched", 3, 6, 2],
        ["Hydra", "bit", 5, 3, 5, "Manticore", "clawed and bit", 6, 2, 4],
        ["White dragon", "froze", 3, 6, 7, "Acolyte", "thumped", 1, 6, 9],
        ["Troll", "bit and clawed", 6, 2, 2, "Ogre", "clubbed", 5, 8, 8],
        ["Cyclops", "thumped", 15, 3, 8, 6],
        ["Salamander", "scorched", 2, 6, 2, "Goblin", "wounded", 1, 8, 5],
        ["Skeleton", "mace'd", 1, 6, 8],
        ["Zombie", "hit", 3, 3, 6, 6, "Giant scorpion", "stung", 4, 3, 8],
        ["Orc", "sliced", 2, 8, 4, "Mummy", "paralysed", 4, 2, 6, "Hobgoblin", "thumped", 3, 6, 9],
        ["Hell hound", "burnt", 4, 3, 6, "Chimera", "hit", 9, 3, 4],
        ["Wyvern", "stung and burnt", 7, 2, 4, "Stone Golem", "hit", 9, 8, 2],
        ["Bone Golem", "mutilated", 7, 2, 4],
        ["Hill giant", "squashed", 3, 8, 7],
        ["Bugbear", "stabbed", 3, 8],
        ["Gargoyle", "fanged", 4, 16, 5, "Harpy", "charmed and bit", 4, 3, 5],
        ["Sirine", "drunk", 1, 3, 1],
        ["Warlord", "slashed", 5, 8, 10, "Priest", "maced", 4, 6, 5],
        ["Assassin", "stabbed", 3, 6, 7, "Unicorn", "horned", 3, 8, 4],
        ["Mad dog", "bit", 5, 8, 6, "Storm giant", "electrocuted", 18, 5],
        ["Gnome", "hit", 1, 6, 5, "Elf", "sliced", 2, 10, 8, "Thief", "stabbed", 1, 4, 8, 7],
        ["Owl bear", "hugged", 5, 3, 5, "Werebear", "hugged", 5, 4, 5, 4, 2],
        ["Roc", "Pecked", 6, 8, 22, "Cleric", "baptised", 2, 6, 8, 2],
        ["Dwarf", "thumped", 4, 6, 2, "Halfling", "sliced", 1, 4, 5],
        ["Hobbit", "slashed", 1, 4, 6, 5, 2, "Centaur", "knocked", 6, 8, 20],
        ["Hippogriff", "Pecked", 3, 8, 22, 5, "Dwarven hero", "chopped"],
        ["Super-hero", "sliced", 8, 6, 10, 1, "Master thief", "stabbed", 9, 4, 4, 2],
        ["Brass dragon", "breathed on", 8, 8, 30, 2, "Pegasus", "bit", 2, 8, 16, 6],
        ["Giant hawk", "Pecked", 3, 8, 6, "Blink dog", "gnawed", 4, 3, 6, 2],
        ["Lawful Goblin", "struck", 1, 8, 8, 7],
        ["Giant weasel", "bit", 4, 8, 7, "Bard", "sung to", 3, 6, 6, "Druid", "sickled", 4, 6, 45]
    ]

    experience_points = 0
    num_creatures = 30
    player_creatures = [{"name": c[0], "action": c[1], "strength": c[2], "health": c[3]} for c in creatures]
    computer_creatures = [{"name": c[5], "action": c[6], "strength": c[7], "health": c[8]} for c in creatures]
    player_experience = [0] * num_creatures
    computer_experience = [0] * num_creatures

    print("INSTRUCTIONS")
    print("You are the leader of a small band of weird characters whose job is to eliminate a group of evil creatures who are killing and destroying everything in their path. You have found them in the arena of vulcan and you fight them one by one. The computer chooses first and then you enter in the number corresponding to your choice. You both start off with 30 creatures and the first party to be killed off loses.")

    input("Press any key to start...")
    print("Your cleric and priest can turn the undead (mummy, skeleton, ghoul, and the zombie) see if they are lucky.")
    print("You start off with 0 experience points but if you kill a strong creature with a weaker creature you gain points (you lose points for the reverse). Good luck.")

    def choose_creature():
        return random.randint(0, num_creatures - 1)

    def battle(player, computer):
        nonlocal experience_points
        print(f"Your {player['name']} {player['action']} the {computer['name']}")
        if player['strength'] > computer['strength']:
            experience_points += (player['strength'] - computer['strength'])
            print(f"You won! Your {player['name']} has gained experience points.")
            return True
        elif player['strength'] < computer['strength']:
            experience_points -= (computer['strength'] - player['strength'])
            print(f"You lost! Your {player['name']} has lost experience points.")
            return False
        else:
            print("It's a tie! No points gained or lost.")
            return None

    def play_game():
        for round in range(num_creatures):
            computer_choice = choose_creature()
            computer_creature = computer_creatures[computer_choice]
            while computer_creature["health"] <= 0:
                computer_choice = choose_creature()
                computer_creature = computer_creatures[computer_choice]

            print(f"Computer chooses: {computer_creature['name']}")

            player_choice = int(input("Enter the number of your creature (1-30): ")) - 1
            player_creature = player_creatures[player_choice]
            while player_creature["health"] <= 0:
                print("This creature is already dead. Choose another one.")
                player_choice = int(input("Enter the number of your creature (1-30): ")) - 1
                player_creature = player_creatures[player_choice]

            result = battle(player_creature, computer_creature)
            if result is True:
                computer_creature["health"] -= 1
            elif result is False:
                player_creature["health"] -= 1

            if all(c["health"] <= 0 for c in player_creatures):
                print("All your creatures are dead. You lose!")
                break
            if all(c["health"] <= 0 for c in computer_creatures):
                print("All computer creatures are dead. You win!")
                break

    play_game()

if __name__ == "__main__":
    main()
