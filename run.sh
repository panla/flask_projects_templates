venv/bin/gunicorn -c settings.py --log-level=debug --reload manager:app
