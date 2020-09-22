# M2seq_mod
## A wrapper for M2seq pipeline

```
run_m2seq_pipeline.py -s sequence_file.fa -f XXX_L001_R1_001.fastq XXX_L001_R2_001.fastq
```

### Differences form the original M2seq

The two key deifferences between this modified version and the original version of **M2seq** are:

1. The `m2seq.py` script was modified to not run the demultiplexing step, since our data is already demultiplexed. If you want to see changes between the original `m2seq.py` and the modified `m2seq_mod.py` you can use diff tool:

```
diff m2seq.py m2seq_mod.py

or gui diff:

xxdiff m2seq.py m2seq_mod.py

```

2. The whole pipeline is wrapped under one, simplified script `run_m2seq_pipeline.py`, where you need to specify only files from the sequencing and a fasta file. No more need for cumbersome generation of the configure file for ShapeMapper. The wrapper does everything, and creates all the needed inputs and directories.

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
