#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# hiiiiiii
##hlw ww
#:)      muje btao ki tm direct call kie te telegram call se phele? nope
#acha mera v abi tk rom change ni kia to lte me call ni ata bs gsm me ata he [xustom roms be like XD] lol :DDDD
import logging
import pytz
from datetime import datetime
import pytz
import datetime
# Set the basic configuration for the logger
logging.basicConfig(filename="app.log", level=logging.INFO)

# Use the log method to log a message


#acha to chlo shuru krte he   yup
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line

        ist = pytz.timezone('Asia/Kolkata')
        logging.info(f"\n[{datetime.datetime.now(ist)}] : Application started")
    except ImportError as exc:
        logging.error("Application crashed")
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?") from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
