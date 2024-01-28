## 📚 Theory

Deploying applications on OpenShift involves harnessing the power of containers within a Kubernetes-based orchestration framework. At the heart of OpenShift's deployment model lie concepts such as pods, deployments, and advanced strategies for running applications efficiently and reliably. 

In Kubernetes, a pod represents the smallest deployable unit that encapsulates one or more containers, along with shared storage and network resources. A deployment in provides a declarative approach to managing application lifecycle. It defines the desired state of the application, including the number of replicas (instances) to run and how to handle updates and rollbacks. Deployments ensure that applications are continuously available and can be easily managed and scaled.

OpenShift offers several strategies for running applications effectively, catering to workload requirements and operational preferences. Rolling updates allow for seamless deployment of new application versions while ensuring zero downtime. OpenShift gradually replaces existing pods with new ones, ensuring a smooth transition without service interruptions. Blue-green deployments involve maintaining two identical production environments (blue and green). OpenShift switches traffic between the environments, enabling fast and risk-free application updates. Canary deployments enable the gradual rollout of new application versions to a subset of users or traffic. OpenShift directs a portion of traffic to the new version while monitoring its performance. If successful, the deployment expands gradually; otherwise, OpenShift can quickly revert to the previous version. By leveraging these deployment strategies, OpenShift empowers organizations to maintain agility, reliability, and scalability in their application deployment processes. 

In this task, you will be deploying an application on your OpenShift cluster that you've installed in Section 1 of this lab.

Let's proceed

## 💻 Practice

### 1. Pull the application from our Github repository



1. pull from git

2. run the oc create -f 

3. verify whether the deployment and pods are standing up

4. check the openshift console

5. check on the APIC

6. try accessing the app
