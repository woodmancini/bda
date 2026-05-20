### Session 6 | Part 2

> In Part 2, you will learn how semaphores limit concurrent work when many tasks share a restricted resource.

#### 1. Goal

You will:

- explain the difference between a mutex and a semaphore
- use `threading.Semaphore` to limit concurrent work
- simulate many workers sharing only a few available passes
- limit web-style calls to 4 active calls at a time
- protect shared result-file writing

#### 2. Prerequisites

From the `session6` folder:

1. Activate your virtual environment.

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

2. Install dependencies if needed:

```bash
pip install -r requirements.txt
```

#### 3. Basics you should know

- semaphore: a counter-based lock that allows up to N workers at the same time
- permit: one available slot in a semaphore
- concurrency limit: the maximum number of workers allowed to do something at once
- I/O-bound work: work that spends time waiting on input/output, such as network calls

#### 4. Semaphore with `threading.Semaphore`

A semaphore is useful when several workers are allowed to run at the same time, but there is still a limit.

Example:

```python
import threading

limit = threading.Semaphore(4)

with limit:
    # at most 4 threads can run this block at the same time
    print("limited shared work")
```

A mutex is like a room with one key.
A semaphore is like a room with a fixed number of passes.

Checkpoint question:

If you have 40 tasks but a semaphore limit of 4, how many tasks can be inside the protected block at once?

<details>
<summary>Show answer</summary>

At most 4 tasks can be inside the protected block at the same time. The other tasks wait until one of the 4 leaves.

</details>

#### 5. Simple semaphore example

Before simulating web calls, try a tiny example where five workers share only two available passes.

Create this warm-up file:

```txt
session6/solutions/exercise-06-00-semaphore.py
```

Add this code:

```python
from concurrent.futures import ThreadPoolExecutor
import threading
import time


door_limit = threading.Semaphore(2)


def enter_room(worker_name):
    print(f"{worker_name} is waiting to enter")

    with door_limit:
        print(f"{worker_name} entered")
        time.sleep(1)
        print(f"{worker_name} left")


if __name__ == "__main__":
    workers = ["Worker A", "Worker B", "Worker C", "Worker D", "Worker E"]

    with ThreadPoolExecutor(max_workers=5) as executor:
        for worker in workers:
            executor.submit(enter_room, worker)
```

Run:

```bash
python3 solutions/exercise-06-00-semaphore.py
```

What this shows:

1. Five workers are submitted.
2. Only two workers can enter the protected block at the same time.
3. When one worker leaves, another waiting worker can enter.

<details>
<summary>Show explanation</summary>

`threading.Semaphore(2)` starts with two available permits. Each worker takes one permit when entering `with door_limit:` and returns it when leaving the block.

</details>

#### 6. Exercise 2: Simulate 40 web calls with a limit of 4

Create this file and complete it:

```txt
session6/solutions/exercise-06-02.py
```

Your program should:

1. Emulate 40 web calls.
2. Use `requests` to make a small HTTP request for each task.
3. Use a semaphore so only 4 calls are active at the same time.
4. Save one result line per call into `request_results.txt`.
5. Print clear start/finish messages.
6. Measure total runtime with `time.perf_counter()`.

> [!TIP]
>
> `httpbin.org` is a small HTTP testing service. The `/delay/1` endpoint waits about 1 second before responding, which makes it useful here because you can clearly see the semaphore limiting how many calls run at the same time.

Use this URL pattern:

```python
url = f"https://httpbin.org/delay/1?request={request_id}"
```

Network note:

- This exercise depends on internet access (`httpbin.org`).
- If a request fails, record the failure and continue.
- If your network is unavailable, you may temporarily replace the request with `time.sleep(1)` while testing the semaphore behavior.

Suggested skeleton:

```python
from concurrent.futures import ThreadPoolExecutor
import threading
import time

import requests


call_limit = threading.Semaphore(4)
write_lock = threading.Lock()


def fetch(request_id):
    url = f"https://httpbin.org/delay/1?request={request_id}"

    # TODO: use call_limit to allow only 4 active requests
    # TODO: call requests.get(url, timeout=10)
    # TODO: write one result line to request_results.txt
    ...


if __name__ == "__main__":
    start = time.perf_counter()

    # TODO: clear request_results.txt
    # TODO: run 40 fetch tasks using ThreadPoolExecutor
    ...

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f}s")
```

Run:

```bash
python3 solutions/exercise-06-02.py
```

Minimum completion checklist:

1. Exactly 40 tasks are attempted.
2. At most 4 requests are active at the same time.
3. Results are written to `request_results.txt`.
4. Failures are recorded instead of crashing the whole program.

<details>
<summary>Show hint</summary>

Use `with call_limit:` around the actual request. Use a separate `write_lock` for writing to the output file, because limiting requests and protecting file writes are two different coordination problems.

</details>

<details>
<summary>Show expected idea</summary>

With 40 one-second request-like tasks and a limit of 4, the runtime should often feel closer to 10 waves of work than 40 fully serial waits. Real network timing varies, so focus on whether the limit is respected and all results are recorded.

</details>

#### 7. Quiz

```bash
quizmd quizzes/python-session-06-part-02-quiz.md
```
