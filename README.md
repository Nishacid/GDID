# GDID (Google Dorks for Information Disclosure)

Script made for your recon automation in Bug Bounty or Pentest. It will help you to find `Information Disclosure`.

## Installation 

```bash
git clone https://github.com/Nishacid/GDID.git
cd  GDID/
pip3 install -r requirements.txt
```

## Usage

```bash
usage: main.py [-h] -c COMPANY
```

### Exemple 

```
python3 main.py -c Tesla

[+] Possible result found for github.com : https://google.com/search?q=site:http://github.com%20Tesla
[+] Possible result found for gitlab.com : https://google.com/search?q=site:http://gitlab.com%20Tesla
[+] Possible result found for codepen.io : https://google.com/search?q=site:http://codepen.io%20Tesla
[+] Possible result found for trello.com : https://google.com/search?q=site:http://trello.com%20Tesla
[...]
```