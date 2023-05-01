import os
import datetime

for year in range(11, datetime.datetime.now().year - 2000 + 1):
    for sem in range(1, 4):
        os.system(f"python3 main.py {year}-{year+1}-{sem}")
