from concurrent.futures import ThreadPoolExecutor
import threading
import time

import requests


call_limit = threading.Semaphore(4)
write_lock = threading.Lock()
active_lock = threading.Lock()
active_calls = 0


def write_result(line):
    with write_lock:
        with open("request_results.txt", "a", encoding="utf-8") as file:
            file.write(line + "\n")


def fetch(request_id):
    global active_calls

    url = f"https://httpbin.org/delay/1?request={request_id}"

    with call_limit:
        with active_lock:
            active_calls += 1
            current_active = active_calls

        print(f"[START] request {request_id:02d} active={current_active}")

        try:
            response = requests.get(url, timeout=10)
            status = f"success status={response.status_code}"
        except requests.RequestException as exc:
            status = f"failed error={exc}"

        with active_lock:
            active_calls -= 1
            current_active = active_calls

        print(f"[DONE] request {request_id:02d} active={current_active}")

    write_result(f"request={request_id:02d} {status}")


if __name__ == "__main__":
    with open("request_results.txt", "w", encoding="utf-8"):
        pass

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=40) as executor:
        executor.map(fetch, range(1, 41))

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f}s")
    print("Done. Check request_results.txt")
