import argparse
import bruteforce
from termcolor import colored, cprint

cprint(
'''


▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀     ██████  ██░ ██  ▄▄▄      ▓█████▄  ▒█████   █     █░
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ░██   █▌▒██░  ██▒▒█░ █ ░█ 
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄      ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░░█░ █ ░█ 
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░░██▒██▓ 
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░   ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░  
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░    ░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░   ░  
   ░          ░  ░   ░     ░  ░            ░   ░  ░  ░      ░  ░   ░        ░ ░      ░    
 ░                                                               ░                        


=============================================================================================================
''', 'magenta'
)
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--user', help='username')
parser.add_argument('-L', '--users', help='Users File')
parser.add_argument('-p', '--password', help='password')
parser.add_argument('-P', '--passwords', help='Passwords File')
parser.add_argument('-u', '--url', help='URL')
parser.add_argument('-v', '--verbose', help='Continues brute force after valid password is found', action='store_true')
#parser.add_argument('-d', '--droplet', help='Get droplet info', action='store_true')

args = parser.parse_args()

def help_message():
    print("Usage: main.py -l admin -P wordlist.txt -u http://website.com/login.php")

if args.url:
    url = args.url
else:
    help_message()
    exit()

if args.user:
    user = args.user
elif args.users:
    user = args.users
else:
    help_message()
    exit()

if args.password:
    password = args.password
elif args.passwords:
    password = args.passwords
else:
    help_message()
    exit()

if args.verbose:
    verbose = True
else:
    verbose = False

if __name__ == '__main__':
    bruteforce.brute_force_passwords(user, password, url, verbose)