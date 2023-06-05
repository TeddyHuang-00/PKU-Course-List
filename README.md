# PKU-Course-List

This is a repo for scraping all course list from http://www.dean.pku.edu.cn

## Installation

Install the dependencies:

```sh
$ pip install -r requirements.txt
```

## Usage

### Overview

You can check out the usage of parameters by typing `python3 main.py -h`:

```sh
usage: main.py [-h] [-c COURSENAME] [-t TEACHERNAME] [-s COURSETYPE] [-y YUANXI] [-r RETRY] [-l LOGLEVEL] [-p] [-f] YearAndSeme

positional arguments:
  YearAndSeme           Year and semester to look up for (e.g. 22-23-1 stands for the first semester in year 2022-2023)

options:
  -h, --help            show this help message and exit
  -c COURSENAME, --coursename COURSENAME
                        Course name to look up for (default empty string for all)
  -t TEACHERNAME, --teachername TEACHERNAME
                        Teacher name to look up for (default empty string for all)
  -s COURSETYPE, --coursetype COURSETYPE
                        Course type to look up for (default 0 for all)
  -y YUANXI, --yuanxi YUANXI
                        School/department to look up for (this is the code for school/department, default 0 for all)
  -r RETRY, --retry RETRY
                        Max number of retries before giving up (default 3)
  -l LOGLEVEL, --loglevel LOGLEVEL
                        Log level for printing to console (default 2:INFO)
  -p, --parallel        Enable multi-processing scraping (default False)
  -f, --force           Overwrite the existing output file (default False)
```
