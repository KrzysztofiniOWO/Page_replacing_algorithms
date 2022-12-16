import random


class Data:

    def __init__(self):
        """Initialize_class"""

    def create_random_data(self):
        """Create 50 files filled with 100 random numbers every in new line"""
        for number in range(1, 51):
            with open(f"data/{number}.txt", "w") as f:
                for numbers in range(0, 100):
                    f.write(f"{random.randint(1, 15)}\n")
                f.close()
