#shutting down computer with python
import os
import platform
def main():
    if platform.system()=="windows":
        os.system("shutdown -s -t -0")
    else:
        os.system("shutdown -h now")
if __name__ == '__main__':
    main()
#run and Shutdown