
# Security Enhancements Applied

This document outlines the container-level security enhancements applied across the following file:
- `deployment.yaml` (Radius Service) - schritt2/radius-service/deployment.yaml


## 1. Container-Level SecurityContext Recommendations

### 1.1 Disable Privilege Escalation
- **What was done**: Added `allowPrivilegeEscalation: false` to prevent processes within the container from gaining additional privileges.
- **Why it matters**: This restricts processes in the container from increasing their privilege level, reducing the risk of privilege escalation attacks.

### 1.2 Read-Only Root Filesystem
- **What was done**: Set `readOnlyRootFilesystem: true` to make the root filesystem read-only.
- **Why it matters**: Prevents malicious actors or software from modifying critical files in the container. Ensures that the container only writes to explicitly defined writable volumes.

### 1.3 Avoid Privileged Containers
- **What was done**: Added `privileged: false` to ensure the container does not run as a privileged container.
- **Why it matters**: Running privileged containers gives processes inside the container nearly unlimited access to the host, which is a significant security risk.

### 1.4 Drop All Capabilities
- **What was done**: Dropped all Linux capabilities using `capabilities.drop: - ALL`.
- **Why it matters**: Reduces the container’s access to kernel features and minimizes the attack surface. Additional capabilities can be added back on a need-to-use basis.

### 1.5 Run as Non-Root User
- **What was done**: Added `runAsNonRoot: true` and `runAsUser: 1000` to enforce running the container as a non-root user.
- **Why it matters**: Running containers as root increases the risk of privilege escalation. Using a non-root user ensures that processes within the container operate with the least privilege necessary.

---

## Why These Enhancements Make Sense

1. **Minimized Attack Surface**:
   - These changes reduce the potential entry points for attackers by limiting the container's access to unnecessary resources and kernel features.

2. **Compliance with Best Practices**:
   - Security guidelines for Kubernetes recommend enforcing these practices to create secure containerized workloads.

3. **Prevention of Privilege Escalation**:
   - Without these configurations, an attacker or compromised process could escalate its privileges and potentially affect the host system or other containers.

4. **Improved Isolation**:
   - These configurations ensure that each container operates within its intended boundaries, minimizing potential interference between containers or with the host.

5. **Operational Safety**:
   - By enforcing strict security policies, these enhancements mitigate the risk of unauthorized changes to containerized workloads, improving reliability and safety.

---
## 2 .ServiceAccount Security Enhancements

## What Was Done

1. **Created Dedicated ServiceAccount**:
   - A new ServiceAccount, specific to the workload (`radius-service-sa`), was created instead of using the default ServiceAccount.

2. **Disabled Automatic Token Mounting**:
   - Added `automountServiceAccountToken: false` in the Pod spec to prevent Kubernetes from automatically mounting a ServiceAccount token unless explicitly required.

3. **Updated Deployment**:
   - Updated the Deployment manifest to associate the new ServiceAccount with the workload.

---

## Why This Is Important

1. **Improved Security**:
   - Using a dedicated ServiceAccount ensures that each workload has only the permissions it needs, reducing the risk of over-permissioned workloads.
   - Prevents workloads from unintentionally sharing permissions assigned to the default ServiceAccount.

2. **Prevention of Token Misuse**:
   - Disabling automatic token mounting prevents unnecessary exposure of ServiceAccount tokens. This is particularly useful for workloads that do not require access to the Kubernetes API.

3. **Granular Access Control**:
   - By assigning specific ServiceAccounts to workloads, Role-Based Access Control (RBAC) rules can be tailored to grant the least privilege necessary.

---

## What This Does

1. **Separation of Responsibilities**:
   - Each workload has its own ServiceAccount, limiting the blast radius in case of a security incident.

2. **Restricts Kubernetes API Access**:
   - Prevents Pods from accessing the Kubernetes API unless explicitly required, reducing potential attack vectors.

3. **Supports Best Practices**:
   - Aligns with Kubernetes security best practices for isolating workloads and minimizing privileges.

---

## 3. Application design

## What Was Done

1. **Configured Resource Requests and Limits**:
   - Added resource requests and limits for CPU and memory in the `radius-service` Deployment.
   - Ensured that the memory limit is greater than or equal to the memory request.

2. **Defined QoS Class**:
   - By configuring resource requests and limits, the workload will be categorized under the **Burstable** QoS class unless requests and limits match, in which case it will fall under the **Guaranteed** QoS class.

---

## What This Does

1. **Resource Requests**:
   - Specifies the minimum resources (CPU and memory) guaranteed to the container.
   - Ensures the container gets the resources it needs to function properly under normal load.

2. **Resource Limits**:
   - Caps the maximum resources (CPU and memory) the container can consume.
   - Prevents a single container from monopolizing node resources.

3. **Quality of Service (QoS)**:
   - Ensures predictable resource allocation and prioritizes workloads during resource contention based on their QoS class.

---

## Why This Is Important

1. **Prevents Resource Starvation**:
   - Without resource requests, containers might compete for resources, leading to resource starvation for critical workloads.
   - Resource limits prevent a misbehaving container from consuming excessive resources.

2. **Improves Cluster Stability**:
   - By capping resource usage, the risk of node instability or disruption is minimized.

3. **Supports Predictable Performance**:
   - Ensures workloads operate reliably with the guaranteed resources specified in the requests.

4. **Aligns with Best Practices**:
   - Setting resource requests and limits is a Kubernetes best practice that aids in capacity planning and efficient resource utilization.


---
These recommendations help establish a more secure and resilient Kubernetes environment, aligning with industry standards and best practices.
