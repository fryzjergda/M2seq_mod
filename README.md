# M2seq_mod
## A wrapper for M2seq pipeline

```
run_m2seq_pipeline.py -s sequence_file.fa -f XXX_L001_R1_001.fastq XXX_L001_R2_001.fastq
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


#### RDATKit

This is required to handle RDAT files, mainly for generation of graphs (MATLAB also required...).

Clone the software from the github repository, to where you keep programs:

https://github.com/ribokit/RDATKit

```
git clone git@github.com:ribokit/RDATKit.git
```

*MATLAB:*

In MATLAB, go to "Set Path". Then "Add with Subfolders" of the target path/to/RDATKit/MATLAB/.

*Python:*

Copy `path.py.example` into `rdatkit/path.py`. Edit `rdatkit/path.py` following the instructions in the file to point to local installations of `RNAstructure`, `ViennaRNA`, and `VARNA`.