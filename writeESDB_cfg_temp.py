import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

import os

# REMEMBER TO CHANGE !!!!!!!
# from esdqmconfig import config

options = VarParsing('analysis')
# options.register('generalTag', default = 'GLOBAL', mult = VarParsing.multiplicity.singleton, mytype = VarParsing.varType.string)
# options.register("laserWavelengths", mult = VarParsing.multiplicity.list, mytype = VarParsing.varType.int, info = "Laser wavelengths")
# options.register("ledWavelengths", mult = VarParsing.multiplicity.list, mytype = VarParsing.varType.int, info = "LED wavelengths")
# options.register("MGPAGains", mult = VarParsing.multiplicity.list, mytype = VarParsing.varType.int, info = "MGPA gains")
# options.register("MGPAGainsPN", mult = VarParsing.multiplicity.list, mytype = VarParsing.varType.int, info = "PN MGPA gains")
# options.register("runType",default = "COSMIC", mult = VarParsing.multiplicity.singleton, mytype = VarParsing.varType.string)
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
# process.ESCondDBWriter.location = 'P5_Co'
# process.ESCondDBWriter.runType = options.runType 
# process.ESCondDBWriter.runGeneralTag = options.generalTag
# process.ESCondDBWriter.monRunGeneralTag = 'CMSSW-offline-private'
process.ESCondDBWriter.inputRootFiles = cms.untracked.vstring(options.inputFiles)
process.ESCondDBWriter.verbosity = 2

process.load("DQMServices.Core.DQM_cfg")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
#process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")
#process.load("Geometry.CaloEventSetup.CaloTopology_cfi")
#process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")
#process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
#process.load("Geometry.EcalMapping.EcalMapping_cfi")
#process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")

process.load("DQM.Integration.config.FrontierCondition_GT_cfi")

# process.MessageLogger = cms.Service('MessageLogger',
#     destinations = cms.untracked.vstring('cout'),
#     categories = cms.untracked.vstring('ESDQM'),
#     cout = cms.untracked.PSet(
#         threshold = cms.untracked.string('INFO'),
#         ESDQM = cms.untracked.PSet(
#             limit = cms.untracked.int32(-1)
#         ),
#         default = cms.untracked.PSet(
#             limit = cms.untracked.int32(0)
#         )
#     )
# )
process.p = cms.Path(process.ESCondDBWriter)
