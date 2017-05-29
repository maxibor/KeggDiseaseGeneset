# KEGG Diseases GeneSet

Creating the **Mutations** (not Differential expression) Genesets from [KEGG medicus diseases Pathways](ftp://ftp.genome.jp/pub/kegg/medicus/disease/disease) (1328 disease on 21/04/2017)

- Data parsing/scrapping with [Python](./kegg_disease_geneset.py) and output [csv](./mycsvfile.csv)
- Conversion to [R](rscript.r) list and saved as [Rdata](./keggDiseasesGeneset.RData)

### How to use it :

`python kegg_disease_geneset.py`

### Output :

`keggDiseasesGeneset.RData`
