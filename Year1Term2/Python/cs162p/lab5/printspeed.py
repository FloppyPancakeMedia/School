import sys,time

def print_medium(string : str):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def print_slow(string : str):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)
    print()

def print_slower(string : str):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def print_slowest(string : str):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)
    print()