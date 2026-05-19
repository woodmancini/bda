# Session 6 Homework Reference Notes

This is not a full capstone solution. Use it as a checklist for reviewing your own capstone extension.

## Expected changes

- Add exactly 5 additional short YouTube URLs to the capstone input list.
- Keep the existing capstone behavior working.
- Use a semaphore with 5 permits to limit parallel video downloads.
- Protect shared result-file writing so one worker writes a complete result line at a time.
- Record success and failure outcomes clearly.

## Suggested pattern

```python
import threading

download_limit = threading.Semaphore(5)
result_file_guard = threading.Semaphore(1)


def download_video(url):
    with download_limit:
        # Run the actual video download here.
        result_line = "..."

    with result_file_guard:
        with open("download_results.txt", "a", encoding="utf-8") as file:
            file.write(result_line + "\n")
```

## Testing checklist

- Print active download count while testing.
- Confirm the active count never goes above 5.
- Confirm every URL produces one result line.
- Confirm failures are written to the result file.
- Run the program twice and check that output filenames/results are understandable.
