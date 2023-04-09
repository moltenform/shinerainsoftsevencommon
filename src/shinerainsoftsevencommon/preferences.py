
import os
import re
import tempfile
from configparser import ConfigParser

#~ softDeleteFile:
#~ if no location is set, send to recycle bin (Send2Trash module) (and log what was deleted to ~/.ben_python_common.log)
#~ otherwise send it to that location
#~ or if location is set per-drive, send to that place.

#~ scratchLocation:
#~ if no location is set, use a temporary location in c:\temp
#~ or if location is set per-drive, send to that place.





class SimpleConfigParser:
    def __init__(self, addDefaultSection='main'):
        self.prefs_dict = {}
        self.addDefaultSection = addDefaultSection
    
    def load(self, path):
        with open(path, encoding='utf-8') as f:
            prefs_contents = f.read()
            
            if self.addDefaultSection:
                expect = '[' + self.addDefaultSection + ']\n'
                if expect not in prefs_contents:
                    prefs_contents = expect + '\n' + prefs_contents
            
            self.cfg = configparser.ConfigParser(delimiters='=')
            
            # make it case-sensitive
            self.cfg.optionxform = str
            self.cfg.read_string(prefs_contents)
            
            for key in self.cfg:
                self.prefs_dict[key] = self.cfg[key]
    
    def getDict(self):
        return self.prefs_dict
        

class BenPythonCommonPreferences:
    def __init__(self):
        self.prefs_dict = {}
    
    def load(self):
        userHome = os.path.expanduser('~')
        userPrefsFile = userHome + '/' + '.shinerainsoftsevencommon'
        
        def go(f):
    
    
    dir = cfg['main']

def runOnModuleLoad(cachedPrefs):
    

def _getDirRoot(path):
    path = os.path.abspath(path)
    if re.match(r'^[a-zA-Z]:$', path[0:2]):
        return path[0].lower()
    else:
        return None

def getDirectoryBasedOnPath(path, prefix):
    global cachedPrefs
    dict = cachedPrefs.getDict()
    
    root = _getDirRoot(path)
    if root:
        key = f'{prefix}_{root}_drive'
        if key in dict and dict[key]:
            return dict[key]
    
    key = f'{prefix}_general'
    if key in dict and dict[key]:
        return dict[key]
    

# run this on module load
cachedPrefs = BenPythonCommonConfigParser()
runOnModuleLoad(cachedPrefs)

def getTempDirectoryForPath(path):
    # always returns a valid directory
    result = getDirectoryBasedOnPath(path, 'temp_directory')
    if not result:
        result = tempfile.gettempdir() + '/shinerainsoftsevencommon'
        
    try:
        if not os.path.isdir(result):
            os.makedirs(result)
    except Exception as e:
        raise Exception(f'getTempDirectoryForPath error creating {result} {e}')
    
    if not os.path.isdir(result):
        raise Exception('getTempDirectoryForPath does not exist {result}')
    
    return result
    
def getSoftDeleteDirectoryForPath(path):
    # returns a directory, or None
    result = getDirectoryBasedOnPath(path, 'soft_delete_directory')
    if result:
        try:
            if not os.path.isdir(result):
                os.makedirs(result)
        except Exception as e:
            raise Exception(f'getSoftDeleteDirectoryForPath creating {result} {e}')
        
        if not os.path.isdir(result):
            raise Exception('getSoftDeleteDirectoryForPath does not exist {result}')
    
    return result
    


