import subprocess
import threading
import time
import shutil
import tempfile
from pathlib import Path
import psutil

from ..config import PYTHON_BIN, RUN_TIMEOUT

def run_file_with_input(code_path: Path, input_data: str = None, timeout: int = RUN_TIMEOUT):
    with tempfile.TemporaryDirectory() as tmpdir:
        target = Path(tmpdir) / code_path.name
        shutil.copy(code_path, target)

        proc = subprocess.Popen(
            [PYTHON_BIN, str(target)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        stdout = ""
        stderr = ""

        # ---- Thread to run communicate() so it won't block ----
        def read_io():
            nonlocal stdout, stderr
            try:
                stdout, stderr = proc.communicate(input=input_data, timeout=timeout)
            except subprocess.TimeoutExpired:
                proc.kill()

        io_thread = threading.Thread(target=read_io)
        io_thread.start()

        # ---- Memory monitoring loop ----
        max_rss = 0
        start = time.perf_counter()

        p = psutil.Process(proc.pid)

        while io_thread.is_alive():
            try:
                rss = p.memory_info().rss
                max_rss = max(max_rss, rss)
            except psutil.NoSuchProcess:
                break

            time.sleep(0.02)

        io_thread.join()  # ensure I/O is done
        end = time.perf_counter()

        return {
            "returncode": proc.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "runtime": end - start,
            "memory": max_rss,
        }
