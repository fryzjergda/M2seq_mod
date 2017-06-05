# M2seq

Analysis of 2D signal in mutational profiling sequencing data

Ensure that you have the following installed:

* Novobarcode, part of the Novoalign software package, which is freely available for educational and not-for-profit use. Download the latest version of Novoalign at http://www.novocraft.com/support/download/
* ShapeMapper 1.2, software developed by the Weeks lab at UNC Chapel Hill for 1D analysis of mutational profiling data. Available at http://www.chem.unc.edu/rna/software.html  (Make sure you go into that directory and run `make`.)
* BowTie2 is needed for ShapeMapper. Available here: https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.9/. Version 2.2.9 works.
* numpy
* The RDATkit for handling RDAT data files. Available at https://github.com/hitrace/rdatkit

Add the M2seq, novobarcode, etc. folders to your PATH. For example in your `.bashrc` add lines like `PATH=$PATH:$HOME/src/M2seq`.

To test on example sequencing data, download the two example FASTQs from [this link](https://www.dropbox.com/sh/0xrs2aypzzlims9/AACFa_pbuZ8QYB1O2rE-1fN-a?dl=0) and move them to the Tutorial folder. Then, run:

    m2seq.py P4P6.fa RTBbarcodes.fa Sample1_S1_L001_R1_001.fastq Sample1_S1_L001_R2_001.fastq --config example.cfg --offset 89
* `P4P6.fa` [required] is a fasta-formatted file with the name and sequence of the RNA. Note that the name of the fasta file and the sequence in the fasta file must match the name of the reference sequence given in the config file.
* `RTBbarcodes.fa` [required] is a Novobarcode-formatted file with the names and sequences of the barcodes in the RTB primers.
* The read 1 and read 2 `FASTQ`s are required inputs.
* `example.cfg` [optional] is a config file in the format required by ShapeMapper. If a config file is provided, the 2D dataset will be generated by ShapeMapper analysis followed by conversion of binary mutation-counted files to 2D data that are output as RDAT files. The correct names of the conditions in the pilot experiment used for this tutorial are already input in the [alignments] and [profiles] sections of the config file. These sections must be edited for different experiments.
* Make sure no spaces are in any of the folder names parent to this directory -- you may see fails of bowtie2 otherwise.
* *Useful tip* you may want to do a 'pilot run' with test fastq files that hold just a few test lines from your full `FASTQ` files. Prepare these as `head -n 100000  Sample1_S1_L001_R1_001.fastq  > test/Sample1_S1_L001_R1_001.fastq` and
`head -n 100000  Sample1_S1_L001_R2_001.fastq  > test/Sample1_S1_L001_R2_001.fastq` and supply `test/RTBbarcodes.fa Sample1_S1_L001_R1_001.fastq test/Sample1_S1_L001_R2_001.fastq` in the `m2seq.py` command line.
* If you need to rerun, you'll need to cleanly remove the previous output directories: `rm -rf 1_Demultiplex/ 2_ShapeMapper/ 3_MaP2D/`.

The `m2seq.py` command performs the following:
* First, it uses Novobarcode to demultiplex the pairs of sequencing reads using the barcodes provided in RTBbarcodes.fa
* Then, it performs ShapeMapper analysis with the settings in the config file to compare the reference sequence to the paired sequencing reads for each barcode
* ShapeMapper outputs a mutation strings text file for each barcode recording the mutations per read compared to the reference sequence, which is then converted to binary format
* The binary-formatted mutation strings are analyzed with simple_to_rdat.py to generate 2D datasets

The output of the pipeline includes, for each barcode:
* 2D reactivity RDAT
* 2D raw counts RDAT
* counted mutations over all sequencing reads
* log files
The ExampleResults archive contains these expected outputs from running the analysis on the example sequencing data at the link above.

The key modes of visualizing the MaP2D data are as a 2D plot (mutate-and-map style) and as mutation spectra (rates of mutation/deletion both across the sequence and on average).

To view the 2D plot, open MATLAB, make sure the `matlab` folder is in your MATLAB path, and run:

    map2dplot('3_MaP2D/simple_files/RTB005_P4P6_P4P6.reactivity.rdat');

Compare the resulting plot to the 2D plot in the `ExampleResults` folder (you may need to unzip `ExampleResults.zip`): `Example2D.eps`

To view the mutation spectra, open MATLAB and run:

    mut_heatmap('2_ShapeMapper/output/counted_mutations/RTB005_P4P6.csv',103:260,'',13);

Compare the resulting plot to the mutation spectra in the Figures folder: ExampleSpectra.eps, ExampleSpectra_mut_avg.eps, ExampleSpectra_mut_max.eps

