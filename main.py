import time
import subprocess

COMMAND_FILE = 'command.txt'
HISTORY_FILE = 'history.txt'
SETUPENV = "source ~/.bashrc && "

def compute_line():
    with open(HISTORY_FILE) as f:
        lines = f.readlines()
    lines = list(filter(lambda x: x.strip() != "", lines))
    return len(lines)

def read_command(n):
    with open(COMMAND_FILE) as f:
        lines = f.readlines()
        if n >= len(lines):
            return None
        return lines[n]

def append_hist():
    with open(HISTORY_FILE, 'a') as f:
        f.write(f"{time.time()}\n")

def run():
    '''
    return number of seconds to sleep
    '''
    n = compute_line()
    cmd = read_command(n)
    if cmd is None:
        print("cmd none. end of file")
        return 1
    cmd = SETUPENV + cmd
    p = subprocess.Popen(cmd, shell=True)
    p.wait()
    append_hist()
    return 0

while 1:
    c = run()
    time.sleep(c)
