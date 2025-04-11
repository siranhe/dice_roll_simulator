"""Dice simulator."""

# dice_simulator.py
import random
import argparse

def roll_die(sides=6):
    return random.randint(1, sides)

def roll_multiple_dice(num_dice, sides=6):
    return [roll_die(sides) for _ in range(num_dice)]

def save_results_to_file(results, filename="results.txt"):
    with open(filename, "w") as file:
        file.write("Rolled dice results:\n")
        file.write(", ".join(map(str, results)))
        file.write("\n")

def main():
    parser = argparse.ArgumentParser(description="Dice Simulator")
    parser.add_argument("--sides", type=int, default=6, help="Number of sides on the die")
    parser.add_argument("--num-dice", type=int, default=1, help="Number of dice to roll")
    parser.add_argument("--output", type=str, default="results.txt", help="Output file for results")
    args = parser.parse_args()

    results = roll_multiple_dice(args.num_dice, args.sides)
    print(f"Rolled: {results}")
    save_results_to_file(results, args.output)
    print(f"Results saved to {args.output}")
    print("End of simulation")
    print("Thank you for using the simulator")

if __name__ == "__main__":
    main()