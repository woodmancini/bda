## Welcome to Session 6

### Learning goals

By the end of Session 6, you should be able to:

- explain why shared resources need coordination
- use a mutex with `threading.Lock`
- use a semaphore with `threading.Semaphore`
- limit concurrent work in a practical I/O-style task
- design a small parallel resource-allocation project

### Recommended order

1. [Part 1](./session-06-part-01.md)
2. [Part 2](./session-06-part-02.md)
3. [Optional Mini Project](./session-06-optional-mini-project.md)
4. [Homework](./session-06-homework.md)
5. Write your own work in [solutions](./solutions/).
6. Review [reference solutions](./session_solutions/) only after attempting tasks yourself.
7. Practice with [quizzes](./quizzes/) when ready.

### Notes

- Tutorial and warm-up material is included directly inside each part markdown file.
- Keep your own solutions in separate files inside `solutions/`.
- Use exercise-style names in `solutions/` (for example `exercise-06-01.py`, `exercise-06-02.py`).
- For the optional project, create `solutions/exercise-06-project.py`.
- For homework, create `solutions/exercise-06-homework.md`.
- Create your files inside `solutions/` as you work through each part.
- Reference answers are in `session_solutions/`.
- If `requirements.txt` is missing, create it and add:
  - `requests==2.32.3`
  - `Faker`
  - `quizmd`
- Keep all dependencies in `requirements.txt`, then install with:
  - `pip install -r requirements.txt`
