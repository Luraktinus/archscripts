#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
class Tools:
    # Procheck tests what software is installed
    def procheck(self, prog):
        chksum = os.system("which "+prog)
        if chksum == 0:
            return True
        else:
            return False
t = Tools()
if t.procheck("pacman"):
    os.system("sudo pacman -Syu")
    os.system("sudo pacman -Rsn $(pacman -Qdtq)")
    os.system("sudo pacman -Sc")
    os.system("sudo bootctl update")
elif t.procheck("apt"):
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    os.system("sudo apt autoremove")
    os.system("sudo apt clean")

