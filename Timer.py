from colorama import init as colors, Fore; colors()
from threading import Thread
from time import sleep

def worker():
	# Timer Thread
	step = 1
	time = -step
	while not sleep(1):
		time += step
		mins = time // 60
		if mins >= 60: print(Fore.MAGENTA + 'Limit hit'); exit()
		secs = time  % 60
		if   mins == 0                   : color = Fore.LIGHTGREEN_EX
		elif mins in [1, 2, 3, 4]        : color = Fore.GREEN
		elif mins in [5, 6, 7, 8, 9]     : color = Fore.YELLOW
		elif mins in [10, 11, 12, 13, 14]: color = Fore.LIGHTRED_EX
		else: color = Fore.RED
		print(f'  {color}{str(mins).zfill(2)}:{str(secs).zfill(2)}{Fore.RESET}')

def stop():
	# Thread to stop the timer: when this thread exits, the main program dies, and tada!
	try: input(); exit()
	except: exit()

Threads = [Thread(target=worker), Thread(target=stop)]
for i in Threads: i.daemon = True
for i in Threads: i.start()
try: Threads[1].join()
except: pass