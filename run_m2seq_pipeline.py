#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import RawTextHelpFormatter
import os
import numpy as np

def argument_parser():

    parser = argparse.ArgumentParser(description=__doc__, prog='run_m2seq_pipeline.py', formatter_class=RawTextHelpFormatter)
    parser.add_argument("-s", "--seq_in", required=True, dest="seq_in",
                        help="File with sequence in FASTA format.")
    parser.add_argument("-f", "--filename", dest="fastq_file",    nargs='+',
                        help="Names of fastq files")
    parser.add_argument("-o", "--offset", required=False, dest="offset_in", default=0)

    args = parser.parse_args() 

    seq_in = args.seq_in
    fastq_in = args.fastq_file
    offset_in = args.offset_in
    
    return seq_in, fastq_in, offset_in


def run_m2seq():

    name = fastq_in[0].rstrip("_L001_R1_001.fastq")
    cfg_name = seq_in.replace("fa","cfg")
    os.system("mkdir " + name)


    cfg_command = name+':'
    str_command = "m2seq_mod.py " + seq_in 
    cp_command = ""
    for i in range(0, len(fastq_in)):
        cfg_command += ' '+fastq_in[i] + ','
        str_command += ' '+fastq_in[i]
        cp_command += fastq_in[i] +' '
    cfg_command = cfg_command.rstrip(",") + " = " + seq_in.rstrip(".fa")
    create_cfg_file(cfg_command, cfg_name)

    str_command += " --config " +cfg_name + " --offset " + str(offset_in)
    print str_command
    
    
    cp_command += seq_in + " " + cfg_name
    os.system("cp " + cp_command + " ./" + name)
#    os.system("cd ./" + name +"/ | "+str_command)
    os.chdir(name)
    os.system(str_command)



def create_cfg_file(cfg_str, cfg_name):
    
    config_text = '# ShapeMapper version 1.2 example config file (Copyright Steven Busan 2015)\n\
# Modified for analysis of mutate-and-map-seq experiments by Clarence Cheng, 2016\n\
# Example data can be downloaded with MaP2D scripts at https://github.com/DasLab/MaP2D\n\
#\n\
# Comments are indicated by "#" and ignored\n\
# The following are equivalent: "on","ON","On","True","TRUE","T","true"\n\
# These are also equivalent: "off","OFF","Off","False","FALSE","F","false"\n\
#==================================================================================\n\
# GPL statement:\n\
#\n\
# This file is part of Shapemapper.\n\
#\n\
# ShapeMapper is free software: you can redistribute it and/or modify\n\
# it under the terms of the GNU General Public License as published by\n\
# the Free Software Foundation, either version 3 of the License, or\n\
# (at your option) any later version.\n\
#\n\
# ShapeMapper is distributed in the hope that it will be useful,\n\
# but WITHOUT ANY WARRANTY; without even the implied warranty of\n\
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n\
# GNU General Public License for more details.\n\
#\n\
# You should have received a copy of the GNU General Public License\n\
# along with ShapeMapper.  If not, see <http://www.gnu.org/licenses/>.\n\
#==================================================================================\n\
# ShapeMapper stages to run\n\
\n\
buildIndex = on\n\
trimReads = on\n\
alignReads= on\n\
parseAlignments = on\n\
countMutations = on\n\
pivotCSVs = on\n\
makeProfiles = on\n\
foldSeqs = off\n\
renderStructures = off\n\
\n\
#=================================================================================\n\
# Global run options\n\
\n\
# trimReads options\n\
minPhred = 0\n\
windowSize = 1\n\
minLength = 25\n\
\n\
# alignReads options\n\
alignPaired = True # align using paired-end information\n\
                   # This option also affects the parseAlignments stage\n\
\n\
maxInsertSize = 500 # bowtie2 maximum insert size for valid paired-end alignments\n\
\n\
# countMutations options\n\
randomlyPrimed = off # If on, primerLength+1 nucs from the 3-prime end of each \n\
                     # read will be excluded from analysis\n\
primerLength = 10 # Length of random n-mers used to prime reverse transcription\n\
                  # (Only used if randomlyPrimed is on)\n\
trimBothEnds = off # If on, a region primerLength+1 will also be excluded from\n\
                   # the 5-prime end of each read.  This is needed when the sense\n\
                   # of the RNA is not consistently known (e.g. transcriptome).\n\
minMapQual = 30  # Reads with mapping qualities below this threshold will be ignored\n\
                 # Summary from Bowtie2 docs:\n\
                 # Mapping quality = -10*log10(probability mapping position is wrong)\n\
                 # A mapping quality of 10 corresponds to a 1 in 10 probability that a \n\
                 # read actually matches another location.\n\
minPhredToCount = 20 # individual read nucleotides with associated basecall quality \n\
                    # scores below this threshold will be ignored\n\
makeOldMutationStrings = on # make mutation strings compatible with single-molecule scripts\n\
                             # these will be written to output/mutation_strings_filtered/\n\
\n\
# makeProfiles options\n\
normProfile = on # Normalize profile using boxplot or outlier exclusion for short sequences\n\
filterStderr = off # Exclude nucs whose stderrs exceed abs(shape)*0.5+0.4\n\
maxBackground = 0.05 # Exclude nucs whose background mutation rates exceed this value\n\
minDepth = 10 # Exclude nucs whose read depth in any condition is less than this value\n\
minNormDepth = 0 # Exclude nucs from calculation of normalization factor whose read\n\
                 # depth in any condition is less than this value. This is especially\n\
                 # useful for transcriptome datasets in which large portions of the\n\
                 # reference sequence are uncovered. 5000 is a reasonable value.\n\
ignoreDeletions = off # Do not count deletions when generating reactivity profiles.\n\
\n\
# foldSeqs options\n\
slope = 1.8 \n\
intercept = -0.6\n\
\n\
#===================================================================================\n\
# If enabled - filenames, paths, and sample names will not be checked for consistency\n\
# Only for advanced users\n\
devMode = off\n\
\n\
#===================================================================================\n\
# Specify which RNAs are present in each pair of FASTQ files. FASTQ file sample\n\
# names on left, comma-separated alignment target sequence names on right.\n\
\n\
[alignments] # do not change this line\n\
\n\
# Alternative syntax (specify full FASTQ filenames) - name to the left of colon is \n\
# user-specified. Using this syntax, the fastq filenames do not need to match \n\
# Illumina convention.\n\
\n\
'+ cfg_str + '\n' + \
'\n\
\n\
#===================================================================================\n\
# Specify which files correspond to the three experimental conditions\n\
# (SHAPE-modified, untreated, and denatured control) and name each reactivity\n\
# profile to be output.\n\
\n\
[profiles] # do not change this line\n\
\n\
\n\
#====================================================================================\n\
# SHAPE profiles and associated sequences to fold (using RNAStructure) and render\n\
# (using pvclient.py and Pseudoviewer).\n\
\n\
[folds] # do not change this line\n\n\
'

    cfg_file = open(cfg_name, "w")
    cfg_file.write(config_text)
    cfg_file.close()
    


if __name__ == '__main__':

    seq_in, fastq_in, offset_in = argument_parser()

    run_m2seq()
    
    
    
    
        

    
