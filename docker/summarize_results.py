#!/usr/bin/env python3

import pandas as pd
#Path to csv files

#read in our two plasmid csv files
main = pd.read_csv("/output/plasforest_platon.csv")
spades = pd.read_csv("/output/plasmidSPAdes_closest_conitg.csv")
#create output file
outfile = open("/output/results_summary.txt", 'w')

spadesCol = []
mainArr = main["SPAdes contig"].to_numpy()
spadesArr = spades[" closest SPAdes contig"].to_numpy()

#remove whitespace
spadesArr = [x.strip(' ') for x in spadesArr]
main.columns = [x.strip(' ') for x in main.columns]
main['platon'] = main["platon"].str.strip(' ')
main["plasforest"] = main["plasforest"].str.strip(' ')

#Map spades contigs to plasmidSpades contigs
for contig in mainArr:
    if contig in spadesArr:
        spadesCol.append("plasmid")
    elif contig not in spadesArr:
        spadesCol.append("chromosome")

#add plasmidSpades to our df
main["plasmidSPAdes"] = spadesCol

#export final datafram
main.to_csv('/output/results.csv')


#calculate counts for chromosomal and plasmid identifications
outfile.write(str(main["platon"].value_counts()))
outfile.write('\n')
outfile.write('\n')
outfile.write(str(main["plasforest"].value_counts()))
outfile.write('\n')
outfile.write('\n')
outfile.write(str(main["plasmidSPAdes"].value_counts()))
outfile.write('\n')
outfile.write('\n')

#calculate overlap between tools
platonPlasforest_overlap = main.loc[(main['platon'] == 'plasmid') & (main['plasforest'] == 'plasmid')]
sum1 = "Platon and PlasForest found "+str(len(platonPlasforest_overlap))+" plasmid sequences in common"
platonSpades_overlap = main.loc[(main['platon'] == 'plasmid') & (main['plasmidSPAdes'] == 'plasmid')]
sum2 = "Platon and plasmidSPAdes found "+str(len(platonSpades_overlap))+" plasmid sequences in common"
plasforestSpades_overlap = main.loc[(main['plasmidSPAdes'] == 'plasmid') & (main['plasforest'] == 'plasmid')]
sum3 = "plasmidSPAdes and PlasForest found "+str(len(plasforestSpades_overlap))+" plasmid sequences in common"
all_overlap = main.loc[(main['platon'] == 'plasmid') & (main['plasforest'] == 'plasmid') & (main['plasmidSPAdes'] == 'plasmid')]
sumall = "Platon, PlasForest and plasmidSPAdes found "+str(len(all_overlap))+" plasmid sequences in common"

#write out results
outfile.write(str(sum1))
outfile.write("\n")
outfile.write(str(sum2))
outfile.write("\n")
outfile.write(str(sum3))
outfile.write("\n")
outfile.write(str(sumall))

outfile.close()
