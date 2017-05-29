#!/usr/bin/env python

import re
import csv
import subprocess

cmd = """wget ftp://ftp.genome.jp/pub/kegg/medicus/disease/disease"""
subprocess.check_output(cmd, shell = True)

cmd = "mv ./disease ./disease.txt"
subprocess.check_output(cmd, shell = True)


diseases = {}
gene_read = 0
hsa_id_regex = re.compile(".*\[HSA:(\d*).*")
with open("disease.txt", "r") as keggfile :
    for line in keggfile :
        line = line.rstrip()
        if line.startswith("NAME") :
            disease_name = line[12:]
            continue
        elif line.startswith("GENE") :
            tmp_hsa_id = re.findall(hsa_id_regex,line)
            # print len(tmp_hsa_id)
            if len(tmp_hsa_id) > 0 :
                diseases[disease_name] = [tmp_hsa_id[0]]
                gene_read = 1
            continue
        elif line[:12] == "            " and gene_read == 1:
            tmp_hsa_id = re.findall(hsa_id_regex,line)
            if len(tmp_hsa_id) > 0 :
                diseases[disease_name].append(tmp_hsa_id[0])
            continue
        elif line[:12] != "            " and gene_read == 1:
            gene_read = 0
            continue
        else :
            continue


for key in diseases.keys() :
    # print type(diseases[key])
    # print(diseases[key])
    # break
    # print(str(key),":",diseases[key])
    print(str(key)+" : "+str(", ".join(diseases[key])) )
    diseases[key] = str(", ".join(diseases[key]))


with open('mycsvfile.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, diseases.keys())
    w.writeheader()
    w.writerow(diseases)

cmd = "/usr/bin/Rscript ./rscript.r"
subprocess.check_output(cmd, shell = True)
