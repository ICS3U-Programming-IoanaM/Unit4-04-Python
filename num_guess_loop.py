#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Nov. 19, 2022
# guess the random number


import random


def main():
    # variables
    rand_num = random.randint(1, 10)

    while True:
        # gets user input
        user_num_string = input("Guess an integer from 1 to 10: ")

        # converts user input to int
        try:
            user_num_int = int(user_num_string)

        # if user input was not an integer
        except Exception:
            print("Input invalid! Please enter an integer within the specified range!")

        # user input is an integer
        else:
            # user num is out of range
            if user_num_int < 1 or user_num_int > 10:
                print(
                    "Input invalid! Please enter an integer within the specified range!"
                )

            # user input is in range
            else:
                # user guessed correctly
                if user_num_int == rand_num:
                    print(f"Correct! {user_num_int} is the right number!")
                    break

                # user guessed incorrectly
                else:
                    print(f"{user_num_int} is not the right number. Try again.")


if __name__ == "__main__":
    main()
