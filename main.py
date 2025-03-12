#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import Webnew



warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
import os
def system():
    os.system('npm create vite@latest sample')
    os.chdir('sample')
    os.chdir('src')
    os.system('npm install')
def running():
    os.system('npm run dev')
def run():
    Webnew().crew().kickoff()
system()
run()
running()