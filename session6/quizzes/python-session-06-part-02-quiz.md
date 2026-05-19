# Session 6 Part 2 Quiz (Semaphore Basics)

## Question 1

What is a semaphore useful for?

- Making a function recursive
- Sorting strings alphabetically
- Removing the need for error handling
- Allowing up to a fixed number of workers into a block

Answer: 4
Type: single
Time: 45
Explanation: A semaphore controls access by maintaining a limited number of permits.

## Question 2

If a semaphore is created with `threading.Semaphore(4)`, how many threads can enter the protected block at once?

- 1
- 2
- 4
- 40

Answer: 3
Type: single
Time: 35
Explanation: The initial semaphore value gives 4 available permits.

## Question 3

What is a permit in a semaphore?

- A Python file extension
- One available slot that lets a worker enter
- A failed network request
- A random sentence

Answer: 2
Type: single
Time: 40
Explanation: A permit represents one available entry into the semaphore-controlled section.

## Question 4

In the simple semaphore example, why can only two workers enter at once?

- The semaphore is created with 2 permits
- There are only two Python files
- Threads always run in pairs
- `time.sleep(1)` blocks all output forever

Answer: 1
Type: single
Time: 45
Explanation: `threading.Semaphore(2)` allows two workers into the protected block at a time.

## Question 5

Which statement best describes the difference between a mutex and a semaphore?

- A mutex is only for HTTP requests
- A semaphore always allows unlimited workers
- They are unrelated to shared resources
- A mutex allows one worker; a semaphore can allow a fixed number of workers

Answer: 4
Type: single
Time: 50
Explanation: A mutex is one-at-a-time access, while a semaphore can allow N-at-a-time access.

## Question 6

In the request exercise, why do we use a semaphore instead of starting all 40 calls without a limit?

- To make every request fail
- To respect a concurrency limit and avoid overwhelming a service
- To remove the need for URLs
- To stop Python from importing modules

Answer: 2
Type: single
Time: 45
Explanation: The semaphore keeps only a controlled number of requests active at once.

## Question 7

Why might the request exercise still need a separate write lock?

- Locks cannot be used with requests
- Files are always downloaded automatically
- The semaphore limits requests, but file writing is a different shared resource
- A write lock increases network speed

Answer: 3
Type: single
Time: 50
Explanation: Limiting active requests and protecting shared file writes are separate coordination concerns.

## Question 8

If 40 one-second tasks run with a limit of 4, how many waves of work do you expect approximately?

- 1
- 4
- 10
- 40

Answer: 3
Type: single
Time: 45
Explanation: 40 tasks divided into groups of 4 gives about 10 waves, ignoring overhead and network variation.

## Question 9

What should happen if one HTTP request fails?

- Record the failure and continue
- Hide the error silently
- Stop writing all results
- Delete the semaphore

Answer: 1
Type: single
Time: 40
Explanation: A robust parallel task records failures instead of crashing the whole run.

## Question 10

Which line creates a semaphore with four permits?

- `threading.Lock(4)`
- `requests.Semaphore(4)`
- `ThreadPoolExecutor.Semaphore(4)`
- `threading.Semaphore(4)`

Answer: 4
Type: single
Time: 40
Explanation: `threading.Semaphore(4)` creates a semaphore with four available permits.
