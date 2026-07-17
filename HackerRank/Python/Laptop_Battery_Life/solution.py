#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    timeCharged = float(input().strip())
    print(f"{min(2 * timeCharged, 8.0):.2f}")
