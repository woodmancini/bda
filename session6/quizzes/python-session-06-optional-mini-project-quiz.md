# Session 6 Optional Mini Project Quiz (Printer Simulation)

## Question 1

What limited resource is modeled in the printer project?

- CPU temperature
- Available printers
- Python packages
- Git branches

Answer: 2
Type: single
Time: 35
Explanation: The project models many files sharing only three printers.

## Question 2

Why is `queue.Queue` useful for the printers?

- It edits PDF files automatically
- It replaces Python functions
- It guarantees jobs take the same time
- It stores available printer names and gives one to each job

Answer: 4
Type: single
Time: 45
Explanation: The queue holds printer names, so each job can claim one available printer.

## Question 3

What should happen after a print job finishes?

- The printer should be returned to the queue
- The printer should be deleted
- The job should run forever
- All waiting jobs should be cancelled

Answer: 1
Type: single
Time: 40
Explanation: Returning the printer makes it available for another waiting job.

## Question 4

Why is a `finally` block useful in `print_file(...)`?

- It runs only if no errors happen
- It creates new printers
- It helps ensure the printer is returned even if something goes wrong
- It sorts the print jobs

Answer: 3
Type: single
Time: 45
Explanation: `finally` is used for cleanup actions that should happen after success or failure.

## Question 5

If there are 10 print jobs and 3 printers, how many jobs should be actively printing at the same time?

- At most 1
- At most 3
- Exactly 10
- Unlimited

Answer: 2
Type: single
Time: 35
Explanation: There are only three printers, so at most three jobs can print simultaneously.

## Question 6

What is the purpose of `message_lock` in the project?

- To download files
- To create random filenames
- To remove print jobs
- To keep printed status messages readable

Answer: 4
Type: single
Time: 40
Explanation: The lock avoids multiple threads mixing their status output.

## Question 7

What could happen if a printer is never returned to the queue?

- More printers appear
- The queue becomes faster
- Future jobs may wait forever or the system may slow down
- Python automatically fixes it

Answer: 3
Type: single
Time: 45
Explanation: Losing a resource from the pool can block later jobs.

## Question 8

Why does the output order vary between runs?

- Parallel jobs finish at different times
- Python cannot print strings
- The queue deletes old jobs
- The list is invalid

Answer: 1
Type: single
Time: 40
Explanation: In parallel execution, scheduling and random print durations affect finish order.

## Question 9

Why might a real printer system use priorities?

- Priorities prevent all errors automatically
- Priorities make printers unlimited
- Priorities remove the need for queues
- Some jobs may be more urgent than others

Answer: 4
Type: single
Time: 40
Explanation: Real systems often need urgent jobs to move ahead of less urgent ones.

## Question 10

Which design best matches the project?

- One worker writes one local variable
- Many workers share a limited pool of named resources
- No task ever waits
- Every job gets its own new printer

Answer: 2
Type: single
Time: 45
Explanation: The printer project is a resource-pool simulation with named resources.
