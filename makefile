setup: requirements.txt
    pip install -r requirements.txt
run:
    python setup.py
clean:
    rm -rf __pycache__