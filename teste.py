import os

env = "JOB_NAME"


os.system("git clone https://github.com/albuquerquealdry/{}.git".format(env))
os.sytem("cd {} && cat READNE.md".format(env))
