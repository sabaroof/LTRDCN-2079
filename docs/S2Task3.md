## 📚 Theory


Let's proceed

## 💻 Practice


[//] # "We will not use SNAT for cluster IP, rather namespace"

3. Create a cluster-wide SNAT policy using the SNAT IP that comes from the pre-allocated pool 22.1.151.128/27. The name of the policy can be changed. Without SNAT policy the pods from pod network wont be able to access resources outside of the cluster (example, coredns would not be able to access external DNS server) 

apiVersion: aci.snat/v1
kind: SnatPolicy
metadata:
  name: installerclusterdefault
spec:
  snatIp:
  - 22.1.152.129
Apply this yaml file to create a corresponding resource in the cluster using command “oc apply -f xxx.yaml” and verify that snat resource was created.
[cisco@ocp02-orch upi]$ oc get snatpolicy
NAME                      AGE
installerclusterdefault   44m



3. Create a cluster-wide SNAT policy using the SNAT IP that comes from the pre-allocated pool 22.1.151.128/27. The name of the policy can be changed. Without SNAT policy the pods from pod network wont be able to access resources outside of the cluster (example, coredns would not be able to access external DNS server) 

apiVersion: aci.snat/v1
kind: SnatPolicy
metadata:
  name: installerclusterdefault
spec:
  snatIp:
  - 22.1.152.129
Apply this yaml file to create a corresponding resource in the cluster using command “oc apply -f xxx.yaml” and verify that snat resource was created.
[cisco@ocp02-orch upi]$ oc get snatpolicy
NAME                      AGE
installerclusterdefault   44m