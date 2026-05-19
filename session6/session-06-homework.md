### Session 6 | Homework

> In this homework, you will extend the Session 5 capstone project by adding controlled parallel video downloading.

#### 1. Goal

You will:

- revisit your Session 5 capstone repository
- add 5 more short YouTube video URLs
- limit parallel video downloads to 5 at a time
- use a semaphore to coordinate shared result-file writing
- record clear success/failure output for each video

#### 2. Capstone repository

Use the separate capstone repository from Session 5:

[BDA capstone 1](https://github.com/warestack/bda-capstone-1)

Do not write your capstone solution files in this weekly `bda` repository.

#### 3. What to do

1. Open your fork of the Session 5 capstone repository.
2. Pull the latest changes from your fork.
3. Find 5 additional short YouTube videos.
4. Add the 5 new URLs to your capstone input list.
5. Update your downloader so no more than 5 videos download at the same time.
6. Use `threading.Semaphore(5)` or an equivalent semaphore to enforce the download limit.
7. Use a semaphore or lock-style protected section when writing results to a shared results file.
8. Record one result line per video:
   - URL
   - status (`success` or `failed`)
   - output filename or error message
   - timestamp
9. Test your program with the expanded URL list.
10. Commit and push your updated capstone work.

#### 4. Suggested design

Use one semaphore for the download limit:

```python
download_limit = threading.Semaphore(5)
```

Use another one-at-a-time guard for the shared results file:

```python
result_file_guard = threading.Semaphore(1)
```

This is intentionally similar to a mutex. It allows exactly one worker to write to the file at a time.

#### 5. File to submit in this repository

Create this file:

```txt
session6/solutions/exercise-06-homework.md
```

Your markdown file should include:

~~~md
# Session 6 Homework

## Capstone repository

Link:

## New YouTube URLs

1.
2.
3.
4.
5.

## What I changed

Explain how you limited parallel downloads to 5.

## Semaphore design

Explain where you used the download semaphore and where you protected result-file writing.

## Result file format

Show 2-3 example result lines from your output file.

## Testing

Explain how you tested that only 5 downloads can run at once.

## Reflection

What was harder: limiting downloads or safely writing results? Why?
~~~

#### 6. Rules

- Use Python.
- Use a semaphore for the parallel download limit.
- Add exactly 5 additional short YouTube URLs.
- Do not overwrite old capstone results without backing them up or clearly regenerating them.
- Record failures instead of hiding them.
- Keep your code readable enough for another student to follow.

#### 7. Share your work

Post your completed `session6/solutions/exercise-06-homework.md` in the class discussion forum.

Use the MS Teams discussion forum:

[MS Teams discussion forum](https://teams.microsoft.com/l/team/19%3AQLvZizpid98i6iNwF9_ee7RuoAUPC9YsOVoB3Yrq5YY1%40thread.tacv2/conversations?groupId=8b3672d8-2c38-4134-9725-3b779f03c2b0&tenantId=89d07f47-d258-463c-8700-635ffaeca38e)

When you post, include:

- your capstone repository link
- your 5 new video URLs
- a short explanation of your semaphore design
