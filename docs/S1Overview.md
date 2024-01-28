In this section, you will be installing OpenShift 4.13 on baremetal servers using the User-Provisioned Infrastructure (UPI) installation method.

## Instalation methods overview

 The OpenShift Container Platform installation program offers four methods for deploying a cluster which are detailed in the following list:

    Interactive: You can deploy a cluster with the web-based Assisted Installer. This is an ideal approach for clusters with networks connected to the internet. The Assisted Installer is the easiest way to install OpenShift Container Platform, it provides smart defaults, and it performs pre-flight validations before installing the cluster. It also provides a RESTful API for automation and advanced configuration scenarios.
    Local Agent-based: You can deploy a cluster locally with the Agent-based Installer for disconnected environments or restricted networks. It provides many of the benefits of the Assisted Installer, but you must download and configure the Agent-based Installer first. Configuration is done with a command-line interface. This approach is ideal for disconnected environments.
    Automated: You can deploy a cluster on installer-provisioned infrastructure. The installation program uses each cluster host’s baseboard management controller (BMC) for provisioning. You can deploy clusters in connected or disconnected environments.
    Full control: You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters in connected or disconnected environments. 

User Provisioned Infrastructure (UPI) in the context of OpenShift refers to a deployment method where users have control over the underlying infrastructure on which OpenShift clusters are deployed. Unlike installer-provisioned infrastructure, where OpenShift provisions infrastructure resources automatically, UPI allows users to pre-provision infrastructure components like virtual machines or bare metal servers.

Prerequisites for UPI:

## Lab topology

<figure markdown>
  ![LabTopology](./assets/topology.png){ width="500" }
</figure>

## Lab access details

table
