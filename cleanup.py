import glob
import os


def cleanup():
    """Cleanup svg files"""
    for f in glob.glob("*.svg"):
        os.remove(f)


if __name__ == '__main__':
    cleanup()
