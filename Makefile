target: hello run clean

hello:
	echo "Hello, this is run from Makefile"

run:
	python3 -m converter -c 30
	python3 -m converter -f -925

clean:
	rm -rf __pycache__