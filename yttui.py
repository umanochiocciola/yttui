#! /bin/python3

from youtubesearchpython import VideosSearch
from os import system
from sys import argv


HELP = '''

usage:
    yttui <search prompt> interval-len <len> max-len <len>

interal-len is optional, change <len> to the amount of titles you wish to be displayed per chunk (default 5)
interal-len is optional, change <len> to the amount of titles you wish to be loaded (default 50)

'''

def main():
    try:
        title()
        ilen, mlen, query = parse_args()
        titles, links = load_stuff(ilen, mlen, query)
        selection(titles, links, ilen)
        
    except Exception as e:
        error(f'Shit! I fucked up something! Sorry, it\'s so embarrassing!\nThis thing happend: {e}\nPlease contact me if you have a solution or just to report the bug :)')



def error(cringe):
    print('\33[0;31mERROR:',cringe)
    exit(1)

def place(status):
    print('\33[1;32m'+status+'\33[0;37m]')

def debug(task):
    print('\33[0;37m[ ]', task, end='\r[')


def title():
    print("\33[1;31m+---------------------------------------------+")
    print("|                YouTube TUI                  |")
    print("+---------------------------------------------+\33[0;37m")
    print('watch videos without executing any google shit!')

def parse_args():

    if 'help' in argv:
        print(HELP)
        exit(0)

    INTERVAL_LEN = 5
    if 'interval-len' in argv:
        try:
            INTERVAL_LEN = argv[argv.index('interval-len')+1]
            argv.remove('interval-len')
            argv.remove(INTERVAL_LEN)
            INTERVAL_LEN = int(INTERVAL_LEN)
        except: error('interval-len needs a numerical input')
    
    MAX_LEN = 50
    if 'max-len' in argv:
        try:
            MAX_LEN = argv[argv.index('max-len')+1]
            argv.remove('max-len')
            argv.remove(MAX_LEN)
            MAX_LEN = int(MAX_LEN)
        except: error('max-len needs a numerical input')

    if len(argv)<2:
        print('\n(no search argument provided)')
        QUERY = input('\33[1mSEARCH: \33[0;37m')
        print('\n')
    else:
        QUERY = ''.join(argv[1:])
    
    
    return INTERVAL_LEN, MAX_LEN, QUERY


def load_stuff(INTERVAL_LEN, MAX_LEN, QUERY):
    debug('retrieving video info...')

    videosSearch = VideosSearch(QUERY, limit=MAX_LEN)
    out = videosSearch.result()
    result = out.get('result', {})
    
    titles = []
    links = []
    for i in range(len(result)):
        titles.append( result[i].get('title', 'TITLE UNAVAIABLE') )
        links.append(  result[i].get('link', '')                  )
        # cannel?, more info? there's a lot that could be added

    place('OK')
    print('-'*30)

    return titles, links


def selection(titles, links, INTERVAL_LEN):

    # display search results
    interval = (0, INTERVAL_LEN)
    a=''
    while type(a) != int:
        for i in range(len(titles[interval[0]:interval[1]])):
            print('\33[0;32m[\33[1;32m',i+interval[0],'\33[0;32m]\33[1;37m ', titles[i+interval[0]], end='\n')

        print('\33[0;37m[ ] ENTER to display more results, Q to quit, number to play video', end='\r[')
        a = input()
        print('                                                                           ', end='\r')
        if a == '':
            interval = (interval[1], interval[1]+INTERVAL_LEN)

        if a.lower() == 'q':
            exit(0)

        try: a = int(a)
        except: 0


    print('enjoy your javascript spyware and cookies free video! (ignore the command prompt, just wait a sec)')

    system(f"mpv \"{links[a]}\" &> /dev/null")
    

if __name__ == "__main__":
    main()
