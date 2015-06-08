import os

import sh

print sh.ifconfig("en0")
print sh.ls("/")
sh.git.clone("git@git.superboss.cc:dmj/dmj-tj.git")

os.system('clear')
