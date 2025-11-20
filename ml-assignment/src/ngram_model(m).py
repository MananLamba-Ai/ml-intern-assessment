import random
import re

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        self.trigrams = {}
        self.bigrams = {}

    def fit(self, text):
        """
        Trains the trigram model on the given text.

        Args:
            text (str): The text to train the model on.
        """
        # 1. Clean the text
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)

        # 2. Tokenize
        words = text.split()

        # 3. Pad with start and end tokens
        words = ['<s>', '<s>'] + words + ['</s>']

        # 4. Count trigrams and bigrams
        for i in range(len(words) - 2):
            w1, w2, w3 = words[i], words[i+1], words[i+2]
            self.bigrams[(w1, w2)] = self.bigrams.get((w1, w2), 0) + 1
            self.trigrams[(w1, w2, w3)] = self.trigrams.get((w1, w2, w3), 0) + 1

    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.

        Args:
            max_length (int): The maximum length of the generated text.

        Returns:
            str: The generated text.
        """
        result = ['<s>', '<s>']

        for _ in range(max_length):
            w1, w2 = result[-2], result[-1]
            candidates = {w3: count for (a, b, w3), count in self.trigrams.items() if a == w1 and b == w2}

            if not candidates:
                break

            # Randomly choose next word based on frequency
            total = sum(candidates.values())
            r = random.randint(1, total)
            cumulative = 0
            for word, count in candidates.items():
                cumulative += count
                if r <= cumulative:
                    result.append(word)
                    break

            if result[-1] == '</s>':
                break

        return ' '.join(result[2:-1])  # remove <s> and </s>