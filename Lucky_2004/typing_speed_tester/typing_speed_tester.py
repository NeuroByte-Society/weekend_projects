import time
import random
import os


def get_prompt():
    """Return a typing prompt (from file if available, else fallback)."""
    prompt_file = "prompts.txt"
    if os.path.exists(prompt_file):
        with open(prompt_file, "r", encoding="utf-8") as f:
            prompts = [line.strip() for line in f if line.strip()]
        return random.choice(prompts)
    else:
        # fallback prompt
        return "The quick brown fox jumps over the lazy dog."


def measure_time_and_input(prompt):
    """Show prompt, measure typing time, and capture user input."""
    print("\nPrompt:\n")
    print(f"\"{prompt}\"\n")
    input("Press Enter when ready to start typing...")

    start = time.perf_counter()
    typed_text = input("\nStart typing and press Enter when done:\n> ")
    end = time.perf_counter()

    elapsed = end - start
    return typed_text, elapsed


def calculate_metrics(prompt, typed_text, elapsed):
    """Calculate WPM and accuracy."""
    # Time in minutes
    minutes = elapsed / 60

    # WPM = (characters_typed / 5) / minutes_elapsed
    characters_typed = len(typed_text)
    wpm = (characters_typed / 5) / minutes if minutes > 0 else 0

    # Accuracy = correct_chars / total_chars_typed
    correct_chars = sum(1 for p, t in zip(prompt, typed_text) if p == t)
    accuracy = (correct_chars / characters_typed * 100) if characters_typed > 0 else 0

    return {
        "time": elapsed,
        "wpm": wpm,
        "accuracy": accuracy,
        "prompt_length_chars": len(prompt),
        "prompt_length_words": len(prompt.split()),
    }


def show_summary(metrics):
    """Print results in a neat format."""
    print("\n--- Results ---")
    print(f"Prompt length: {metrics['prompt_length_chars']} chars, {metrics['prompt_length_words']} words")
    print(f"Time taken: {metrics['time']:.2f} seconds")
    print(f"WPM: {metrics['wpm']:.2f}")
    print(f"Accuracy: {metrics['accuracy']:.2f}%")
    print("----------------\n")


def main():
    prompt = get_prompt()
    typed_text, elapsed = measure_time_and_input(prompt)
    metrics = calculate_metrics(prompt, typed_text, elapsed)
    show_summary(metrics)


if __name__ == "__main__":
    main()
