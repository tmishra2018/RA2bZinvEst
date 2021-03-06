from multiprocessing import Process
import os

#os.environ["DYLD_LIBRARY_PATH"] = "/Users/whitbeck/root_build/lib"
backgroundSamples=["QCD_200to300",
                   "QCD_300to500",
                   "QCD_500to700",
                   "QCD_700to1000",
                   "QCD_1000to1500",
                   "QCD_1500to2000",
                   "QCD_2000toInf",
                   "GJets0p4_100to200",
                   "GJets0p4_200to400",
                   "GJets0p4_400to600",
                   "GJets0p4_600toInf",
                   "TT_600to800",
                   "TT_800to1200",
                   "TT_1200to2500",
                   "TT_2500toInf",
                   "Other_WWTo1L1Nu2Q",
                   "Other_WZTo1L1Nu2Q",
                   "Other_WZTo1L3Nu",
                   "Other_WZZ",
                   "Other_ZZTo2L2Q",
                   "Other_ZZZ",
                   "Other_TTTT",
                   "Other_TTWJetsToLNu",
                   "Other_TTWJetsToQQ",
                   "Other_TTGJets",
                   "Other_TTZToLLNuNu",
                   "Other_TTZToQQ",
                   "Other_ST_s",
                   "Other_ST_t_antitop",
                   "Other_ST_t_top",
                   "Other_ST_tW_antitop",
                   "Other_ST_tW_top"
                   ]

dataSamples=["SinglePhoton_2016B",
             "SinglePhoton_2016C",
             "SinglePhoton_2016D",
             "SinglePhoton_2016E",
             "SinglePhoton_2016F",
             "SinglePhoton_2016G",
             "SinglePhoton_2016H"
             ]
def runPlotPurityProperties(bkg,data):
    print '../bin/plotObs_baseline 2 "{0}" "{1}"'.format(bkg,data)
    os.system('../bin/plotObs_baseline 2 "{0}" "{1}"'.format(bkg,data))

processes=[]
for sample in backgroundSamples : 
    p = Process(target=runPlotPurityProperties, args=(sample, "") )
    p.start()
    processes.append(p)

for sample in dataSamples : 
    p = Process(target=runPlotPurityProperties, args=("", sample) )
    p.start()
    processes.append(p)

for p in processes : 
    p.join()

#os.system("hadd -f plotObs_photon_baseline.root plotObs_photon_baseline_*.root")
#os.system("rm plotObs_photon_baseline_*.root")
    
    


