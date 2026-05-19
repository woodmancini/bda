### Session 6 | Optional Mini Project

> This optional mini project gives you extra practice by simulating many print jobs sharing only three available printers.

#### 1. Goal

You will:

- model a limited resource pool
- assign print jobs to whichever printer becomes available
- use parallel execution without allowing more than 3 active print jobs
- produce clear status messages for each job
- reason about fairness, waiting, and shared output

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

#### 3. Project: parallel printer simulation

Imagine an office with many files waiting to print.

There are only 3 printers:

```python
printers = ["Printer-A", "Printer-B", "Printer-C"]
```

There are more files than printers:

```python
print_jobs = [
    "invoice_batch.pdf",
    "student_report.docx",
    "sales_chart.xlsx",
    "meeting_notes.pdf",
    "poster_draft.png",
    "research_summary.pdf",
    "attendance_sheet.csv",
    "budget_plan.xlsx",
    "slides_final.pptx",
    "lab_instructions.pdf",
]
```

Your task is to simulate printing these files in parallel.

Each file should:

1. Wait until a printer is available.
2. Use that printer.
3. Print a clear start message.
4. Sleep for a random short duration to simulate printing.
5. Print a clear finish message.
6. Return the printer so another file can use it.

#### 4. Why a queue is useful here

A semaphore can limit the number of active jobs to 3, but it does not tell you which printer a job received.

For this project, use `queue.Queue` to hold available printer names.

The idea:

```python
from queue import Queue

available_printers = Queue()

for printer in printers:
    available_printers.put(printer)

printer = available_printers.get()

try:
    print(f"Using {printer}")
finally:
    available_printers.put(printer)
```

The queue gives each job one available printer and then receives it back when the job finishes.

Checkpoint question:

Why should the printer be returned in a `finally` block?

<details>
<summary>Show answer</summary>

Because `finally` runs even if the job hits an error. This helps avoid losing a printer from the available pool forever.

</details>

#### 5. Build the project

Create this file and complete it:

```txt
session6/solutions/exercise-06-project.py
```

Suggested skeleton:

```python
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import random
import threading
import time


printers = ["Printer-A", "Printer-B", "Printer-C"]

print_jobs = [
    "invoice_batch.pdf",
    "student_report.docx",
    "sales_chart.xlsx",
    "meeting_notes.pdf",
    "poster_draft.png",
    "research_summary.pdf",
    "attendance_sheet.csv",
    "budget_plan.xlsx",
    "slides_final.pptx",
    "lab_instructions.pdf",
]

message_lock = threading.Lock()


def log(message):
    # TODO: use message_lock so messages do not mix together
    ...


def print_file(filename, available_printers):
    # TODO: get an available printer from the queue
    # TODO: simulate print time with time.sleep(...)
    # TODO: return the printer to the queue
    ...


if __name__ == "__main__":
    available_printers = Queue()

    # TODO: add all printers to the queue
    # TODO: run all jobs with ThreadPoolExecutor
    ...
```

Run:

```bash
python3 solutions/exercise-06-project.py
```

Minimum completion checklist:

1. All 10 files are printed.
2. Only 3 jobs print at the same time.
3. Each job prints which printer it used.
4. Printers become available again after each job.
5. Messages are clear and readable.
6. Total runtime is printed.

<details>
<summary>Show hint</summary>

Set `max_workers=len(print_jobs)` so all jobs are submitted, but only jobs that successfully get a printer from the queue can print. Use `available_printers.get()` before printing and `available_printers.put(printer)` after printing.

</details>

<details>
<summary>Show expected output shape</summary>

Your exact order will vary because jobs run in parallel.

```txt
[WAITING] invoice_batch.pdf is waiting for a printer
[START] invoice_batch.pdf is printing on Printer-A
[WAITING] student_report.docx is waiting for a printer
[START] student_report.docx is printing on Printer-B
[DONE] invoice_batch.pdf finished on Printer-A in 1.42s
```

</details>

#### 6. Questions to answer in comments

Answer briefly in comments at the bottom of your file:

1. Why did we use a queue instead of only a semaphore?
2. What would happen if a printer was never returned to the queue?
3. Why might real print systems need priorities?

#### 7. Quiz

**Quiz 1**

```bash
quizmd quizzes/python-session-06-optional-mini-project-quiz.md
```

**Quiz 2 (Essay)**

```bash
quizmd quizzes/python-session-06-printer-project-essay.md
```
