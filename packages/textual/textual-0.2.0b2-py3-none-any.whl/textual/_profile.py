"""
Timer context manager, only used in debug.

"""

from time import time

import contextlib
from typing import Generator

from . import log


@contextlib.contextmanager
def timer(subject: str = "time") -> Generator[None, None, None]:
    """print the elapsed time. (only used in debugging)"""
    start = time()
    yield
    elapsed = time() - start
    elapsed_ms = elapsed * 1000
    log(f"{subject} elapsed {elapsed_ms:.2f}ms")
