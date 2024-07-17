#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import os
import platform
import subprocess


def main():
    # def ping(host):
    #     param = "-n" if platform.system().lower() == "windows" else "-c"
    #     command = ["ping", param, "1", host]
    #     return subprocess.call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0
    #
    # subnet = "192.168.1."  # 替换为你的子网前缀
    #
    # for i in range(170, 255):
    #     ip = subnet + str(i)
    #     if ping(ip):
    #         print(f"Host {ip} is up")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_introduction.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
