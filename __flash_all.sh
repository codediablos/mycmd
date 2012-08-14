#!/bin/bash
function usage(){
  echo "Version 1.1"
  echo "Usage: $0 <[T20, T30]> <SBK_1_4> <SBK_2_4> <SBK_3_4> <SBK_4_4>"
  echo "       <SBK_X_Y>: 8 hex digits with 0x prefix"
  echo "       e.g.: $0 T30 0x19ADC3AB 0xF00003D7 0x9C321B09 0x8F2FD92C"
}
error=1
if [ $# == 5 ]; then
  case $1 in
    "T20")
        chip=0x20
        odmdata=0x100c0105
        bootloader_id=4
        ;;
    "t20")
        chip=0x20
        odmdata=0x100c0105
        bootloader_id=4
        ;;
    "T30")
        chip=0x30
        odmdata=0x40080105
        bootloader_id=4
        ;;
    "t30")
        chip=0x30
        odmdata=0x40080105
        bootloader_id=4
        ;;
    *)
        chip=unknown
        ;;  
  esac
  
  if [ $chip == "unknown" ]; then
    error=1
  else
    error=0
    echo "sudo ./nvsbktool --sbk $2 $3 $4 $5 --chip $chip --bct flash.bct flash_enc.bct --bl bootloader.bin bootloader_enc.bin"
    sudo ./nvsbktool --sbk $2 $3 $4 $5 --chip $chip --bct flash.bct flash_enc.bct --bl bootloader.bin bootloader_enc.bin
    echo "sudo ./nvflash --blob blob.bin --bct flash_enc.bct --setbct --configfile flash_enc.cfg --create --odmdata $odmdata --bl bootloader_enc.bin"
    sudo ./nvflash --blob blob.bin --bct flash_enc.bct --setbct --configfile flash.cfg --create --odmdata $odmdata --bl bootloader_enc.bin
    echo "sudo ./nvflash --resume --blob blob.bin --setblhash flash_enc.bct --configfile flash.cfg --download $bootloader_id bootloader_enc.bin --bl bootloader_enc.bin"
    sudo ./nvflash --resume --blob blob.bin --setblhash flash_enc.bct --configfile flash.cfg --download $bootloader_id bootloader_enc.bin --bl bootloader_enc.bin
    echo "sudo ./nvflash --resume --go"
    sudo ./nvflash --resume --go
  fi
fi

if [ $error == 1 ]; then
  usage
fi
