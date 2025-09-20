import time

def typing_speed_test():
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

    if secs1 < 10 and accuracy1 > 80:
        print("You're ready for a harder challenge!")
        print("\nvvv Type this sentence as fast as you can! vvv\n   ----------------------------------------")
        print(f"{prompt2}\n   ----------------------------------------")
        
        start2 = time.time()
        typed_response2 = input(">>> ")
        end2 = time.time()

        secs2 = end2 - start2

        accuracy2 = accuracy_checker(prompt2, typed_response2)

        print(f"It took you, {secs2:.2f} seconds!")
        print(f"Your accuracy: {accuracy2:.2f}%")

def accuracy_checker(prompt:str, user_input:str):
    correct_char = 0

    prompt_strip = prompt.strip()
    user_input_strip = user_input.strip()
    
    for i in range(min(len(prompt_strip), len(user_input_strip))):
        if prompt_strip[i] == user_input_strip[i]:
            correct_char += 1
    
    accuracy = (correct_char / len(prompt)) * 100

    return accuracy

typing_speed_test()