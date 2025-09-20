import time

def typing_speed_test():
    start = input("\nWelcome to the typing test!\nPress 'enter' to start! ")

    print("\nvvv Type this sentence as fast as you can! vvv\n   ----------------------------------------")

    prompt1 = "The quick brown fox jumps over the lazy dog."
    prompt2 = "Despite the heavy rain, Julia sprinted across the crowded street—dodging cars, " \
                "splashing through puddles, and laughing the entire way."
    
    print(f"{prompt1}\n   ----------------------------------------\n")

    start1 = time.time()
    typed_response1 = input(">>> ")
    end1 = time.time()

    secs1 = (end1 - start1)

    accuracy1 = accuracy_checker(prompt1, typed_response1)

    print(f"It took you, {secs1:.2f} seconds!")
    print(f"Your accuracy: {accuracy1:.2f}%")

    if secs1 < 12 and accuracy1 > 60:
        start = input("\nYou're ready for a harder challenge!\nPress 'enter' to start! ")
        print("\nvvv Type this sentence as fast as you can! vvv\n   ----------------------------------------")
        print(f"{prompt2}\n   ----------------------------------------")
        
        start2 = time.time()
        typed_response2 = input(">>> ")
        end2 = time.time()

        secs2 = end2 - start2

        accuracy2 = accuracy_checker(prompt2, typed_response2)

        print(f"It took you, {secs2:.2f} seconds!")
        print(f"Your accuracy: {accuracy2:.2f}%\n Great job!")
        

    else:
        print("\nNot too bad try again and get better results for a harder challenge!")

def accuracy_checker(prompt:str, user_input:str):
    """
    Returns accuracy as the percentage of characters in the prompt 
    that match the user's input (position by position).
    """
    prompt_words = prompt.strip().split()
    user_words = user_input.strip().split()
    
    correct_words = sum(1 for p, u in zip(prompt_words, user_words) if p == u)
    accuracy = (correct_words / len(prompt_words)) * 100 if len(prompt_words) > 0 else 0.0

    return accuracy

typing_speed_test()