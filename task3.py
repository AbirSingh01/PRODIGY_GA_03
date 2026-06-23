import os
import markovify

# Get the path of sample.txt
file_path = os.path.join(os.path.dirname(__file__), "sample.txt")

# Read the text file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Create Markov model
model = markovify.Text(text, state_size=1)

print("\nGenerated Text:\n")

# Generate 5 sentences
count = 0
while count < 5:
    sentence = model.make_short_sentence(100)
    if sentence:
        count += 1
        print(f"{count}. {sentence}")