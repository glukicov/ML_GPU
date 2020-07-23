#!/bin/bash

#-----------------------------------------------------------
remotedir="USERNAME@HOST:/PATH/TO/MOUNT"  # TODO Add directory on the remote machine
mountdir="/Users/user/Mount/Directory"   # TODO Add local directory 
#-----------------------------------------------------------
echo "Mounting (${mountdir})..."

if [ -d "${mountdir}" ]; then
  #Unmount if it's already mounted
  if mount | grep "on $mountdir" > /dev/null; then
    umount ${mountdir}  
  fi
else
  mkdir ${mountdir}
fi

#Now mount the remote file system
#   (The -o workaround=rename -o noexec are used so kwrite can save files.)
sshfs -o ssh_command='ssh -AKXY' -o workaround=rename -o noexec -o idmap=user -o uid=$(id -u) -o gid=$(id -g) ${remotedir} ${mountdir}

#Sleep 1 second to give it time to register, then check that it is now mounted
sleep 1
if mount | grep "on $mountdir" > /dev/null; then
  echo "Success"
  cd ${mountdir}
else
  echo "Failure!"  
fi

# exit 0
