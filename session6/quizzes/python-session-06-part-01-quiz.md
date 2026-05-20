# Session 6 Part 1 Quiz (Mutex Basics)

## Question 1

What is a mutex mainly used for?

- Running code faster automatically
- Allowing only one worker into a critical section
- Downloading files from the internet
- Creating random numbers

Answer: 2
Type: single
Time: 40
Explanation: A mutex protects shared resources by allowing one worker at a time into the protected code.

## Question 2

In Python, which object is commonly used as a mutex in this session?

- `random.choice`
- `requests.get`
- `time.perf_counter`
- `threading.Lock`

Answer: 4
Type: single
Time: 40
Explanation: `threading.Lock` is used to protect critical sections.

## Question 3

What is a critical section?

- A comment at the top of a file
- A list of URLs
- Code that must be protected because it uses shared state
- A package installation command

Answer: 3
Type: single
Time: 45
Explanation: Critical sections are parts of code where shared resources are accessed and need coordination.

## Question 4

Why should multiple threads writing to one file be coordinated?

- Threads cannot open files
- Output can become mixed, lost, or difficult to trust
- Python files can only contain one line
- File writing is always CPU-bound

Answer: 2
Type: single
Time: 45
Explanation: Uncoordinated writes can cause confusing or incorrect output.

## Question 5

What does `with lock:` do?

- Enters a protected block and releases the lock when done
- Deletes the lock
- Converts a thread into a process
- Starts all waiting threads at once

Answer: 1
Type: single
Time: 45
Explanation: The context manager acquires the lock, runs the block, and releases the lock.

## Question 6

Why is the shared counter example protected by a lock?

- The counter is a network request
- Locks make integers larger
- `ThreadPoolExecutor` cannot run without a lock
- Reading and updating the counter should happen as one safe operation

Answer: 4
Type: single
Time: 50
Explanation: The read-update-write sequence should not be interrupted by another worker.

## Question 7

What does `Faker` help with in Exercise 1?

- Starting threads automatically
- Locking files
- Generating fake sentences for practice
- Measuring runtime

Answer: 3
Type: single
Time: 40
Explanation: `Faker` generates fake text so the exercise can focus on safe file writing.

## Question 8

Which line generates a short fake sentence?

- `fake.sentence(nb_words=6)`
- `fake.lock(nb_words=6)`
- `threading.sentence(6)`
- `write_lock.sentence()`

Answer: 1
Type: single
Time: 40
Explanation: `fake.sentence(nb_words=6)` asks Faker for a short fake sentence.

## Question 9

In the phrase exercise, what should be inside the lock-protected block?

- The whole program from top to bottom
- The import statements
- The `pip install` command
- Only the shared file-writing section

Answer: 4
Type: single
Time: 45
Explanation: Keep the critical section small and protect the shared file write.

## Question 10

What is a race condition?

- A faster version of a loop
- A bug caused by unpredictable timing between workers
- A type of fake sentence
- A completed quiz

Answer: 2
Type: single
Time: 45
Explanation: Race conditions happen when worker timing affects shared-state behavior.
