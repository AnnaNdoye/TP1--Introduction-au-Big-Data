import os
import random
import string

def generate_random_word(length=5):
    """Generate a random word of given length."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_corpus(size_mb, filename):
    """Generate a text file of approximately size_mb MB with random words."""
    size_bytes = size_mb * 1024 * 1024
    current_size = 0
    with open(filename, 'w') as f:
        while current_size < size_bytes:
            num_words = random.randint(5, 15)
            line = ' '.join(generate_random_word() for _ in range(num_words)) + '\n'
            f.write(line)
            current_size += len(line.encode('utf-8'))

sizes = [1, 5, 10, 20, 50]
for size in sizes:
    filename = f'corpus_{size}MB.txt'
    generate_corpus(size, filename)
    print(f'Generated {filename}')
