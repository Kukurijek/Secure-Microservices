
# Setup Instructions for macOS

This guide will walk you through setting up the required environment on macOS for deploying your application using Kubernetes.

---

## Prerequisites

Before starting, ensure you have:
- A stable internet connection.
- Basic knowledge of the terminal.

---

## Step-by-Step Guide

### 1. Install Homebrew

Homebrew is a package manager for macOS that simplifies installing software.

Run the following command to install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

### 2. Install Minikube with Homebrew

Minikube allows you to run Kubernetes locally. Install it using Homebrew:

```bash
brew install minikube
```

After installation, verify Minikube is installed correctly:

```bash
minikube version
```

---

### 3. Start Minikube

Start the Minikube cluster:

```bash
minikube start
```

---

### 4. Apply Kubernetes Configurations

Use `kubectl` to apply the YAML files for different components of your application. Ensure `kubectl` is configured correctly for Minikube:

1. **Apply all `.yaml` files from the `billing-db` folder:**

   ```bash
   kubectl apply -f billing-db/
   ```

2. **Apply all `.yaml` files from the `mysql` folder:**

   ```bash
   kubectl apply -f mysql/
   ```

3. **Apply all `.yaml` files from the `radius-service` folder:**

   ```bash
   kubectl apply -f radius-service/
   ```

---

### Alternative: Use the `deploy-services.sh` Script

Instead of running each command manually, you can use the provided `deploy-services.sh` script to apply all configurations at once.

1. Make the script executable:

   ```bash
   chmod +x deploy-services.sh
   ```

2. Run the script:

   ```bash
   ./deploy-services.sh
   ```

This will automatically deploy all the services.
---
### 5. Testing the Radius Service

The `radius-service` is not exposed externally (using `NodePort`) as it is intended for internal cluster communication. You can still test the service locally by using **port forwarding**.

Run the following command to forward the port:

```bash
kubectl port-forward svc/radius-service 8000:80
```

Once the port forwarding is active, you can test the service locally with a `curl` command:

```bash
curl -X GET "http://localhost:8000" -H "username-header: mresch" -H "pass-header: 12345678"
```

This will send a test request to the `radius-service` and verify its functionality.

---
### 6. Verify Deployment

After applying all configurations, verify that your pods and services are running:

```bash
kubectl get pods
kubectl get services
```

---

## Additional Notes

- If you encounter any issues, check the logs of the pods for debugging:
  ```bash
  kubectl logs <pod-name>
  ```
- Minikube dashboard can provide a visual overview of your cluster:
  ```bash
  minikube dashboard
  ```

---

This concludes the setup guide. If you have questions or issues, feel free to reach out! 😊
