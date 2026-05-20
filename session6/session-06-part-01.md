### Session 6 | Part 1

> In Part 1, you will learn how mutexes protect shared resources when multiple workers run at the same time.

#### 1. Goal

You will:

- explain what can go wrong when multiple workers share one resource
- use `threading.Lock` as a mutex
- protect a critical section
- write a small program that safely saves generated phrases to a file

#### 2. Prerequisites

Before starting:

1. In Visual Studio Code terminal, update your local repository.

```bash
git pull origin main
```

If `git pull` fails because of local changes, use one of these paths:

Keep your work (recommended):

```bash
git stash push -m "session6-wip"
git pull origin main
git stash pop
```

Discard your local changes in `session6` only (use with care):

```bash
# Run this only from inside the session6 folder.
# Check first (it should end with `/bda/session6`):
pwd
git fetch origin
git restore --source origin/main --worktree --staged -- .
```

2. Open the `session6` folder in Visual Studio Code and in terminal.
3. Create and activate a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

4. If `requirements.txt` is missing, create it in `session6/` with:

```txt
requests==2.32.3
Faker
quizmd
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

#### 3. Basics you should know

- thread: a lightweight worker that runs inside the same Python process
- shared resource: something multiple workers can access, for example a file
- race condition: a bug caused by workers interacting in an unpredictable order
- mutex: a lock that allows only one worker into a critical section
- critical section: code that must not be interrupted by another worker

#### 4. Mini tutorial: mutex with `threading.Lock`

A mutex is useful when many workers need to use one shared resource.

In Python, we commonly use `threading.Lock()`:

```python
import threading

lock = threading.Lock()

with lock:
    # only one thread can run this block at a time
    print("safe shared work")
```

The `with lock:` block is the critical section. Other threads must wait until the lock is released.

Checkpoint question:

Why should file writing often be protected by a lock?

<details>
<summary>Show answer</summary>

Because multiple workers writing at the same time can create mixed, missing, or confusing output. A lock makes each write section finish before another worker enters it.

</details>

#### 5. Simple lock example

Before writing to a file, try a tiny example where two workers share one counter.

Create this warm-up file:

```txt
session6/solutions/exercise-06-00-lock.py
```

Add this code:

```python
from concurrent.futures import ThreadPoolExecutor
import threading
import time


counter = 0
counter_lock = threading.Lock()


def add_one(worker_name):
    global counter

    print(f"{worker_name} is waiting for the lock")

    with counter_lock:
        print(f"{worker_name} entered the critical section")

        current_value = counter
        time.sleep(0.5)
        counter = current_value + 1

        print(f"{worker_name} updated counter to {counter}")


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(add_one, "Worker A")
        executor.submit(add_one, "Worker B")

    print(f"Final counter value: {counter}")
```

Run:

```bash
python3 solutions/exercise-06-00-lock.py
```

What this shows:

1. Both workers want to update the same shared variable.
2. Only one worker can enter the `with counter_lock:` block at a time.
3. The final counter value should be `2`.

<details>
<summary>Show explanation</summary>

The lock protects the read-update-write sequence. Without the lock, both workers could read the same old value before either one writes the new value, which can produce an incorrect final counter.

</details>

#### 6. Simple Faker example

`Faker` is a Python library that generates fake data for testing and practice.

In this exercise, we use it only to generate simple fake sentences. This keeps the focus on the mutex and file writing, not on building a text generator.

Try this small example first:

```python
from faker import Faker

fake = Faker()

def generate_phrase():
    return fake.sentence(nb_words=6)

print(generate_phrase())
```

Each time you run it, you should see a short fake sentence.

#### 7. Exercise 1: Generate 10 phrases and save them safely

Create this file and complete it:

```txt
session6/solutions/exercise-06-01.py
```

Your program should:

1. Use `Faker` to generate simple fake sentences.
2. Start 10 worker threads.
3. Each worker generates one phrase.
4. Each worker writes its phrase to `generated_phrases.txt`.
5. Use a mutex so only one thread writes to the file at a time.
6. Print a friendly message when each phrase is saved.

Suggested skeleton:

```python
from concurrent.futures import ThreadPoolExecutor
import threading

from faker import Faker


fake = Faker()
write_lock = threading.Lock()


def generate_phrase():
    # TODO: use fake.sentence(...) to return a phrase
    ...


def save_phrase(index):
    phrase = generate_phrase()

    # TODO: use write_lock before writing to generated_phrases.txt
    ...


if __name__ == "__main__":
    # TODO: clear generated_phrases.txt before starting
    # TODO: run 10 workers with ThreadPoolExecutor
    ...
```

Run:

```bash
python3 solutions/exercise-06-01.py
```

Minimum completion checklist:

1. `generated_phrases.txt` is created.
2. The file contains exactly 10 lines.
3. Each line includes a phrase number and generated phrase.
4. File writing is protected by `threading.Lock`.

<details>
<summary>Show hint</summary>

Use `fake.sentence(nb_words=6)` to generate one phrase. Use `with write_lock:` around the file-writing block only, not around the whole phrase generation function.

</details>

<details>
<summary>Show expected shape</summary>

Your output file might look similar to this:

```txt
Phrase 1: Python analyzes logs.
Phrase 2: A worker streams records.
Phrase 3: The model summarizes results.
```

The exact phrases may be different because `Faker` generates fake text.

</details>

#### 8. Quiz

```bash
quizmd quizzes/python-session-06-part-01-quiz.md
```
