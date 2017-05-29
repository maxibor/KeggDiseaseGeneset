dt = read.csv("./mycsvfile.csv")

keggDiseasesGeneset = list()
for (i in (seq(1, length(colnames(dt))))){
  keggDiseasesGeneset[[colnames(dt)[i]]] = as.integer(strsplit(as.character(dt[1,i]),", ")[[1]])
}

save(keggDiseasesGeneset, file = "./keggDiseasesGeneset.RData")
