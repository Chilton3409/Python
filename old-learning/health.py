#!/usr/bin/env python3
#New file created
from ftplib import error_perm
import psutil
#import emails
import os
import sys
import shutil
import socket
from multiprocessing import Pool
import json

class healthChecks():
    def __init__(self):
        self.messages = {}

    def cpu_check(self):
        cpu_usage = psutil.cpu_percent(1)
        if cpu_usage > 80:
            error_message = "Error --cpu usage clocked at over"
            self.messages = {error_message, cpu_usage}
        else:
            self.messages = {"Cpu usage:", cpu_usage}

    def check_cpu_stats(self):
        checking = psutil.cpu_stats()
        self.messages = {'cpu_stats', checking}
    
    def check_virtual_mem(self):
        mem = psutil.virtual_memory()
        self.messages = {'virtual_memory', mem}

    def disk_space(self):
        disk_usage = shutil.disk_usage("/")
        disk_total = disk_usage.total
        disk_free = disk_usage.used
        total_space = disk_free / disk_total * 100
        if total_space > 20:
            error_message = 'Error --Available disk space is lower than 20%'
            self.messages = {error_message, total_space}
        else:
            self.messages = {'disk_usage:', total_space}
        
    def check_partitions(self):
        partitions = psutil.disk_partitions()
        self.messages = {'partitions:', partitions}

    def input_output(self):
        io = psutil.disk_io_counters()
        self.meessages = {'io:', io}
        
    def check_users(self):
        users = psutil.users()
        self.messages = {str(users), 'usernames'}

class load(healthChecks):
    def __init__(self):
        self.data = {'key', 'value'}

    def run(self):
        #have to look up json docs on how to easily do this.

        pass

    def extract(self):
        pass

    def write(self):
        pass

    def dump(self):
        pass

    
        
def main():
    print("calling main")
    x = healthChecks()
    x.disk_space()
    x.check_cpu_stats()
    
    
    x.check_users()
    print(x.messages)

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(main(),[])

