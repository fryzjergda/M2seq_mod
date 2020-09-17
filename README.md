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

#### Novobarcode

For this wrapper, Novobarcode is no longer needed. Our data is alreade demultiplexed, so there is no need for installation this software.


#### RNAStructure

Download software from:

https://rna.urmc.rochester.edu/register.html

Free registration is required.

Extract to directore where you keep programs, and add the following to `~/.bashrc`:

```
export PATH=$PATH:$HOME/RNAstructure/exe
export DATAPATH=$HOME/RNAstructure/data_tables


example:
export PATH=$PATH:/home/fryzjer/Apps/RNAstructure/exe/
export DATAPATH='/home/fryzjer/Apps/RNAstructure/data_tables/'

```




#### ShapeMapper 1.2

https://github.com/Weeks-UNC/ShapeMapper_v1.2


