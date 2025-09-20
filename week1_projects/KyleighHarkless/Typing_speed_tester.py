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
    print("Type this sentence as fast as you can!")

    prompt1 = "The quick brown fox jumps over the lazy dog."
    prompt2 = "Despite the heavy rain, Julia sprinted across the crowded street—dodging cars, " \
                "splashing through puddles, and laughing the entire way."
    
    print(prompt1)

    start = time.time()
    typed_response = input(">>> ")
    end = time.time()

    characters_typed = len(typed_response.split())
    WPM = (characters_typed / 5) / (end - start)

    print(f"Words per minute: {WPM:.2f} seconds")
    print(f"Your accuracy: {accuracy_checker(prompt1, typed_response):.2f}%")

    # if WPM < 0.25:
    #     print("You're ready for a harder challenge!")
    #     print(f"{prompt2}\n---------")

def accuracy_checker(prompt:str, user_input:str):
    correct_char = 0
    
    for i in range(min(len(prompt), len(user_input))):
        if prompt[i] == user_input[i]:
            correct_char += 1
    
    accuracy = (correct_char / len(prompt)) * 100

    return accuracy

    










typing_speed_test()
    


    