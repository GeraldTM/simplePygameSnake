import configparser
from sys import version

def getFig(config):
    figFile = "Settings.config"
    parser = configparser.ConfigParser
    parser.get(figFile,config)
def setFig(config, value):
    figFile = "Settings.config"
    parser = configparser.ConfigParser
    parser.set(figFile, config, value)

def test():
    PYcadeVersion = getFig('Version')
    print(PYcadeVersion)
    setFig('Version','test')

test()