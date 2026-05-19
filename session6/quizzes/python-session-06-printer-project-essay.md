# Essay Question: design a controlled parallel printer system

## Question
Assume you are designing a small print server for an office.

The office has many print jobs, but only three physical printers. Jobs can arrive at different times, and some jobs may fail halfway through.

Explain how you would design the system.

Your answer must explicitly discuss:
- how print jobs wait for an available printer
- how you would track which printer is assigned to each job
- how you would ensure printers are returned after success or failure
- what status messages or result logs you would record
- one improvement for a real system, such as priorities, retries, or cancellation

Do not write code. Focus on reasoning and design decisions.

## Instructions for Students
Write 10-14 lines.

## Instructor Name
Stelios

## Hint
Hint: Think about the printer as a limited shared resource, not just a string in a list.

## Evaluation Criteria (Total: 4 points)
1. **Resource-pool design (1 point)**  
- Correctly explains that only three printers can be active at once.  
- We expect mention of a queue, semaphore, or equivalent waiting mechanism.  
- We expect the answer to avoid "start everything without control."
2. **Printer assignment clarity (1 point)**  
- Explains how each job receives a specific printer name or identifier.  
- We expect the student to track which printer handled which file.  
- We expect clear reasoning about avoiding duplicate assignment of the same printer.
3. **Cleanup and failure handling (1 point)**  
- Explains that printers must be returned after success or failure.  
- We expect mention of `finally`, cleanup, error handling, or equivalent logic.  
- We expect at least one concrete failure risk.
4. **Logging and real-system thinking (1 point)**  
- Describes useful status/result logs.  
- Includes one realistic improvement such as priority jobs, retries, cancellation, or estimated wait time.  
- Writing should be concise and use correct terminology.

## Reference Answer
A practical print server should treat printers as a limited shared resource.

I would keep the three available printer names in a shared queue. When a job arrives, it waits until it can get one printer from the queue. This prevents more than three jobs from printing at the same time and also records which physical printer is assigned.

Each job should log when it is waiting, when it starts, which printer it uses, when it finishes, and whether it failed. The printer should be returned to the queue in a cleanup step such as `finally`, because a failed job should not permanently remove a printer from the system.

For result tracking, I would write one line per job with the filename, printer name, status, duration, and error message if needed.

In a real office system, I would add priorities for urgent jobs, retries for temporary printer errors, and cancellation for jobs submitted by mistake.

## AI Evaluation Rules
Evaluate only by the rubric above.
Do not use external knowledge.
Score = (points achieved / 4) x 100.
Accept equivalent phrasing and related concepts, not only exact wording from the reference answer.
Award credit when the student uses correct ideas with different terminology (for example "printer pool", "available resource list", "cleanup step", "job log", "retry failed print").
Do not penalize minor wording differences if the reasoning is correct and complete.
When partially correct, give partial credit in the relevant criterion and explain exactly what is missing.

## Output Format
Score: XX%

Feedback:
- What the student did well
- What is missing
- 1-2 suggestions for improvement
