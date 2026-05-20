from concurrent.futures import ThreadPoolExecutor
import threading

from faker import Faker


fake = Faker()
write_lock = threading.Lock()


def generate_phrase():
    return fake.sentence(nb_words=6)


def save_phrase(index):
    phrase = generate_phrase()

    # Only the shared file write needs the mutex.
    with write_lock:
        with open("generated_phrases.txt", "a", encoding="utf-8") as file:
            file.write(f"Phrase {index}: {phrase}\n")

    print(f"Saved phrase {index}: {phrase}")


if __name__ == "__main__":
    with open("generated_phrases.txt", "w", encoding="utf-8"):
        pass

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(save_phrase, range(1, 11))

    print("Done. Check generated_phrases.txt")
