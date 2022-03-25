import configparser

class Utils:
    '''
    Generic Utils - to read ini file
    '''
    @classmethod
    def getInitFile(self):
        conf = configparser.ConfigParser()
        conf.read('config.ini')
        return conf.get( 'setup', 'INITFILE')

    @classmethod
    def getParamValue(self, configType, paramName):
        '''
        ClassMethod: Reads the ini file parameters
        Input arguments:
        configType :    header within "ini" file
        param      :    specific param within configType
        '''
        conf = configparser.ConfigParser()
        initFile = Utils.getInitFile()
        conf.read(initFile)
        return conf.get( configType, paramName)

if __name__ == '__main__':
    print(Utils.getInitFile())

