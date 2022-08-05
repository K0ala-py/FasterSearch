
# FasterSearch

THIS IS A DIR SEARCH!
RUNS THE ENTIRE WORDLIST IN 45 SECONDS
READ THE NOTE TO KNOW MORE!

## Note

- THIS PROGRAM CANNOT BE RUN WITH OTHER WORDLIST
- THIS PROGRAM DOES THE ENTIRE SCAN IN A MAXIMUM OF 1 MINUTE AND 30 SECONDS!
  IF IT EXCEEDS ONE MINUTE YOU NEED TO STOP THE SCRIPT
- THIS PROGRAM NEEDS SOME LIBRARIES TO DOWNLOAD (see installation)
## Installation

You have need this library for use my script: 

### Linux / Windows 
```bash
cd FasterSearch
pip install -r requirements.txt
```
    
## Use

BOTH FUNCTIONS ARE MANDATORY!
For help write:

```bash
python FasterSearch.py -h
```
### help
- -u  |  Enter URL
- -s  |  Enter status you want (200,404,403) {if you want see all pages != 404, enter 'all'}

### examples:

- python FasterSearch.py -u https://example.com -s all
- python FasterSearch.py -u https://example.com -s 403
- python FasterSearch.py -u https://example.com -s 200
