import os
import glob
import re

class DirectoryManager():

    def __init__(self, path):

        self.path = path
        self.list_users_dirs = []


    def get_users_dir(self):

        dir_list = glob.glob(os.path.join(self.path, '*'))
        # remove database file from list
        regex = re.compile(r'.*\.db')
        self.list_users_dirs = [i for i in dir_list if not regex.search(i)]

    def clean_users_dirs(self):
        
        for user_dir in self.list_users_dirs:
            self.clean_directory(user_dir + '/rdf')
            self.clean_directory(user_dir + '/result')
            self.clean_directory(user_dir + '/upload')

    def clean_directory(self, path):

        if os.path.isdir(path):
            for file in os.listdir(path):
                if os.path.isfile(path + '/' + file):
                    os.unlink(path + '/' + file)