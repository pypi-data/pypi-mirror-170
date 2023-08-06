import json
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import pandas as pd
import os
from matplotlib.backends.backend_pdf import PdfPages
from textwrap import wrap
from pymol import cmd
import cv2 as cv
import glob
import sys
import time
import pymol
import math

def getscores(rankby):

    proteinA_lst=[]
    proteinB_lst=[]
    uniprotA_lst=[]
    uniprotB_lst=[]
    iptmhighscore_lst = []
    ptmhighscore_lst = []
    pdbname_lst = []
    paepng_lst = []
    paejson_lst = []
    
    existuniprot = False
    #get uniprots
    if os.path.exists("uniprots.txt"):
        existuniprot = True
    uniprotlst = []
    if existuniprot:
        with open("uniprots.txt") as f:
            lines=f.readlines()
        for l in lines:
            uniprotlst.append([l.split(":")[0], l.split(":")[1].replace("\n","")])
        #print(uniprotlst)

    #get all data
    for scorepath in Path('results').rglob('scores.txt'):

        resultname = str(scorepath.parent).split("/")[-1]
            
        try:
            next(Path('results/'+resultname).glob("*rank*.pdb"))
        except StopIteration:
            print("\n>> Warning: skipping " + resultname + " since it is missing PDB files.")
            continue
            
        try:
            next(Path('results/'+resultname).glob("*_scores.json"))
            scorewildcard="_scores.json"
        except StopIteration:
            try:
                next(Path('results/'+resultname).glob("*_pae.json"))
                scorewildcard="_pae.json"
            except StopIteration:
                print("\n>> Warning: skipping " + resultname + " since it is missing the scores json files.")
                continue

        try:
            next(Path('results/'+resultname).glob("*PAE*.png"))
            for path in Path('results/'+resultname).glob("*PAE*.png"):
                paepng_lst.append(str(path))
        except StopIteration:
            paepng_lst.append("-")

        with open(scorepath) as f:
            lines=f.readlines()
            iptms=[float(x.split(' ')[0].split(":")[1]) for x in lines]
            ptms=[float(x.split(' ')[1].split(":")[1]) for x in lines]
        
        #if len(lines) == 0:
        #    continue
        
        if rankby=="iptm":
            m = np.argmax(iptms)
        elif rankby=="ptm":
            m = np.argmax(ptms)
        else:
            sys.exit("\n>> Provide ptm or iptm as the ranking method.\n")

        iptmhighscore_lst.append(iptms[m])
        ptmhighscore_lst.append(ptms[m])
        
        #resultname = str(scorepath.parent).split("/")[-1]
        ProteinA=resultname.split("-")[0]
        ProteinB=resultname.split("-")[1]
        ProteinAmin=ProteinA.split("_")[0]+"_"+ProteinA.split("_")[1]
        ProteinBmin=ProteinB.split("_")[0]+"_"+ProteinB.split("_")[1]
        proteinA_lst.append(ProteinA)
        proteinB_lst.append(ProteinB)

        modelnumlst = []
        pdbpaths = []
        for path in Path('results/'+resultname).glob("*rank*.pdb"):
            pdbpaths.append(str(path))
            modelnum = str(path).split("model_")[-1].split(".pdb")[0].split("_")[0]
            modelnumlst.append(int(modelnum)-1) #-1 is to turn it into index (0-4) since numbers are 1-5
         
        modelindex = modelnumlst.index(m)
        
        pdbname = pdbpaths[modelindex]
        pdbname_lst.append(pdbname)

        if scorewildcard == "_scores.json":
            for path in Path('results/'+resultname).glob(pdbname.split("/")[-1][:-4]+scorewildcard):
                paejson_lst.append(str(path))
        elif scorewildcard == "_pae.json":
            for path in Path('results/'+resultname).glob("rank_*_model_"+modelnum+"_ptm_seed_0"+scorewildcard):
                paejson_lst.append(str(path))
        
        if existuniprot:
            foundA=False
            foundB=False
            for u in uniprotlst:
                if u[1] == ProteinAmin and not foundA:
                    uniprotA_lst.append(u[0])
                    foundA=True
                if u[1] == ProteinBmin and not foundB:
                    uniprotB_lst.append(u[0])
                    foundB=True
                if foundA and foundB:
                    break
            if not foundA:
                print("Could not find uniprot ID for " + ProteinAmin)
            if not foundB:
                print("Could not find uniprot ID for " + ProteinBmin)
                
    if not existuniprot:
        uniprotA_lst = ["-"] * len(proteinA_lst)
        uniprotB_lst = ["-"] * len(proteinB_lst)
     
    dimerized = glob.glob('dimerized*')
    
    if len(dimerized) > 0:
        dimerized_uniprot_lst = [dimerized[0].split("/")[-1].split("-")[1]]*len(proteinA_lst)
        dimerized_name_lst = [dimerized[0].split("/")[-1].split("-")[2]]*len(proteinA_lst)
    else:
        dimerized_uniprot_lst = ["-"]*len(proteinA_lst)
        dimerized_name_lst = ["-"]*len(proteinA_lst)
            
    #print(len(proteinA_lst), len(proteinB_lst), len(iptmhighscore_lst), len(ptmhighscore_lst), len(pdbname_lst), len(paepng_lst), len(paejson_lst))

    df = pd.DataFrame(
        {'Protein A': proteinA_lst,
         'Protein B': proteinB_lst,
         'iptm': iptmhighscore_lst,
         'ptm': ptmhighscore_lst,
         'Model': pdbname_lst,
         'PAE-png': paepng_lst,
         'PAE-json': paejson_lst,
         'Dimerized-protein': dimerized_name_lst,
         'Dimerized-uniprot': dimerized_uniprot_lst,
         'SWISS-PROT Accessions Interactor A' : uniprotA_lst,
         'SWISS-PROT Accessions Interactor B' : uniprotB_lst
        })
        
    df.sort_values(by=[rankby], ascending=False, ignore_index=True, inplace=True)

    return(df)

def make_paeplot(pae, protnames, protlens):
    
    plt.imshow(pae, vmin=0, vmax=30, cmap="bwr")
    currlen=0
    yticklocs = []
    newprotnames = []
    for i, p in enumerate(protnames):
        newprotnames.append(p.split("_")[0]+"\n"+p.split("_")[2]+"-"+p.split("_")[3])
        
    for n, l in zip(protnames, protlens):
        
        yticklocs.append(int(l/2)+currlen)
        
        currlen = currlen + l
        
        plt.axvline(x=currlen, color='k')
        plt.axhline(y=currlen, color='k')
    
    plt.xlim(1, currlen)
    plt.ylim(1, currlen)
    plt.yticks(yticklocs, newprotnames, rotation='horizontal')
    plt.gca().invert_yaxis()
    
    return(plt)
    

def getinfo_frompaename(paejson):

    scores = json.loads(Path(paejson).read_text())

    pae = scores["pae"]            

    nameA = str(paejson).split("results/")[1].split("/")[0].split("-")[0]
    nameB = str(paejson).split("results/")[1].split("/")[0].split("-")[1]
    fasta=str(paejson).split("results/")[0]+"fastas/"+nameA+"-"+nameB+".fasta"
    with open(fasta, 'r') as f:
        lines = f.readlines()
    protnames = []
    protlens = []
    for i, a in enumerate(lines):
        if a[0]==">":
            protnames.append(a[1:])
            protlens.append(len(lines[i+1]))
    #lenprotA = int(nameA.split("_")[-1]) - int(nameA.split("_")[-2]) + 1
    #lenprotB = int(nameB.split("_")[-1]) - int(nameB.split("_")[-2]) + 1
    #nameprotA = nameA.split("_")[0] + " " + nameA.split("_")[1] + "\n" + nameA.split("_")[2]+ "-" + nameA.split("_")[3]
    #nameprotB = nameB.split("_")[0] + " " + nameB.split("_")[1] + "\n" + nameB.split("_")[2]+ "-" + nameB.split("_")[3]
    
    return(pae, protnames, protlens)

def getinfo_frompaename_legacy(paejson):

    scores = json.loads(Path(paejson).read_text())

    pae = scores[0]["distance"]
    splitby = int(math.sqrt(len(pae)))
    pae = [pae[i:i + splitby] for i in range(0, len(pae), splitby)]

    nameA = str(paejson).split("results/")[1].split("/")[0].split("-")[0]
    nameB = str(paejson).split("results/")[1].split("/")[0].split("-")[1]
    fasta=str(paejson).split("results/")[0]+"fastas/"+nameA+"-"+nameB+".fasta"
    with open(fasta, 'r') as f:
        lines = f.readlines()
    protnames = []
    protlens = []
    for i, a in enumerate(lines):
        if a[0]==">":
            protnames.append(a[1:])
            protlens.append(len(lines[i+1]))

    #lenprotA = int(nameA.split("_")[-1]) - int(nameA.split("_")[-2]) + 1
    #lenprotB = int(nameB.split("_")[-1]) - int(nameB.split("_")[-2]) + 1
    #nameprotA = nameA.split("_")[0] + " " + nameA.split("_")[1] + "\n" + nameA.split("_")[2]+ "-" + nameA.split("_")[3]
    #nameprotB = nameB.split("_")[0] + " " + nameB.split("_")[1] + "\n" + nameB.split("_")[2]+ "-" + nameB.split("_")[3]
    
    return(pae, protnames, protlens)

# def showpae(paejson):

#     pae, protnames, protlens = getinfo_frompaename(paejson)
#     plt = make_paeplot(pae, protnames, protlens)
#     plt.show()
#     return(len(protnames))
    
def summarize_pae_pdf(df, threshold, rankby):
    
    if threshold == 0:
        pdfname = "PAEs.pdf"
    else:
        pdfname = "PAEs-"+rankby+"-above-" + str(threshold).replace(".", "p") + ".pdf"
    
    print("\n>> Writing " + pdfname)

    with PdfPages(pdfname) as pdf:
        for i, result in df[df[rankby]>threshold].iterrows():
            try:
                pae, protnames, protlens = getinfo_frompaename(result["PAE-json"])
            except:
                try:
                    pae, protnames, protlens = getinfo_frompaename_legacy(result["PAE-json"])
                except:
                    sys.exit("\n>> Could not interpret the PAE json file.\n")
            plt = make_paeplot(pae, protnames, protlens)
            plt.title("\n".join(wrap(result["Model"], 80)), fontsize=8)
            pdf.savefig()
            plt.close('all')

# def show_pdb(modelname, chains, show_sidechains, show_mainchains=False, color="chain"):
    
#     view = py3Dmol.view(js='https://3dmol.org/build/3Dmol.js',)
#     view.addModel(open(modelname,'r').read(),'pdb')

#     if color == "lDDT":
#         view.setStyle({'cartoon': {'colorscheme': {'prop':'b','gradient': 'roygb','min':50,'max':90}}})
#     elif color == "rainbow":
#         view.setStyle({'cartoon': {'color':'spectrum'}})
#     elif color == "chain":
#         #chains = len(queries[0][1]) + 1 if is_complex else 1
#         for n,chain,color in zip(range(chains),list("BCDEFGH"),
#                          ["cyan", "magenta", "orange", "yellow"]): #"["lime","cyan","magenta","yellow","salmon","white","blue","orange"]"
#             view.setStyle({'chain':chain},{'cartoon': {'color':color}})
#     if show_sidechains:
#         BB = ['C','O','N']
#         view.addStyle({'and':[{'resn':["GLY","PRO"],'invert':True},{'atom':BB,'invert':True}]},
#                             {'stick':{'colorscheme':f"WhiteCarbon",'radius':0.3}})
#         view.addStyle({'and':[{'resn':"GLY"},{'atom':'CA'}]},
#                             {'sphere':{'colorscheme':f"WhiteCarbon",'radius':0.3}})
#         view.addStyle({'and':[{'resn':"PRO"},{'atom':['C','O'],'invert':True}]},
#                             {'stick':{'colorscheme':f"WhiteCarbon",'radius':0.3}})  
#     if show_mainchains:
#         BB = ['C','O','N','CA']
#         view.addStyle({'atom':BB},{'stick':{'colorscheme':f"WhiteCarbon",'radius':0.3}})
        
#     nameA = str(modelname).split("results/")[1].split("/")[0].split("-")[0]
#     nameB = str(modelname).split("results/")[1].split("/")[0].split("-")[1]
#     lenprotA = int(nameA.split("_")[-1]) - int(nameA.split("_")[-2]) + 1
#     lenprotB = int(nameB.split("_")[-1]) - int(nameB.split("_")[-2]) + 1
#     nameprotA = nameA.split("_")[0] + " " + nameA.split("_")[1] + "\n" + nameA.split("_")[2]+ "-" + nameA.split("_")[3]
#     nameprotB = nameB.split("_")[0] + " " + nameB.split("_")[1] + "\n" + nameB.split("_")[2]+ "-" + nameB.split("_")[3]
#     #view.addLabel(nameprotA,{'fontOpacity':1, 'fontSize':12, 'fontColor':'black','backgroundOpacity':0.2, 'backgroundColor':'cyan'},{'resi':1})
#     #view.addLabel(nameprotB,{'fontOpacity':1, 'fontSize':12, 'fontColor':'black','backgroundOpacity':0.2, 'backgroundColor':'magenta'},{'resi':lenprotA+10})

#     view.zoomTo()
#     return view

def write_top(df, threshold, rankby):
    
    if threshold == 0:
        basename = "Results"
    else:
        basename = "Results-"+rankby+"-above-" + str(threshold).replace(".", "p")
        
    excelname = basename + ".xlsx"
    csvname = basename + ".csv"
    
    with pd.ExcelWriter(excelname) as writer:  
        df[df[rankby]>threshold].to_excel(writer)
        
    df.to_csv(csvname)
    
    print("\n>> Wrote " + excelname + " and " + csvname)
        
        
def write_modelpngs(df, threshold, rankby, overwrite=False):

    print("\n>> Writing model snapshots...")

    pymol.finish_launching(['pymol', '-qc']) #-Q will suppress render outputs too

    total=0

    for i,result in df[df[rankby]>threshold].iterrows():
        
        model=result["Model"]
        png1 = model[:-4]+".png"
        png2 = model[:-4]+"-rotated.png"
        
        if not overwrite and os.path.exists(png1) and os.path.exists(png2):
            continue

        if os.path.exists(png1):
            os.rename(png1, model[:-4]+"-backup.png")
        
        cmd.load(model, "current")
        cmd.cartoon("automatic")
        cmd.bg_color("white")
        #cmd.ray(600,600)
        #cmd.draw(300,300,antialias=2)
        cmd.zoom()
        cmd.util.cbc()
        cmd.png(png1, width=600, height=600, dpi=900)

        waitfor(png1)

        if not os.path.exists(png1):
            if os.path.exists(model[:-4]+"-backup.png"):
                os.rename(model[:-4]+"-backup.png", png1)
            sys.exit("\n>> Error: pymol didn't output anything.\nFailed on: "+model+"\n")
        elif os.path.exists(model[:-4]+"-backup.png"):
            os.remove(model[:-4]+"-backup.png")
        
        cmd.rotate(axis='x',angle=90)
        cmd.rotate(axis='y',angle=90)
        cmd.zoom()
        cmd.png(png2, width=600, height=600, dpi=900)

        waitfor(png2)

        cmd.delete("current")
        
        total+=1
        
    #print("\n>> Wrote png-snapshots for " + str(total) + " pdbs.")
        
def waitfor(filename):
    pngexists=False
    tic = time.perf_counter()
    while not pngexists:
        if os.path.exists(filename):
            pngexists=True
        time.sleep(0.25)
        toc = time.perf_counter()
        if toc-tic > 3:
            sys.exit("\n>> Error: pymol didn't output anything in 3 seconds for file:\n"+filename)
    
def summarize_paeandmodel_pdf(df, threshold, rankby):
    
    if threshold == 0:
        pdfname = "PAEs-Models.pdf"
    else:
        pdfname = "PAEs-Models-"+rankby+"-above-"+ str(threshold).replace(".", "p") + ".pdf"
    
    print("\n>> Writing " + pdfname + "\n")

    with PdfPages(pdfname) as pdf:
        for i, result in df[df[rankby]>threshold].iterrows():
            
            plottitle = [result["Model"],"iptm: "+str("{:.2f}".format(result["iptm"])),"ptm: "+str("{:.2f}".format(result["ptm"])),result["Protein A"]+" ("+result["SWISS-PROT Accessions Interactor A"]+")",result["Protein B"]+" ("+result["SWISS-PROT Accessions Interactor B"]+")"]
            if result["Dimerized-protein"] != "-":
                plottitle.append("Dimerized: " + result["Dimerized-protein"])
            plottitle = "\n".join(plottitle)
            
            try:
                pae, protnames, protlens = getinfo_frompaename(result["PAE-json"])
            except:
                try:
                    pae, protnames, protlens = getinfo_frompaename_legacy(result["PAE-json"])
                except:
                    sys.exit("\n>> Could not interpret the PAE json file.\n")

            fig = plt.figure(figsize=(60,20))
            fig.suptitle(plottitle, fontsize=28)
            plt.subplot(1, 3, 1)
            make_paeplot(pae, protnames, protlens)
            plt.xticks(fontsize=36)
            plt.yticks(fontsize=36)

            png1 = result["Model"][:-4]+".png"
            png2 = result["Model"][:-4]+"-rotated.png"
            
            if not os.path.exists(png1):
                sys.exit("\n>> Error: The model snapshots could not be found.\n")
            elif not os.path.exists(png2):
                sys.exit("\n>> Error: The model snapshots could not be found.\n")
            
            plt.subplot(1, 3, 2)
            img1=plt.imread(png1)
            plt.axis('off')
            #img1=cv.imread(png1)
            plt.imshow(img1)
            
            plt.subplot(1, 3, 3)
            img2=plt.imread(png2)
            plt.axis('off')
            plt.imshow(img2)
            
            pdf.savefig()
            plt.close('all')

    print(">> If there is an error below, ignore it." + "\n")
