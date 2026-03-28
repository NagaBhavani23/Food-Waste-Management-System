#!/usr/bin/env python
"""Top-level manage.py wrapper so `python manage.py` works from repo root."""
import os
import sys


def main():
    # Ensure the project package is on path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.join(current_dir, 'foodwaste_project')
    if project_dir not in sys.path:
        sys.path.insert(0, project_dir)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodwaste_project.settings')
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
