"""Dice simulator."""

import random

def roll_die():
    return random.randit(1,6)

print("Dice simulator")
print(f"Rolled: {roll_die}")