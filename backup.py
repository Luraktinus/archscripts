#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


bpath="/home/lue/sirius/backups/"
bsname=sys.argv[1]+".tar.gz"
expath="/home/lue/sirius/exclude.txt"

class Tools:
    # Procheck tests what software is installed
    def procheck(self, prog):
        chksum = os.system("which "+prog)
        if chksum == 0:
            return True
        else:
            return False
t = Tools()
if t.procheck("sudo"):
    if t.procheck("tar"):
        os.system("sudo rm "+bpath+bsname)
        print("Deleted old bootstrap!")
        os.system("sudo tar --exclude-from="+expath+" --xattrs -czpvf "+bpath+bsname+" /")
    else:
        print("No tar installed!")
else:
    print("No sudo installed!")

# USE GNU/TAR FOR BACKUP
# Restore from rootdir: tar --xattrs -xvpf $backupfile
