import FWCore.ParameterSet.Config as cms

process = cms.Process("ESDQM")

process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load("FWCore.Modules.preScaler_cfi")

# for live online DQM in P5
# process.load("DQM.Integration.config.inputsource_cfi")

# for testing in lxplus
process.load("DQM.Integration.config.fileinputsource_cfi")

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        "file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/00244373-6488-E611-9D3C-02163E013472.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/04A66066-6488-E611-B1CF-FA163E0D264C.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/0AEFF275-6488-E611-865D-02163E0142F9.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/0EBCE863-6488-E611-B60F-FA163E38F4F7.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/0EFD2662-6488-E611-9434-FA163E9790E8.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/1A0EE46E-6488-E611-904F-02163E0144AC.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/1C70D221-6488-E611-988D-02163E011BFF.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/209CAB77-6488-E611-8FA0-02163E011C88.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/229C986A-6488-E611-A5E6-02163E014313.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/2AA62A67-6488-E611-A807-02163E011CA9.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/304BCC6A-6488-E611-B748-02163E0134BF.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/32D54E66-6488-E611-A5DD-02163E014398.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/42522B7A-6488-E611-B63E-02163E01447F.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/44A73D4D-6488-E611-A505-FA163EF6F368.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/44BB436F-6488-E611-B4BE-02163E011BC1.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/4651777B-6488-E611-80BD-02163E013526.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/5297A366-6488-E611-AB9A-FA163E59B229.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/54A1066B-6488-E611-ADC6-02163E0133BF.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/58E21C74-6488-E611-9291-02163E012958.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/5AC3ADD7-6488-E611-910B-02163E0138E2.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/5ACC4C67-6488-E611-9471-FA163E684126.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/5C0D1D68-6488-E611-9940-02163E0145C5.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/6265DAC4-6488-E611-9041-02163E0129E9.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/66DC9E62-6488-E611-8156-FA163E23221A.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/6A81005D-6488-E611-BDBD-FA163E9501BC.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/70783049-6488-E611-9A59-02163E013543.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/74E1ED69-6488-E611-9646-02163E0146EB.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/74FAF8D1-6488-E611-8FC0-FA163ECD93DC.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/7878B872-6488-E611-80E8-02163E011CE6.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/7A61A171-6488-E611-B2CD-02163E0141B7.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/7ECF825F-6488-E611-8BF0-FA163ECCC2C4.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/86C1B86B-6488-E611-8010-02163E0137E4.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/9008DD3C-6488-E611-B5EA-02163E014660.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/9A80B26C-6488-E611-B406-02163E014233.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/9C3BFC60-6488-E611-866D-FA163E9DAC35.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/9C3E0870-6488-E611-AA5B-02163E011D76.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/9EF64B63-6488-E611-9940-FA163E244EB1.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/A0116F69-6488-E611-BA29-FA163EEFD36B.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/A08C7664-6488-E611-BA7A-FA163EE1765D.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/A265F92E-6488-E611-A74F-FA163E5E335E.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/ACBCDD66-6488-E611-B189-02163E0144E8.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/AE498675-6488-E611-956A-02163E014704.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/B09AE671-6488-E611-B039-02163E011F21.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/B2153A6F-6488-E611-9E01-02163E014195.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/B2599368-6488-E611-8330-FA163ED18503.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/B6A6DF61-6488-E611-A2E9-FA163E67322C.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/BE6F3B67-6488-E611-8D85-02163E01429A.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/C24C0968-6488-E611-94BC-02163E01463A.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/C271F678-6488-E611-A798-02163E01339D.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/C8827BD7-6488-E611-BC34-FA163EFE3192.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/CAD3A267-6488-E611-B56B-02163E014690.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/CC98F674-6488-E611-BFA6-02163E0142B1.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/CEA0ED6E-6488-E611-850F-02163E0146CA.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/DE51106D-6488-E611-A271-FA163E8939FD.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/DE6C8B6D-6488-E611-9E12-02163E011C08.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/E053886E-6488-E611-8187-02163E014342.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/E6B1BF6E-6488-E611-8651-02163E0135B6.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/E6EE84DF-6488-E611-BE68-02163E0133DD.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/EE179C06-7D88-E611-8A87-02163E013468.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/EE35F561-6488-E611-90A0-FA163E3C89FD.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/F0017EE2-6488-E611-B81A-02163E011C96.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/F0FF7623-6488-E611-B74A-FA163E04B5D9.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/FA59D862-6488-E611-8677-FA163E77DC86.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/FAD9B76C-6488-E611-849D-02163E0134A9.root",
"file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Run2016H/Cosmics/RAW/v1/000/282/079/00000/FE5A0784-6488-E611-AFDD-02163E014272.root"
        # "root://cms-xrd-global.cern.ch//store/data/Run2016C/Cosmics/RAW/v2/000/275/615/00000/12B57EDB-2639-E611-BC9A-02163E014650.root"
        # "file:///afs/cern.ch/user/t/tmudholk/private/mount/eos_mount/cms/store/data/Commissioning2016/Cosmics/RAW/v1/000/266/668/00000/10A8ACDE-C3E8-E511-AD6A-02163E013785.root"
    )
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(300))

# Condition for P5 cluster
#process.load("DQM.Integration.config.FrontierCondition_GT_cfi")
# Condition for lxplus: change and possibly customise the GT
# from Configuration.AlCa.GlobalTag import GlobalTag as gtCustomise
#process.GlobalTag = gtCustomise(process.GlobalTag, 'auto:run2_data', '')
#Copied from other version
process.load("DQM.Integration.config.FrontierCondition_GT_autoExpress_cfi") 

process.load("EventFilter.ESRawToDigi.esRawToDigi_cfi")
#process.ecalPreshowerDigis = EventFilter.ESRawToDigi.esRawToDigi_cfi.esRawToDigi.clone()
process.esRawToDigi.sourceTag = 'source'
process.esRawToDigi.debugMode = False

process.load('RecoLocalCalo/EcalRecProducers/ecalPreshowerRecHit_cfi')
process.ecalPreshowerRecHit.ESGain = cms.int32(2)
process.ecalPreshowerRecHit.ESBaseline = cms.int32(0)
process.ecalPreshowerRecHit.ESMIPADC = cms.double(50)
process.ecalPreshowerRecHit.ESdigiCollection = cms.InputTag("esRawToDigi")
process.ecalPreshowerRecHit.ESRecoAlgo = cms.int32(0)

process.preScaler.prescaleFactor = 1

#process.dqmInfoES = cms.EDAnalyzer("DQMEventInfo",
#                                   subSystemFolder = cms.untracked.string('EcalPreshower')
#                                   )

#process.load("DQMServices.Core.DQM_cfg")

process.load("DQM.Integration.config.environment_cfi")
process.dqmEnv.subSystemFolder = 'EcalPreshower'

process.load("DQMServices.Components.DQMFileSaver_cfi")
process.dqmSaver.tag = 'EcalPreshower'
# process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/es_reference.root'
# for local test
process.dqmSaver.path = '.'

process.load("DQM/EcalPreshowerMonitorModule/EcalPreshowerMonitorTasks_cfi")
process.ecalPreshowerIntegrityTask.ESDCCCollections = cms.InputTag("esRawToDigi")
process.ecalPreshowerIntegrityTask.ESKChipCollections = cms.InputTag("esRawToDigi")
process.ecalPreshowerIntegrityTask.ESDCCCollections = cms.InputTag("esRawToDigi")
process.ecalPreshowerIntegrityTask.ESKChipCollections = cms.InputTag("esRawToDigi")
process.ecalPreshowerOccupancyTask.DigiLabel = cms.InputTag("esRawToDigi")
process.ecalPreshowerPedestalTask.DigiLabel = cms.InputTag("esRawToDigi")
process.ecalPreshowerRawDataTask.ESDCCCollections = cms.InputTag("esRawToDigi")
process.ecalPreshowerTimingTask.DigiLabel = cms.InputTag("esRawToDigi")
process.ecalPreshowerTrendTask.ESDCCCollections = cms.InputTag("esRawToDigi")

# process.load("DQM/EcalPreshowerMonitorClient/EcalPreshowerMonitorClient_cfi")
process.load("DQM/EcalPreshowerMonitorClient/EcalPreshowerLocalMonitorClient_cfi")
del process.dqmInfoES
process.p = cms.Path(process.preScaler*
               process.esRawToDigi*
               process.ecalPreshowerRecHit*
               process.ecalPreshowerLocalTasksSequence*
               process.dqmEnv*
               process.ecalPreshowerLocalMonitorClient*
               process.dqmSaver)

process.esRawToDigi.sourceTag = cms.InputTag("rawDataCollector")
process.ecalPreshowerRawDataTask.FEDRawDataCollection = cms.InputTag("rawDataCollector")
#--------------------------------------------------
# Heavy Ion Specific Fed Raw Data Collection Label
#--------------------------------------------------

print "Running with run type = ", process.runType.getRunType()

if (process.runType.getRunType() == process.runType.hi_run):
    process.esRawToDigi.sourceTag = cms.InputTag("rawDataRepacker")
    process.ecalPreshowerRawDataTask.FEDRawDataCollection = cms.InputTag("rawDataRepacker")


### process customizations included here
from DQM.Integration.config.online_customizations_cfi import *
process = customise(process)
