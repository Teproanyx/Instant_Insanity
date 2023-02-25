import glob
import os


def cleanup():
    for f in glob.glob("*.svg"):
        os.remove(f)


if __name__ == '__main__':
    cleanup()
