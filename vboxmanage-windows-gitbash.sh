#!/bin/bash
#
# ./<this script name>.sh <vm name>
#



MACHINENAME=$1

if [ ! -f $HOME/Downloads/centos-7.iso ]; then
    curl http://www.gtlib.gatech.edu/pub/centos/7.8.2003/isos/x86_64/CentOS-7-x86_64-Minimal-2003.iso -O $HOME/Downloads/centos-7.iso
fi

bridgeadapterid=$(VBoxManage list bridgedifs | grep Name: | grep Intel | head -1 | awk -F":" '{ print $2 }' | cut -d'<' -f1|sed 's/^[ \t]*//')
maindir=$HOME
mkdir $maindir/VMS


VBoxManage createvm --name  $MACHINENAME --ostype RedHat_64 --register --basefolder  $maindir/VMS

VBoxManage modifyvm $MACHINENAME --nic1 bridged --bridgeadapter1 "$bridgeadapterid"

VBoxManage modifyvm $MACHINENAME  --memory 2048 

VBoxManage createhd --filename $maindir/VMS/$MACHINENAME/$MACHINENAME.vdi --size 10000 --format VDI

VBoxManage storagectl $MACHINENAME --name "SATA Controller" --add sata --controller IntelAhci
VBoxManage storageattach $MACHINENAME --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium $maindir/VMS/$MACHINENAME/$MACHINENAME.vdi


VBoxManage storagectl $MACHINENAME --name "IDE Controller" --add ide --controller PIIX4
VBoxManage storageattach $MACHINENAME --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium $maindir/Downloads/centos-7.iso

echo "$bridgeadapterid"

VBoxManage startvm $MACHINENAME


#sanspshot commands
#  VBoxManage snapshot $MACHINENAME take "snap1"
#  VBoxManage snapshot $MACHINENAME restore "snap1"
#  VBoxManage unregistervm $MACHINENAME --delete


#import-export
#VBoxManage list vms
#VBoxManage export $MACHINENAME --output $HOME/Downloads/my-snap.ovf
#VBoxManage import $HOME/Downloads/my-snap.ovf

#clone
# VBoxManage controlvm test4 poweroff soft
#VBoxManage clonevm test4--name test6 --register 
# VBoxManage startvm test6 --type headless
