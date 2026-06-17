import markovify

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

model = markovify.Text(text, state_size=1)

print("Generated Text:\n")

for i in range(5):
    sentence = model.make_short_sentence(100)
    if sentence:
        print(f"{i+1}. {sentence}")