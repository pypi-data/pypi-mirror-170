"""
hydrogen_logging

# Defines function to set up the python logger using hydrogen conventions.
"""

import logging
import os
import time
from datetime import datetime
from .directory_paths import get_data_directory


def hydrogen_setup_logger():
    """Configure the python logging to write log messages to a standard place."""

    log_prefix = os.environ.get("HYDRO_LOG_PREFIX", "")
    dirpath = get_data_directory()
    log_file = None
    if dirpath is not None:
        log_dir = f"{dirpath}/logs"
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
            os.chmod(log_dir, 0o777)
        today = datetime.utcnow().strftime('%Y-%m-%d')
        log_file = f"{log_dir}/hydrogen-{log_prefix}-{today}.log"
        if not os.path.exists(log_file):
            with open(log_file, "w+") as stream:
                stream.write("")
            os.chmod(log_file, 0o777)

    logging.Formatter.converter = time.gmtime
    if log_file is not None:
        # Configure the python logger to log into this file
        logging.basicConfig(
            filename=log_file,
            format='%(asctime)s (UTC) %(levelname)s:%(message)s',
            level=logging.INFO,
        )
    cleanup_log_files()
    # Set Umask for process so hydrofiles have rw for group
    os.umask(0o002)

def cleanup_log_files():
    "Remove log files that are older than xxx days."""

    log_prefix = os.environ.get("HYDRO_LOG_PREFIX", "")
    dirpath = get_data_directory()
    log_dir = os.path.join(dirpath, "logs")

    # Find the name of the oldest log file to keep
    save_duration_days = 7
    old_time = time.time() - save_duration_days * 24 * 60 * 60
    old_time_str = time.strftime('%Y-%m-%d', time.localtime(old_time))
    old_log_file_name = f"{log_dir}/hydrogen-{log_prefix}-{old_time_str}.log"

    # Remove any log files older than that
    dirpath = get_data_directory()
    log_file = None
    if dirpath is not None:
        log_dir = f"{dirpath}/logs"
        if  os.path.exists(log_dir):
            for f in os.listdir(log_dir):
                log_file = f"{log_dir}/{f}"
                if f.startswith(f"hydrogen-{log_prefix}-") and f.endswith(".log") and log_file <= old_log_file_name:
                    os.remove(log_file)

    

