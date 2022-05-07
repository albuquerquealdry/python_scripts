import os

env = "prometheus"


os.system("git clone https://github.com/albuquerquealdry/{}.git".format(env))
os.sytem("cd {} && cat READNE.md".format(env))
