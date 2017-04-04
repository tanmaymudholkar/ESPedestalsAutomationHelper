# TEST = False
TEST = True

class ConfigNode:
    def __init__(self):
        pass

    def readFile(self, path):
        conf = {}
        with open(path, 'r') as confFile:
            for line in confFile:
                # read lines that are in format
                # key = value
                try:
                    conf[line.strip().split()[0]] = line.strip().split()[2]
                except:
                    pass

            for key, value in conf.items():
                setattr(self, key, value)


config = ConfigNode()

config.workdir = '/nfshome0/ecalpro/DQM.new/p5tools'
config.period = 'Run2016'
config.logdir = '/data/dqm-data/logs'
config.tmpoutdir = '/data/dqm-data/tmp'

#config.tmpoutdir = '/data/test'

if TEST:
    config.workdir = ''
    config.period = 'Run2016'
    config.logdir = ''
    config.tmpoutdir = 'outdir'

config.dbwrite = ConfigNode()
if TEST:
    # config.dbwrite.readFile('/nfshome0/ecalpro/DQM.new/.ecal_db_test.conf')
    config.dbwrite.readFile('es_db_test.conf')
else:
    # config.dbwrite.readFile('/nfshome0/ecalpro/DQM.new/.ecal_db_prod.conf')
    config.dbwrite.readFile('es_db_test.conf')

# config.dbread = ConfigNode()
# config.dbread.readFile('/nfshome0/ecalpro/DQM.new/.ecal_db_read.conf')
