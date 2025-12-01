import collections

def word_count(filename):
    """Count word frequencies in a text file."""
    word_freq = collections.Counter()
    with open(filename, 'r') as f:
        for line in f:
            words = line.strip().split()
            word_freq.update(words)
    return word_freq

if __name__ == "__main__":
    freq = word_count('corpus_1MB.txt')
    print("Top 10 words:", freq.most_common(10))
