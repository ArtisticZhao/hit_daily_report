#!/bin/bash
export DISPLAY=:0
cd /YOUR/WORK/DIR/
# DONT merge the old log
echo "" >> main.log
echo "===========" >> main.log
echo "Report At:" >> main.log
date >> main.log
echo "===========" >> main.log

# 2>&1 redirct the errors to normal output stream
# ONLY change the id1 and passwd1
python3 main.py id1 passwd1 >> main.log 2>&1 &
echo "===========" >> main.log
