import os

env = "JOB_NAME"


os.system("git clone https://github.com/albuquerquealdry/{}.git".format(env))
os.system("cd {} && cat README.md".format(env))
