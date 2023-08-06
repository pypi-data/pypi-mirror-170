# Python module for counting unique symbol

Module get nuber of uniq chars in text file, string or function

## Options:
```
unique_character.cli_unique_character [-h] 
```
```
unique_character.cli_unique_character [--file FILE] 
```
```
unique_character.cli_unique_character [--string STRING]
```
```
from unique_character.count_unique_character import count_letter
assert count_letter('1234') == 4


```
## Examples:

#### Command:
```bash
python3.8 -m unique_character.cli_unique_character --string aaabbcc123
```
#### Return:
```bash
3
```

#### Command:
```bash
python3.8 -m unique_character.cli_unique_character --file text_file.txt
```
#### Return:
```bash
100
```