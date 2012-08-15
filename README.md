#MYCMD

##Introduction:  

go: Easy change your directory  
install: Easy install apk file  
flash: Easy flash you device  

##How to Use:  

###1. Add below to your .bashrc:  

> if [ -n "$BASH_VERSION" ]; then  
>     # include .bash_completion if it exists  
>     if [ -f "$HOME/mycmd/.bash_completion" ]; then  
>         . "$HOME/mycmd/.bash_completion"  
>     fi  
> fi  

> export  PATH=$HOME/bin:$PATH  

###2. Put files in your linux  

$ cd $HOME  
$ git clone https://github.com/codediablos/mycmd.git  
$ source ~/.bashrc  
$ cp .mycmd_conf_template ~/.mycmd_conf  

###3. Set mycmd config file  
edit .mycmd_conf  
open .mycmd_conf for more detail  

--------------------------------------------------------

##Change Logs

version: 2.7.12  
1. Now can using "tab" to achieve completion function  




