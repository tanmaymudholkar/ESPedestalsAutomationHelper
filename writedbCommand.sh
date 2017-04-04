#!/bin/bash

rm *.pyc || echo "No pyc file found"

cmsRun writeESDB_cfg.py inputFiles=DQM_V0003_R000275511__All__Run2016__MiniDAQ.root runType=PEDESTAL
