# MIT License
# 
# Copyright (c) 2023 CashLabMines
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def getLogAnalyte(idx):
    if idx == 0:
        logA = -9
    elif idx == 1:
        logA = -7
    elif idx == 2:
        logA = -6
    elif idx == 3:
        logA = -5
    elif idx == 7:
        logA = -4
    elif idx == 11:
        logA = -3
    elif idx == 15:
        logA = -2
    elif idx == 14:
        logA = -1
    elif idx == 13:
        logA = 0
    elif idx == 12:
        logA = 2
    else:
        logA = -99
    
    return logA


def getLogAnalyteSwapped(idx):
    if idx == 0:
        logA = -9
    elif idx == 4:
        logA = -7
    elif idx == 8:
        logA = -6
    elif idx == 12:
        logA = -5
    elif idx == 13:
        logA = -4
    elif idx == 14:
        logA = -3
    elif idx == 15:
        logA = -2
    elif idx == 11:
        logA = -1
    elif idx == 7:
        logA = 0
    elif idx == 3:
        logA = 2
    else:
        logA = -99
    
    return logA