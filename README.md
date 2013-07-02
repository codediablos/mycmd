#MYCMD

##Introduction:  

go: Easy change your directory  
install: Easy install your file  
flash: Easy flash your device  

##How to Use:  

###1. Add below to your .bashrc:
<pre><code>if [ -n "$BASH_VERSION" ]; then  
    # include .bash_completion if it exists  
    if [ -f "$HOME/mycmd/.bash_completion" ]; then  
        . "$HOME/mycmd/.bash_completion"  
    fi  
fi  

export  PATH=$HOME/mycmd:$PATH  
</code></pre>

###2. Put files in your linux  
<pre><code>$ cd ~  
$ git clone https://github.com/codediablos/mycmd.git  
$ source ~/.bashrc  
$ cp ~/mycmd/.mycmd_conf_template ~/.mycmd_conf  
</code></pre>

###3. Edit your mycmd config file
<pre><code>$ mycmd --config
</code></pre>

[core]  
project_home = /home/username/project/  <---- your project home, you can use "go"  

 # Setting your project directory  
[project]  
a9 = ics-robin  <---- your a9 project at /home/username/project/a9, you can use "go a9"  
pm = ics-mr1.1-pm  

log = ../test_log/ <---- it can go to /home/username/project/../test_log/

 # Setting your sub-directory  
 # Using "go project sub-directory" to sub-directory  
 # ex. $ go pm i2c  
[subdir]  
i2c = kernel/drivers/i2c  
uart = kernel/drivers/tty/serial  
eeprom = kernel/drivers/misc/eeprom  

 # Setting your sub-directory for different project  
 # First create section [xxx_dir]  
 # Using "go project sub-directory" to sub-directory  
 # ex. $ go project1 xxx  
 # You also can set default option, if you have many project with same directory  
[out_dir]  
prefix = out/target/product  
a9 = a9  
pm = picasso_m  
pmf = picasso_mf  
pre-jb-pmf = picasso_mf  
pe = picasso_e  
pe2 = picasso_e2  
p1 = picasso  
vg = vangogh  

[mach_dir]  <---- you can use "go a9 mach", change directory to /home/username/project/a9/kernel/arch/arm/mach-msm  
prefix = kernel/arch/arm  
default = mach-tegra  
a9 = mach-msm  

 # adb install file  
 # Using "install name" to install apk in your device  
 # ex. $ install log  
[install]  
i2c = /home/username/Test-Tools/I2C_StressTest/apk/CloseJohn_v3.2_Signed.apk  
log = /home/username/Test-Tools/AcerLogSetting_V3.9/AcerLogSetting_v3.9_Unsigned.apk  


 # For flash  
 # Using "flash" to burn your device  
 # ex. $ flash t30 pm  
 #     $ flash t30 boot pm  
 #     $ flash t20  
 #     $ flash t30 system  
[fused]  
pm = 0xF5FF279B 0xF30908C1 0x63A8F8DA 0x98AFC7AA  
pmf_CCC = 0xF5C6E9A8 0x426E48BE 0xB06C7A09 0xCF07ACCC  
vg_@87 = 0x9339020C 0x84A51889 0xA9B5B3D7 0x8E94A600  
pe2_7B1 = 0xA3AD9B60 0x6D76BA87 0xD045210E 0x0D80F7B1  

