We now need to set up Cobbler.

Cobbler is a ...


1.	Copy kernel file to one with the name that is supported by cobbler. 

<!-- [cisco@ocp02-orch image]$ sudo cp rhcos-live-kernel-x86_64 vmlinuz  -->


2.	Add the distro information to the cobbler for PXE Boot. 

<!-- [cisco@ocp02-orch image]$ cobbler distro add --name rhcos-x86_64-4.10.37 --kernel=/var/www/html/image/vmlinuz --initrd=/var/www/html/image/rhcos-live-initramfs.x86_64.img

# verify that the distro was added
[cisco@ocp02-orch image]$ cobbler distro list
   rhcos-x86_64-4.10.37 -->


3.	Add the kickstart profile to the distro.

<!-- [cisco@ocp02-orch image]$ cobbler profile add --name rhcos-x86_64-4.10.37 --distro=rhcos-x86_64-4.10.37
[cisco@ocp02-orch image]$ cobbler profile list
   rhcos-x86_64-4.10.37 -->


4.	Add cluster’s systems – 1 x bootstrap, 3 x control and 2 x worker nodes. 

<!-- cisco@ocp02-orch images]$ cobbler system add \
--name ocp02-bootstrap \
--profile rhcos-x86_64-4.10.37 \
--netboot-enabled=true \
--hostname bootstrap \
--dns-name bootstrap.ocp02.blndc01.cisco.com \
--ip-address 22.1.152.29  \
--static=false \
--interface ens192 \
--netmask 255.255.255.224 \
--mac 00:50:56:AA:BB:CC \
--gateway 22.1.152.1 \
--kernel-options="coreos.live.rootfs_url=http://22.1.152.30:8080/image/rhcos-live-rootfs.x86_64.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://22.1.152.30:8080/ignition/bootstrap.ign"

cobbler system add \
--name ocp02-master1 \
--profile rhcos-x86_64-4.10.37 \
--netboot-enabled=true \
--hostname master1 \
--dns-name master1.blndc01.cisco.com \
--ip-address 22.1.152.2  \
--static=false \
--interface eno5 \
--netmask 255.255.255.224 \
--mac 3c:fd:fe:a7:14:e0 \
--gateway 22.1.152.1 \
--kernel-options="coreos.live.rootfs_url=http://22.1.152.30:8080/image/rhcos-live-rootfs.x86_64.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://22.1.152.30:8080/ignition/master.ign ip=bond0:dhcp:9000 bond=bond0:eno5,eno6:mode=802.3ad,miimon=100,lacp_rate=slow ip=bond1.4093:dhcp:9000 bond=bond1:ens1f0,ens1f1:mode=802.3ad,miimon=100,lacp_rate=slow vlan=bond1.3914:bond1 rd.route=224.0.0.0/4::bond1.3914"

cobbler system add \
--name ocp02-master2 \
--profile rhcos-x86_64-4.10.37 \
--netboot-enabled=true \
--hostname master2 \
--dns-name master2.blndc01.cisco.com \
--ip-address 22.1.152.3  \
--static=false \
--interface eno5 \
--netmask 255.255.255.224 \
--mac 3c:fd:fe:cb:a6:78 \
--gateway 22.1.152.1 \
--kernel-options="coreos.live.rootfs_url=http://22.1.152.30:8080/image/rhcos-live-rootfs.x86_64.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://22.1.152.30:8080/ignition/master.ign ip=bond0:dhcp:9000 bond=bond0:eno5,eno6:mode=802.3ad,miimon=100,lacp_rate=slow ip=bond1.4093:dhcp:9000 bond=bond1:ens1f0,ens1f1:mode=802.3ad,miimon=100,lacp_rate=slow vlan=bond1.3914:bond1 rd.route=224.0.0.0/4::bond1.3914"

cobbler system add \
--name ocp02-master3 \
--profile rhcos-x86_64-4.10.37 \
--netboot-enabled=true \
--hostname master3 \
--dns-name master3.blndc01.cisco.com \
--ip-address 22.1.152.4  \
--static=false \
--interface eno5 \
--netmask 255.255.255.224 \
--mac 3c:fd:fe:d2:2a:40 \
--gateway 22.1.152.1 \
--kernel-options="coreos.live.rootfs_url=http://22.1.152.30:8080/image/rhcos-live-rootfs.x86_64.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://22.1.152.30:8080/ignition/master.ign ip=bond0:dhcp:9000 bond=bond0:eno5,eno6:mode=802.3ad,miimon=100,lacp_rate=slow ip=bond1.4093:dhcp:9000 bond=bond1:ens1f0,ens1f1:mode=802.3ad,miimon=100,lacp_rate=slow vlan=bond1.3914:bond1 rd.route=224.0.0.0/4::bond1.3914"

cobbler system add \
--name ocp02-worker1 \
--profile rhcos-x86_64-4.10.37 \
--netboot-enabled=true \
--hostname worker1 \
--dns-name worker1.blndc01.cisco.com \
--ip-address 22.1.152.5  \
--static=false \
--interface eno5 \
--netmask 255.255.255.224 \
--mac 3c:fd:fe:cb:a5:b8 \
--gateway 22.1.152.1 \
--kernel-options="coreos.live.rootfs_url=http://22.1.152.30:8080/image/rhcos-live-rootfs.x86_64.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://22.1.152.30:8080/ignition/worker.ign ip=bond0:dhcp:9000 bond=bond0:eno5,eno6:mode=802.3ad,miimon=100,lacp_rate=slow ip=bond1.4093:dhcp:9000 bond=bond1:ens1f0,ens1f1:mode=802.3ad,miimon=100,lacp_rate=slow vlan=bond1.3914:bond1 rd.route=224.0.0.0/4::bond1.3914"

cobbler system add \
--name ocp02-worker2 \
--profile rhcos-x86_64-4.10.37 \
--netboot-enabled=true \
--hostname worker2 \
--dns-name worker2.blndc01.cisco.com \
--ip-address 22.1.152.6  \
--static=false \
--interface eno5 \
--netmask 255.255.255.224 \
--mac 3c:fd:fe:dc:b6:60 \
--gateway 22.1.152.1 \
--kernel-options="coreos.live.rootfs_url=http://22.1.152.30:8080/image/rhcos-live-rootfs.x86_64.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://22.1.152.30:8080/ignition/worker.ign ip=bond0:dhcp:9000 bond=bond0:eno5,eno6:mode=802.3ad,miimon=100,lacp_rate=slow ip=bond1.4093:dhcp:9000 bond=bond1:ens1f0,ens1f1:mode=802.3ad,miimon=100,lacp_rate=slow vlan=bond1.3914:bond1 rd.route=224.0.0.0/4::bond1.3914" -->


5.	List all systems. 

<!-- [cisco@ocp02-orch ~]$ cobbler system list
   ocp02-bootstrap
   ocp02-master1
   ocp02-master2
   ocp02-master3
   ocp02-worker1
   ocp02-worker2

[cisco@ocp02-orch ~]$ cobbler system report --name ocp02-worker2
Name                           : ocp02-worker2
Automatic Installation Template : <<inherit>>
Automatic Installation Template Metadata : <<inherit>>
TFTP Boot Files                : <<inherit>>
Boot loaders                   : <<inherit>>
Comment                        : 
Display Name                   : 
Enable iPXE?                   : <<inherit>>
Fetchable Files                : <<inherit>>
DHCP Filename Override         : <<inherit>>
Gateway                        : 22.1.152.1
Hostname                       : worker2
Image                          : 
IPv6 Autoconfiguration         : False
IPv6 Default Device            : 
Kernel Options                 : {'coreos.live.rootfs_url': 'http://22.1.152.30:8080/image/rhcos-live-rootfs.x86_64.img', 'coreos.inst.install_dev': '/dev/sda', 'coreos.inst.ignition_url': 'http://22.1.152.30:8080/ignition/worker.ign', 'ip': ['bond0:dhcp:9000', 'bond1.4093:dhcp:9000'], 'bond': ['bond0:eno5,eno6:mode=802.3ad,miimon=100,lacp_rate=slow', 'bond1:ens1f0,ens1f1:mode=802.3ad,miimon=100,lacp_rate=slow'], 'vlan': 'bond1.3914:bond1', 'rd.route': '224.0.0.0/4::bond1.3914'}
<skipped> -->
