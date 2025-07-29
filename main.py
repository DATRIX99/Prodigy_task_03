import random

def build_markov_chain(text, n=1):
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)

    return markov_chain

def generate_text(chain, length=50, n=1):
    key = random.choice(list(chain.keys()))
    result = list(key)

    for _ in range(length - n):
        next_words = chain.get(key)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        key = tuple(result[-n:])

    return ' '.join(result)

if __name__ == "__main__":
    with open("data.txt", "r") as f:
        input_text = f.read()

    chain = build_markov_chain(input_text, n=1)
    generated = generate_text(chain, length=100)
    print("\nGenerated Text:\n")
    print(generated)
