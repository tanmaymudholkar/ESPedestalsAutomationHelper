import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

import os

from esdqmconfig import config

options = VarParsing('analysis')
options.register('generalTag', default = 'GLOBAL', mult = VarParsing.multiplicity.singleton, mytype = VarParsing.varType.string)
options.register("runType",default = "COSMIC", mult = VarParsing.multiplicity.singleton, mytype = VarParsing.varType.string)
options.parseArguments()

os.environ["TNS_ADMIN"] = "/etc"

process =  cms.Process("DQMDB")

process.source = cms.Source("EmptySource")

process.load("DQM.ESMonitorDbModule.ESCondDBWriter_cfi")
# process.ESCondDBWriter.DBName = config.dbwrite.dbName
# process.ESCondDBWriter.userName = config.dbwrite.dbUserName
# process.ESCondDBWriter.password = config.dbwrite.dbPassword
# process.ESCondDBWriter.hostName = config.dbwrite.dbHostName
# process.ESCondDBWriter.hostPort = int(config.dbwrite.dbHostPort)
process.ESCondDBWriter.location = 'P5_Co'
process.ESCondDBWriter.runType = options.runType 
process.ESCondDBWriter.runGeneralTag = options.generalTag
process.ESCondDBWriter.monRunGeneralTag = 'CMSSW-offline-private'
process.ESCondDBWriter.inputRootFiles = cms.untracked.vstring(options.inputFiles)
process.ESCondDBWriter.verbosity = 2

process.load("DQMServices.Core.DQM_cfg")
process.DQMStore.verbose = 5

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("DQM.Integration.config.FrontierCondition_GT_cfi")
# process.load("DQM.Integration.config.FrontierCondition_GT_autoExpress_cfi")
# from Configuration.StandardSequences.FrontierConditions_GlobalTag_cff import *
# from Configuration.AlCa.GlobalTag import GlobalTag as gtCustomise
# GlobalTag = gtCustomise(GlobalTag, 'auto:run2_data', '')

process.MessageLogger = cms.Service('MessageLogger',
    destinations = cms.untracked.vstring('cout'),
    categories = cms.untracked.vstring('ESDQM'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO'),
        ESDQM = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    )
)
process.p = cms.Path(process.ESCondDBWriter)
