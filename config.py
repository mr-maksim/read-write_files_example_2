from ntpath import join
import os

BASE_PATH = os.getcwd()
FILE_DIR = 'files'
RESULT_DIR = 'result'
FILE_RESULT = 'result.txt'
FILE_IN_DIR = os.listdir(join(BASE_PATH,FILE_DIR))
