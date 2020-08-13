import os

def file_less_than_50mb(file_name):
    size = os.path.getsize(file_name)
    return size <= 52428800
