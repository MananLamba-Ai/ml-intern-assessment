# Evaluation

Please provide a 1-page summary of your design choices for the Trigram Language Model.

This should include:

- How you chose to store the n-gram counts.
- How you handled text cleaning, padding, and unknown words.
- How you implemented the `generate` function and the probabilistic sampling.
- Any other design decisions you made and why you made them.
# Evaluation

## Design Choices for the Trigram Language Model

### N-gram Count Storage
To store n-gram counts efficiently, I used two dictionaries:
- `self.bigrams`: stores counts of word pairs `(w1, w2)`
- `self.trigrams`: stores counts of word triples `(w1, w2, w3)`

This separation allows the model to compute conditional probabilities for the third word given the first two, which is essential for trigram-based generation.

### Text Cleaning, Padding, and Unknown Words
During training (`fit` method), I cleaned the input text by:
- Converting it to lowercase
- Removing punctuation using regular expressions

I then tokenized the text using `split()` and padded it with two start tokens (`<s>`, `<s>`) and one end token (`</s>`). This ensures the model can learn valid sentence boundaries. Unknown words are not explicitly handled in this version; the model assumes training text is representative of the generation domain.

### Generate Function and Probabilistic Sampling
The `generate` method starts with the `<s> <s>` tokens and repeatedly selects the next word based on trigram frequencies. For each `(w1, w2)` context:
- I collect all possible `w3` candidates from `self.trigrams`
- I perform weighted random sampling using cumulative frequency and a random threshold

This approach ensures that more frequent continuations are more likely to be chosen, while still allowing diversity in generation.

### Other Design Decisions
- I avoided external libraries for tokenization and sampling to keep the implementation simple and transparent.
- I used clear comments and modular logic to make the code readable and easy to test.
- The model is designed to be extensible — future improvements could include smoothing, handling unknowns, or integrating with larger corpora.

Overall, the design balances clarity, functionality, and testability, making it suitable for educational and prototyping purposes.
