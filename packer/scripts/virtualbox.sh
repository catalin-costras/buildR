VBOX_VERSION=$(cat /home/3pg/.vbox_version)

# required for VirtualBox 4.3.26
yum install -y bzip2 hello-world

cd /tmp
mount -o loop /home/3pg/VBoxGuestAdditions_$VBOX_VERSION.iso /mnt
sh /mnt/VBoxLinuxAdditions.run
umount /mnt
rm -rf /home/3pg/VBoxGuestAdditions_*.iso
