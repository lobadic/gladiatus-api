import time

#time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())

def info(text):
	print(f'[INFO {time.strftime("%H:%M:%S", time.gmtime())}] {text}')

def warning(text):
	print(f'[WARNING {time.strftime("%H:%M:%S", time.gmtime())}] {text}')

def error(text):
	print(f'[ERROR {time.strftime("%H:%M:%S", time.gmtime())}] {text}')