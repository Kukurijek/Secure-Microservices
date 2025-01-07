# Helm Deployment for Radius Service

We have implemented a Helm-based approach for deploying the Radius service. This allows for easier and more flexible management of deployments.

### Key Features
- **Template-Based Deployment**: The `deployment.yaml` has been templated, enabling dynamic configuration.
- **Value Customization**: Configuration values are defined in `values.yaml`, allowing easy adjustments without modifying templates.

This method simplifies service management, especially when adopting a GitOps workflow, where configurations are managed and applied declaratively via version control.

---

### Benefits of Using Helm
1. **Modularity**: Separation of templates and values promotes reusable components.
2. **Scalability**: Easily scale and configure multiple environments (development, staging, production).
3. **GitOps Compatibility**: Ensures configurations are version-controlled and applied consistently across environments.

Helm provides a streamlined and efficient approach to managing Kubernetes deployments, making it ideal for both small-scale and enterprise-level applications.
