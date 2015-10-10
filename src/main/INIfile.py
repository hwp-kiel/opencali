import configparser
import os

class IniFile:
     def read(self, startSettings, ini):
         filename = os.path.join(startSettings,'opencali.ini')
         if not os.path.isfile(filename):
             return
         config = configparser.ConfigParser()
         config.read(os.path.join(startSettings,'opencali.ini'))
         config_paths = config['Paths']

         ini.paths.projects = config_paths['projects']
         ini.paths.lastproject = config_paths['lastproject']



     def write(self, startSettings, ini):
         config = configparser.ConfigParser()
         config['Paths'] = {'projects': ini.paths.projects,
                            'lastproject': ini.paths.lastproject,
                            'samples': ini.paths.samples}

         filename = os.path.join(startSettings,'opencali.ini')
         with open(filename, 'w') as configfile:
              config.write(configfile)


class Ini:
    def __init__(self):
        self.paths = Paths()

class Paths:
    def __init__(self):
        self.projects = 'blabla'
        self.lastproject = 'sdhghg'
        self.samples = 'samples'
