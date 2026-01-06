#!/usr/bin/env python3
"""
DevOps Log Error Filter: Extract ERROR-level messages from multi-line logs.

Optimized for production log parsing, alerting systems, and infrastructure monitoring.
"""
import re

LOG_DATA = """
2025-01-15 08:45:23 INFO    User logged in
2025-01-15 09:15:42 ERROR   Failed to connect to database
2025-01-15 10:01:05 WARNING Disk space running low
2025-01-15 11:22:10 ERROR   Pod crashloop in namespace=prod
"""

# compiles a regex that matches the exact word ERROR (with word boundaries \b to avoid false matches like ERRORCODE
ERROR_PATTERN = re.compile(r"\bERROR\b")


def find_error_lines(log_text: str) -> list[str]:
    """Return all log lines that contain the ERROR level."""
    error_lines = []
    # Iterates over each line in the log_text string.
    for line in log_text.splitlines():
        
        if ERROR_PATTERN.search(line):    # Tests whether the compiled regular expression ERROR_PATTERN matches anywhere inside the current line.
            error_lines.append(line)
    return error_lines


# runs only when executed directly (not when imported). Best practice for production code.
if __name__ == "__main__":
    for line in find_error_lines(LOG_DATA):
        print(line)
