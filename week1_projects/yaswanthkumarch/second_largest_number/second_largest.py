def second_largest(numbers):
    unique = list(set(numbers))  # Remove duplicates
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, user_input.strip().split()))
        result = second_largest(numbers)
        if result is not None:
            print("Second Largest:", result)
        else:
            print("List doesn't have enough unique numbers.")
    except ValueError:
        print("Please enter valid integers only.")
