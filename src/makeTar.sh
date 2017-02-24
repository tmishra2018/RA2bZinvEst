#!/bin/bash

cd $CMSSW_BASE/../
tar -cf workingArea.tar CMSSW_7_4_2 --exclude='*.dag.*' --exclude='*tar' --exclude='CMSSW_7_4_2/RA2bZinvEst/src/*root' --exclude='*eps' --exclude='*png' --exclude='*pdf' --exclude='*stdout' --exclude='*stderr' --exclude='*condor' --exclude='CMSSW_7_4_2/RA2bZinvEst/bin/*'
mv workingArea.tar CMSSW_7_4_2/src/RA2bZinvEst/src/.