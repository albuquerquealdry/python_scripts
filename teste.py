import os

typeservice= ""
env = "JOB_NAME"


os.system("git clone https://github.com/albuquerquealdry/{}.git".format(env))
os.system(""" cd {} && ls -lh >> README.md && git add . && git commit -m"teste" && git push """.format(env))

