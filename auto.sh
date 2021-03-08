#!/bin/bash
export DISPLAY=:0
cd /YOUR/WORK/DIR/
# merge the old log
date > main.log
# 2>&1 redirct the errors to normal output stream
python3 main.py id1 passwd1 >> main.log 2>&1
echo "===========" >> main.log
