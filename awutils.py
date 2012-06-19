import sys

def progress(msg):
    sys.stdout.write('\r' + msg)
    sys.stdout.flush()

if __name__ == '__main__':
    import time
    for i in range(100):
        progress('Progress: %d%%' % i)
        time.sleep(0.2)
