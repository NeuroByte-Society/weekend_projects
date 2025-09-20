import time

"""Create a new folder: your_name/typing_speed_tester/
Add main script: typing_speed_tester.py
Include a sample prompt in code (or load from prompts.txt)
Display the prompt clearly and start timing when user begins typing
Stop timing when user submits input (e.g., presses Enter)

Calculate:
Time taken (seconds)
WPM using: WPM = (characters_typed / 5) / minutes_elapsed
Accuracy (%) using: accuracy = (correct_chars / total_chars_typed) * 100
Print a neat summary with:

Prompt length (chars & words)
Time taken
WPM
Accuracy

Add README.md explaining:

What the project does
How to run it
Example input/output

(Optional) Add requirements.txt (if you use any libraries)"""
def typing_speed_test():
    # WPM = (characters_typed / 5) / minutes_elapsed
    # accuracy = (correct_chars / total_chars_typed) * 100

    print("Type this sentence as fast as you can!")

    prompt1 = "The quick brown fox jumps over the lazy dog."
    prompt2 = "Despite the heavy rain, Julia sprinted across the crowded street—dodging cars, " \
                "splashing through puddles, and laughing the entire way."
    
    print(prompt1)
    
    start = time.time()
    typing = input(">>> ")
    end = time.time()


typing_speed_test()
    


    