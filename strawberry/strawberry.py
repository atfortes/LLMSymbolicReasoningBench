import argparse
import json
import os
import random

def main():
    parser = argparse.ArgumentParser(description="Generate 'strawberry' letter-count dataset.")
    parser.add_argument("--input_path", type=str, default="words.json")
    parser.add_argument("--random_seed", type=int, default=0)
    parser.add_argument("--dataset_size", type=int, default=10)
    parser.add_argument("--data_dir", type=str, default=".")
    parser.add_argument("--file_name", type=str, default="strawberry")
    args = parser.parse_args()

    random.seed(args.random_seed)

    word_list = []
    with open(args.input_path, "r") as f:
        word_list = json.load(f)

    samples = []
    for _ in range(args.dataset_size):
        word = random.choice(word_list)
        letter = random.choice(word)
        question = f"How many '{letter}' are there in the word '{word}'?"
        count = word.count(letter)

        samples.append({
            "question": question,
            "answer": str(count)
        })

    out_path = os.path.join(args.data_dir, args.file_name + ".json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(samples, f, indent=4)

    print(f"Dataset generated and saved at: {out_path}")

if __name__ == "__main__":
    main()
