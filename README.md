# M2seq_mod
## A wrapper for a modified M2seq pipeline

This is a fork from M2seq reposirtory:

https://github.com/ribokit/M2seq


A modified version of the M2seq pipline, crafted to our needs. The pipeline does not include demultiplexing step, and the procedure of running is simplified.

If you want to see the original documentation please see the original M2seq repository (or `README_old.md`).


### Usage

To use this program you need two files from sequencing, following this naming conention:

```
XXX_L001_R1_001.fastq
XXX_L001_R2_001.fastq
```

where `XXX`
may be whatever string you like, whatever length e.g., sample name/number.

Also required is fasta file with the sequence of the studied RNA, without barcodes, only the region of interest.

When you have those files, you can simply run the program by:

```
run_m2seq_pipeline.py -s sequence_file.fa -f XXX_L001_R1_001.fastq XXX_L001_R2_001.fastq
```

The output will be directed to a newly created folder named as previously specified `XXX` prefix of the sequencing files names.

It will first run ShapeMapper, and then M2seq, resulting in a series of `.rdat` files, which you can use for visualisation of the results.

The output files can be found in `XXX/3_M2seq/simple_files`.


#### Runnig test run on test data

Copy contents of `M2seq_mod/example_data/input/` folder to a directory where you want to run the analysis.

In the directory with the inputs run:

```
run_m2seq_pipeline.py -s P4P6noHP.fa -f RTB000_S1_L001_R1_001.fastq RTB000_S1_L001_R2_001.fastq
```

Folder `RTB000_S1` will be created and the output data will be generated in `RTB000_S1/3_M2seq/simple_files/`.

Compare your results with files in `M2seq_mod/example_data/output/RTB000_S1/3_M2seq/simple_files`.




### Plot generation

The key modes of visualizing the M2seq data are as a 2D plot (mutate-and-map style) and as mutation spectra (rates of mutation/deletion both across the sequence and on average).

To view the 2D plot, open MATLAB and run:

`m2seqplot('3_M2seq/simple_files/XXX_L001_R1_001_fasta.reactivity.rdat`

To view the mutation spectra, open MATLAB and run:

`mut_heatmap('2_ShapeMapper/output/counted_mutations/RTB005_P4P6.csv',103:260,'',13);`

### Example files


Content of example fasta file `P4P6noHP.fa`:

```
>P4P6noHP
GGCCAAAACAACGGAATTGCGGGAAAGGGGTCAACAGCCGTTCAGTACCAAGTCTCAGGGGAAACTTTGAGATGGCCTTGCAAAGGGTATGGTAATAAGCTGACGGACATGGTCCTAACCACGCAGCCAAGTCCTAAGTCAACAGATCTTCTGTTGATATGGATGCAGTTCAAAACCAAACCAAAGAAACAACAACAACAAC
```


Content of exmple Sequencing file `RTB000_S1_L001_R1_001.fastq`:

```
@M00924:162:000000000-AN9GW:1:1101:16134:2249 1:N:0:1
GTTGTTGTTGTTGTTTCTTTGGTTTGGTTTTGAACTGCATCCCTCTCAACCCCCCATCTGTTCCCTTCCCCCTTCGCTCCGTCCTTCCCCCCCTCTCCCTCCGCTTCTTACCATACCCTTTCCCCCCCCCTCTCCCCCTTTCCCCTCCCCCTTCCTACTCACCCTCTCTTCACCCCTTTCCCCCCCTTCCCTTGTTTTTCCCCGCTCCCCCCACCCCTTCCCCCCCCATCCCCACCCCGCTCTCCTCTTCCCTCTTCTTCTTCCCCCCCCCCCCCCCCTCCCCCCCTC
+
@F@FFF9FE<FC<FFEEGGG--;6;,,;9;6,,,;;,;,;CE,9,9B,,:,,,+++9:6,<6,,:66,,,,866,,88,8,:,+89,,,,88+4+9:B,4:++844+58,<B,3,:BA535,:,,++88*464<,,***,77>>>3****448,,,,62,,,6,*65+22++77;:*20<;:*4**/*22*2<*302**+03*)(04*****))/***00)*2***((0(.1(())*/((-3.)(-())-)()(,.)))-)***..)))))))7)57;*71:<921((
@M00924:162:000000000-AN9GW:1:1101:22631:2408 1:N:0:1
GTTGTTGTTGTTGTTTCTTTGGTTTGGTTTTGAACTGCCTCCATCTCCACCCCCCCTCTCTTCCCTTACCCCTTCCCTCCCTCCTTCCCCCCCTCTCCCTCACCTTATTACCATACCCTTTCCACCCCCCTCTCCCCCTTTCCCCTTCCCCTTCCTCCTCCCCCCCTCTTCCCCCCTTTCCCCCCCTTCCCTTCTTTTCCCCAGCTCCCCCCCCCCCTTCCCCCCCCCTCCCGCCACCGTTCTCGTATCCCCTCTTCTCCTTCCCCCCCCCCCCCCCCCCCCCCCCCT
+
CFEFECEFF9FGCFFEEFGF--;C@,,;966,,,;;,;,6;C,,,5:,,9,,++++486,,,,,:,,,,,,9,4,,:5,8,4,+4,,,,,88+4+44A,4A,,855,5,,<A,,,:B=535,:,,,+88+363>,,++3,,8@>>,,,,,533,,3,62,,*5**41*33,,64::*2+5<:*4***020*02*+0++++3;*)().+****))1**/00)*2***((/(-1(())*1(((.)-(((((.)((-,.44).)**)).)))).).7@:@1*.(-212-((
@M00924:162:000000000-AN9GW:1:1101:15792:2496 1:N:0:1
GTTGTTGTTGTTGTTTCTTTGGTTTGGTTTTGAACTGCATCCATATCAACCGAAGATCTGTTGACTTAGGACTTGGCTGCGTGGTTAGGACCCTGTCCGTCAGCTTATTACCATACCCTTTGCAAGGCCATCTCACACTTTCCCCTGAGACTTCGTACTGAACGCCTGTTGACCCCTTTCCCGCAATTCCGTTGTTTTGGCCAGATCCGCCCACCGGTTCCCCACCCATGCCCACACCCCTCTCCTATCCCCTCTTCTGCTTCACCCCACCCACCCCCTCCCCCCCTC

...
```





### Differences from the original M2seq

The two key deifferences between this modified version and the original version of **M2seq** are:

1. The `m2seq.py` script was modified to not run the demultiplexing step, since our data is already demultiplexed. If you want to see changes between the original `m2seq.py` and the modified `m2seq_mod.py` you can use diff tool:

```
diff m2seq.py m2seq_mod.py

or gui diff:

xxdiff m2seq.py m2seq_mod.py

```

2. The whole pipeline is wrapped under one, simplified script `run_m2seq_pipeline.py`, where you need to specify only files from sequencing and a fasta file. No more need for cumbersome generation of the configure file for ShapeMapper. The wrapper does everything, and creates all the needed inputs and directories.

## Installation

Clone the software from the repo:

`git clone git@github.com:fryzjergda/M2seq_mod.git

Go to the folder `M2seq_mod/` and make the following executable:

```
chmod a+x m2seq_mod.py
chmod a+x run_m2seq_pipeline.py
chmod a+x simple_to_rdat.py
```

Add the following to `~/.bashrc`:

```
export PATH=$PATH:$HOME/M2seq_mod/

example:
export PATH=$PATH:/home/fryzjer/Projects/M2seq_mod/
```




## Requirements

#### Python 2.7

Ubnutu 18.04:

```
sudo apt update
sudo apt upgrade
sudo apt install python2.7
```

Ubuntu 20.04:

https://www.vultr.com/docs/how-to-install-python-2-on-ubuntu-20-04

```
sudo apt install python2
```

#### Python modules

```
sudo pip install nwalign
sudo pip install matplotlib
sudo pip install httplib2
sudo pip install numpy
sudo pip install scipy
sudo pip install xlrd
sudo pip install xlwt
```

Any additional Python libraries can be installed the same way.


#### Novobarcode

For this wrapper, Novobarcode is no longer needed. Our data is alreade demultiplexed, so there is no need for installation this software.


#### RNAStructure

Download software from:

https://rna.urmc.rochester.edu/register.html

Free registration is required.

Extract to the directory where you keep programs, and add the following to `~/.bashrc`:

```
export PATH=$PATH:$HOME/RNAstructure/exe
export DATAPATH=$HOME/RNAstructure/data_tables

example:
export PATH=$PATH:/home/fryzjer/Apps/RNAstructure/exe/
export DATAPATH='/home/fryzjer/Apps/RNAstructure/data_tables/'
```


#### ViennaRNA


Install ViennaRNA via `apt install`:

`sudo apt install viennarna`

(if apt cannot find viennarna, this step might be required before:)

`sudo add-apt-repository ppa:j-4-deactivatedaccount/vienna-rna`



If that does not work then try the below method:

Download `ViennaRNA Package - Core`, `ViennaRNA Package - Python 2 bindings` and `ViennaRNA Package - Python 3 bindings`, for yuor appropriate system under the "**Install precompiled Binary Package**" part from here:

https://www.tbi.univie.ac.at/RNA/

and follow the instructions:

```
  1. 'cd' to the directory containing the package's source code and type
     './configure' to configure the package for your system.

     Running 'configure' might take a while.  While running, it prints
     some messages telling which features it is checking for.

  2. Type 'make' to compile the package.

  3. Optionally, type 'make check' to run any self-tests that come with
     the package, generally using the just-built uninstalled binaries.

  4. Type 'make install' to install the programs and any data files and
     documentation.  When installing into a prefix owned by root, it is
     recommended that the package be configured and built as a regular
     user, and only the 'make install' phase executed with root
     privileges.

  5. Optionally, type 'make installcheck' to repeat any self-tests, but
     this time using the binaries in their final installed location.
     This target does not install anything.  Running this target as a
     regular user, particularly if the prior 'make install' required
     root privileges, verifies that the installation completed
     correctly.

```


#### BowTie 2

Download software from:

https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.9/

Extract to the directory where you keep programs, and add the following to `~/.bashrc`:

```
export PATH=$PATH:$HOME/bowtie2-2.2.9/

example:
export PATH=$PATH:/home/fryzjer/Apps/bowtie2-2.2.9/
```

#### ShapeMapper 1.2

Clone the software from the github repository, to where you keep programs:

https://github.com/Weeks-UNC/ShapeMapper_v1.2

```
git clone git@github.com:Weeks-UNC/ShapeMapper_v1.2.git

```

Add the following to `~/.bashrc`:

```
export PATH=$PATH:$HOME/ShapeMapper_v1.2/

example:
export PATH=$PATH:/home/fryzjer/Apps/ShapeMapper_v1.2/

```

Go to the directory with ShapeMapper and run command:

```
make
```

Make `ShapeMapper.py` and `pvclient.py` executable:

```
chmod a+x ShapeMapper.py
chmod a+x pvclient.py
```


#### VARNA


Download the `VARNAv3-93.jar` from here:

http://varna.lri.fr/index.php?lang=en&page=downloads&css=varna

and put it where you keep your programs.


#### RDATKit

This is required to handle RDAT files, mainly for generation of graphs (MATLAB also required...).

Clone the software from the github repository, to where you keep programs:

https://github.com/ribokit/RDATKit

```
git clone git@github.com:ribokit/RDATKit.git
```

or

`git clone https://github.com/ribokit/RDATKit.git`

Copy `path.py.example` into `rdatkit/path.py`. Edit `rdatkit/path.py` following the instructions in the file to point to local installations of `RNAstructure`, `ViennaRNA`, and `VARNA`.

Example contents of `rdatkit/path.py`:

```
PATH_RNA_STRUCTURE = '/home/fryzjer/Apps/RNAstructure/exe/'
PATH_VIENNA_RNA = '/usr/local/bin/'
PATH_VARNA_JAR = '/home/fryzjer/Projects/shape-backend/VARNAv3-93.jar'

```

Then go to RDATKit directory:

```
cd path/to/RDATKit/
```

and run:

```
python setup.py install
```




## Requirements for MATLAB

#### RDATKit

In MATLAB, go to "Set Path". Then "Add with Subfolders" of the target path: `path/to/RDATKit/MATLAB/.`


#### Biers

Clone the program from repo:

`git clone https://github.com/ribokit/Biers.git`

In MATLAB, go to "Set Path". Then "Add with Subfolders" of the target path: `path/to/Biers/Scripts/.`

Add the following to `~/.bashrc`:

```
export VARNA=$PATH:$HOME/src/VARNAv3-93.jar

example:
export VARNA=$PATH:/home/fryzjer/Projects/shape-backend/VARNAv3-93.jar
```


#### HiTRACE

RDATkit requires some MATLAB functions from HiTRACE (even though it is not mentioned NOWHERE in the RDATkit documentation).

Clone the program from the repo:

`git clone git@github.com:ribokit/HiTRACE.git`

or

`git clone https://github.com/ribokit/HiTRACE.git`


In MATLAB, go to "Set Path". Then "Add with Subfolders" of the target path: `path/to/HiTRACE/Scripts/`


#### Strings

For older version of MATLAB you may need to get additional scripts for parsing strings.

Get them from here:

https://uk.mathworks.com/matlabcentral/fileexchange/21710-string-toolkits

unpack the archive where you keep scripts.

In MATLAB, go to "Set Path". Then "Add with Subfolders" of the target path: `path/to/strings/.`


#### Saving MATLAB setup

In order to save all the previously set paths to MATLAB scripts, in MATLAB go to "Set Path", click "save" button and save file `pathdef.m`.

Whenever you want to open MATLAB with all paths set up, go to the directpry where you have saved the `pathdef.m` file, and open MATLAB from the command line.


## Citation

This is a fork of the M2seq repository by Rhiju Das group.
If you use this software, please cite the original authors:

Cheng, C. Kladwang, W. Yesselman, J. Das, R. (2017) "RNA structure inference through chemical mapping after accidental or intentional mutations" _BioRxiv_ https://doi.org/10.1101/169953.
