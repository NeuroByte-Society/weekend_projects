import time

target_text = "The quick brown fox jumps over the lazy dog"

print("Type the following text:")
print(">>>", target_text)
input("\nPress Enter when you're ready... ")

start = time.time()
typed_text = input("\nStart typing here:\n")
end = time.time()

elapsed_time = end - start
elapsed_minutes = elapsed_time / 60

target_words = target_text.split()
typed_words = typed_text.split()

wpm = len(typed_words) / elapsed_minutes if elapsed_minutes > 0 else 0

matches = 0
for i in range(min(len(typed_text), len(target_text))):
    if typed_text[i] == target_text[i]:
        matches += 1

accuracy = (matches / len(target_text)) * 100

print("\n--- Typing Test Results ---")
print(f"Time taken: {elapsed_time:.2f} seconds")
print(f"Words per minute (WPM): {wpm:.2f}")
print(f"Accuracy: {accuracy:.2f}%")
