#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#USE GNU/TAR FOR BACKUP

import os
import sys

class Tools:
    # Procheck tests what software is installed
    def procheck(self, prog):
        chksum = os.system("which "+prog)
        if chksum == 0:
            return True
        else:
            return False
#-------------------------
t = Tools()
program=sys.argv[1]
print(os.getenv("HOME"))
home=os.getenv("HOME")
#-------------------------



if t.procheck("git"):
    if t.procheck("makepkg"):
        os.chdir(home)
        os.system("mkdir apps")
        os.chdir(home+"/apps")
        os.system("git clone https://aur.archlinux.org/"+program+".git")
        os.chdir(home+"/apps/"+program)
        os.system("makepkg -si")
    else:
        print("No makepkg installed!")
else:
    print("No git installed!")
