from colorama import init as colors, Fore; colors()
from threading import Thread
from time import sleep
from random import choice

def worker():
	# Timer Thread
	Colors = [Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.YELLOW]
	Colors = ([''] * (20//5)) + [choice(Colors) for _ in range(60//5)]
	step = 1
	time = -step
	while not sleep(.01):
		time += step
		mins = time // 60
		if mins >= 60: print('\n' + Fore.MAGENTA + ' Limit hit'); exit()
		secs = time  % 60
		if   mins == 0                   : color = Fore.LIGHTGREEN_EX
		elif mins in [1, 2, 3, 4]        : color = Fore.GREEN
		elif mins in [5, 6, 7, 8, 9]     : color = Fore.YELLOW
		elif mins in [10, 11, 12, 13, 14]: color = Fore.LIGHTRED_EX
		elif mins in [15, 16, 17, 18, 19]: color = Fore.RED
		else                             : color = Colors[mins//5]
		print(f'\r  {color}{str(mins).zfill(2)}:{str(secs).zfill(2)}{Fore.RESET}', end='', flush=True)

def stop():
	# Thread to stop the timer: when this thread exits, the main program dies, and tada!
	try: input(); exit()
	except: exit()

Threads = [Thread(target=worker), Thread(target=stop)]
for i in Threads: i.daemon = True
for i in Threads: i.start()
try: Threads[1].join()
except: pass
