#!/bin/bash
export DISPLAY=:0
cd /YOUR/WORK/DIR/
date >> main.log
python3 main.py id1 passwd1 >> main.log
echo "===========" >> main.log
