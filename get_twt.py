import os
import glob
import multiprocessing
import threading
import time
from datetime import datetime

from multiprocessing.pool import ThreadPool

def worker(file):
	now = datetime.now()
	current_time = str(now.month) + '_' + str(now.day)
	
	print(file)
	dir ='G:\\twitter_raw_data\\'
	
	#exe = 'python ' + file + ' > twt_' + file + '_' + current_time + '.txt'
	exe = 'python ' + file + ' >' + dir + 'twt_' + file + '_' + current_time + '.txt'
	
	print(exe)
	os.system(exe)

MAX_THREADS = 30
def export_to_files(filenames):
	pool = ThreadPool(processes=MAX_THREADS)
	pool.map_async(worker,filenames)
	pool.close()
	pool.join()

	
def get_files():
	file_list = []
	for file in os.listdir('.'):
		if file.startswith('get_twitter_data'):
			file_list.append(file)
	return file_list
	
	
if __name__ == '__main__':
	#files = ['get_twitter_data_0.py','get_twitter_data_1.py']
	files = get_files()
	print(files)
	export_to_files(files)

