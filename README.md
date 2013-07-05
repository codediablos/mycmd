#MYCMD

##Introduction:  

go: Easy change your directory  
flash: Easy flash your device  
install: Easy install your file  

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
#### 3.1 Go to your project home, you can use *`go`* 
<pre><code>$ emacs ~/.mycmd_conf  
</code></pre>
<pre><code>[core]  
project_home = /home/username/project/  <---- 
</code></pre>

#### 3.2 Go to your project home, you can use *`go project`* 
your a9 project at /home/username/project/a9, you can use `go a9` 

<pre><code>[project]  
a9 = ics-robin
pm = ics-mr1.1-pm  
log = ../test_log/
</code></pre>


#### 3.3 Setting your sub-directory  *`go project subdir`* 
Using "go project sub-directory" to sub-directory  
ex. $ go pm i2c  
<pre><code>[subdir]  
i2c = kernel/drivers/i2c  
uart = kernel/drivers/tty/serial  
eeprom = kernel/drivers/misc/eeprom  
</code></pre>

#### 3.4 Setting your sub-directory for different project 
Create section [xxx_dir]  
Using `go project sub-directory` to sub-directory  
ex. $ `go project xxx`  
You also can set default option, if you have many project with same directory 
<pre><code>[out_dir]  
prefix = out/target/product  
a9 = a9  
pm = picasso_m  
pmf = picasso_mf  
pre-jb-pmf = picasso_mf  
pe = picasso_e  
pe2 = picasso_e2  
p1 = picasso  
vg = vangogh  
</code></pre>
you can use `go a9 mach`, change directory to /home/username/project/a9/kernel/arch/arm/mach-msm 
<pre><code>[mach_dir]   
prefix = kernel/arch/arm  
default = mach-tegra  
a9 = mach-msm  
</code></pre>

#### 3.4 adb install file
Using "install name" to install apk in your device  
ex. $ install log  
<pre><code>[install]  
i2c = /home/username/Test-Tools/I2C_StressTest/apk/CloseJohn_v3.2_Signed.apk  
log = /home/username/Test-Tools/AcerLogSetting_V3.9/AcerLogSetting_v3.9_Unsigned.apk  
</code></pre>

#### 3.5 For fused flash
For fused & non-fused device  
Using `flash` to burn your device like 
`flash pm`  
`flash boot pm`   
`flash pmf pmf_CCC`    
`flash ta2 system ta2xxx`  
  
<pre><code>[fused]  
pm = 0xF5FF279B 0xF30908C1 0x63A8F8DA 0x98AFC7AA  
pmf_CCC = 0xF5C6E9A8 0x426E48BE 0xB06C7A09 0xCF07ACCC  
vg_@87 = 0x9339020C 0x84A51889 0xA9B5B3D7 0x8E94A600  
pe2_7B1 = 0xA3AD9B60 0x6D76BA87 0xD045210E 0x0D80F7B1
ta2xxx = 0xXXXXXXXX 0xXXXXXXXX 0xXXXXXXXX 0xXXXXXXXX   
</code></pre>  
