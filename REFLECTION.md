# Docker Assignment Reflection

**Name:** Lekhana Sandra  
**Date:** October 27, 2025  
**Course:** Python for Web API Development  
**Assignment:** Dockerizing QR Code Generator Application

---

## Introduction

This assignment provided hands-on experience with containerization technology by Dockerizing a Python-based QR Code Generator application. The project involved creating a Docker image, running containers, pushing to DockerHub, and implementing a CI/CD pipeline using GitHub Actions. Through this process, I gained practical understanding of modern DevOps practices and container orchestration that are essential in today's web development landscape.

---

## Key Experiences and Learning Outcomes

### Docker Installation and Initial Setup

Installing Docker Desktop on my Mac was relatively straightforward. I downloaded Docker Desktop from the official Docker website and followed the installation wizard. After installation, I verified Docker was working correctly by running `docker --version` in Terminal, which displayed version information confirming successful installation. I also created a DockerHub account, which would later serve as my container registry for storing and sharing Docker images.

One initial challenge was understanding Docker's architecture. I learned that Docker uses a client-server model where the Docker CLI communicates with the Docker daemon, which manages containers, images, networks, and volumes. This architecture enables Docker to be lightweight compared to traditional virtual machines.

### Understanding the QR Code Generator Application

Before containerizing the application, I examined the Python code to understand its functionality. The application uses the `qrcode` library to generate QR codes from URLs, with command-line argument support for customization. It creates output directories for QR codes and logs, demonstrating file I/O operations that would need special consideration in a containerized environment.

The application's dependencies were specified in `requirements.txt`, which included `qrcode[pil]` and `Pillow` for image generation. This dependency management would become crucial during the containerization process.

### Creating the Dockerfile

Writing the Dockerfile was an enlightening experience that taught me about container image layers and best practices. Each instruction in the Dockerfile creates a new layer, and Docker caches these layers to speed up subsequent builds. I learned several important concepts:

**Base Image Selection:** Using `python:3.12-slim-bullseye` provided a minimal Python environment, reducing the attack surface and image size. The "slim" variant contains only essential packages, making the container more secure and efficient.

**Working Directory:** The `WORKDIR /app` command sets the working directory inside the container, providing a clean organizational structure and ensuring all subsequent commands execute in the correct location.

**Dependency Installation:** Copying `requirements.txt` first and running `pip install` before copying the application code leverages Docker's layer caching. If the application code changes but dependencies don't, Docker reuses the cached dependency layer, significantly speeding up builds.

**Security Implementation:** Creating a non-root user (`myuser`) was a critical security practice I learned. Running applications as root inside containers is dangerous because if the container is compromised, the attacker has root privileges. By switching to a non-root user with `USER myuser`, I implemented the principle of least privilege, limiting potential damage from security vulnerabilities.

**Entry Points and Commands:** Understanding the difference between `ENTRYPOINT` and `CMD` was important. `ENTRYPOINT` defines the executable that always runs, while `CMD` provides default arguments that can be overridden. This design allows flexibility when running containers with different URLs without rebuilding the image.

### Building and Running Docker Containers

Building the Docker image with `docker build -t qr-code-generator-app .` was my first experience seeing Docker pull base images, install dependencies, and create layers. The build process took a couple of minutes, and watching the output helped me understand what happens during each Dockerfile instruction.

Running containers taught me about container lifecycle management. Using `docker run -d` runs containers in detached mode, allowing them to run in the background. I learned essential commands:
- `docker ps` to list running containers
- `docker logs` to view container output
- `docker stop` and `docker rm` for container cleanup

The volume mount feature (`-v`) was particularly interesting. By mounting my local directory to `/app/qr_codes` inside the container, I could persist generated QR codes on my host machine. This demonstrated how containers can interact with the host filesystem while maintaining isolation.

---

## Challenges Faced and Solutions

### Challenge 1: Python Version Compatibility with Pillow

**Problem:** When creating the virtual environment for local testing, I encountered a `ModuleNotFoundError` for qrcode. After installing dependencies, I faced a more complex error: Pillow 10.1.0 failed to build with Python 3.13. The error message showed a `KeyError: '__version__'` during the wheel building process, indicating version incompatibility.

**Root Cause:** My Mac had Python 3.13 installed, which was very new. Pillow 10.1.0 was released before Python 3.13 and hadn't been tested with it, causing build failures.

**Solution:** I updated `requirements.txt` to use `Pillow>=10.2.0` instead of pinning to 10.1.0. The `>=` operator allowed pip to install a newer, compatible version (10.4.0) that supported Python 3.13. This taught me about semantic versioning and the importance of flexible dependency specifications.

**Learning:** This experience highlighted the reality of dependency management in software development. Pinning exact versions provides reproducibility but can cause compatibility issues. Using version ranges with lower bounds provides flexibility while maintaining minimum requirements.

### Challenge 2: Text Editor Confusion

**Problem:** Early in the assignment, I struggled with entering code into files. I attempted to paste code directly into the Terminal prompt instead of opening a text editor first, resulting in shell errors like `>quote` and `command not found`.

**Root Cause:** I was unfamiliar with command-line text editors and didn't understand the distinction between the Terminal prompt and an editor environment.

**Solution:** I learned to use nano, a beginner-friendly terminal text editor. The workflow became: `nano filename` to open the editor, paste content, then `Control+X`, `Y`, `Enter` to save. I also learned to verify file contents with `cat filename`.

**Learning:** This taught me fundamental command-line skills essential for server administration and remote development where GUI text editors aren't available. Understanding the difference between the shell and applications running within it is crucial for effective Terminal usage.

### Challenge 3: GitHub Actions Authentication Failure

**Problem:** After setting up GitHub Actions workflow, the build consistently failed with "unauthorized: incorrect username or password" when attempting to push to DockerHub. This error persisted across multiple attempts.

**Root Cause:** I initially didn't understand that GitHub Actions requires an access token rather than a DockerHub password. Additionally, there was confusion about secret configuration—the secrets needed exact names (`DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`) and the token needed proper permissions.

**Solution:** I created a DockerHub Personal Access Token with Read/Write/Delete permissions at https://hub.docker.com/settings/security. I then configured GitHub repository secrets correctly, ensuring:
- `DOCKERHUB_USERNAME` contained my exact DockerHub username
- `DOCKERHUB_TOKEN` contained the full access token (starting with `dckr_pat_`)
- No extra spaces or newlines were included

I also learned to test credentials locally first using `docker login -u username` and pasting the token when prompted for a password, verifying they worked before updating GitHub secrets.

**Learning:** This challenge taught me about secure credential management in CI/CD pipelines. Access tokens are more secure than passwords because they can be scoped to specific permissions and easily revoked. This is a critical security practice in modern DevOps, preventing password exposure in logs and enabling fine-grained access control.

### Challenge 4: Understanding Docker Networking and Volume Mounts

**Problem:** Initially, I didn't understand how to access files created inside containers or how containers isolated from the host system.

**Solution:** Learning about volume mounts (`-v` flag) solved this. When running `docker run -v ~/Desktop/qr_codes_output:/app/qr_codes`, I mapped my Desktop directory to the container's `/app/qr_codes` directory. Files written inside the container appeared on my Desktop.

**Learning:** This taught me about container isolation and data persistence. Containers are ephemeral by design—when removed, their data disappears unless persisted through volumes, bind mounts, or external storage systems.

---

## Technical Skills Developed

### Containerization Fundamentals
- **Container vs. VM:** I now understand that containers share the host OS kernel, making them lighter and faster than virtual machines. VMs include a full OS copy, while containers include only application dependencies.
- **Image Layers:** Docker images are built in layers, with each Dockerfile instruction creating a new layer. Unchanged layers are cached, optimizing build times.
- **Container Lifecycle:** Containers can be created, started, stopped, restarted, and removed. Understanding states (running, stopped, exited) is crucial for management.

### Docker Commands Mastery
- `docker build`: Creates images from Dockerfiles
- `docker run`: Creates and starts containers from images
- `docker ps`: Lists containers (add `-a` for all, including stopped)
- `docker logs`: Views container output
- `docker stop/start/restart`: Manages container state
- `docker rm/rmi`: Removes containers and images
- `docker push/pull`: Interacts with container registries

### GitHub Actions CI/CD
- **Workflow Configuration:** YAML syntax for defining automated pipelines
- **Secrets Management:** Securely storing credentials for automated deployments
- **Automated Testing:** Running tests before deployment ensures code quality
- **Multi-step Workflows:** Chaining actions like checkout, setup, test, build, and deploy

### Python Virtual Environments
- Creating isolated Python environments with `python3 -m venv venv`
- Activating environments with `source venv/bin/activate`
- Managing dependencies with `pip` and `requirements.txt`
- Understanding why isolation prevents dependency conflicts

---

## Real-World Applications and Relevance

### Consistency Across Environments
The most significant benefit of containerization is eliminating the "it works on my machine" problem. Docker ensures the application runs identically on my Mac, a Linux server, or a Windows machine. For web API development, this consistency is crucial when deploying to production servers.

### Microservices Architecture
In modern web development, applications are often built as microservices—small, independent services that communicate via APIs. Docker is the standard for deploying microservices, with each service running in its own container. This assignment provided foundational skills for working with microservice architectures.

### DevOps Integration
The GitHub Actions integration demonstrated how Docker fits into DevOps workflows. Automated building, testing, and deployment reduce human error and enable continuous delivery. In professional settings, every code commit triggers automated pipelines that test, build containers, and deploy to staging or production environments.

### Cloud Deployment
Container registries like DockerHub are similar to services like AWS ECR, Google Container Registry, and Azure Container Registry. Understanding how to push/pull images prepares me for cloud deployments where containers are orchestrated by Kubernetes, AWS ECS, or similar platforms.

---

## Connection to Web API Development

This assignment directly relates to our Python for Web API Development course in several ways:

**Deployment:** Web APIs built with Flask, FastAPI, or Django are typically deployed in containers. This assignment taught me how to containerize Python applications, a skill I'll use when deploying course projects.

**Environment Isolation:** Different APIs may require different dependency versions. Containers ensure each API runs in its isolated environment without conflicts.

**Scalability:** Container orchestration platforms like Kubernetes can automatically scale containerized APIs based on demand, handling thousands of requests by spinning up multiple container instances.

**Portability:** APIs containerized during development can be deployed anywhere—local servers, cloud platforms, or edge computing devices—without modification.

---

## Reflection on Learning Process

This assignment challenged me to think beyond writing code to consider deployment, security, and automation. The iterative problem-solving process—encountering errors, researching solutions, and testing fixes—mirrored real-world development scenarios.

The most valuable aspect was learning to read and interpret error messages. Rather than feeling frustrated by errors, I learned to extract useful information from stack traces and use them to diagnose issues. For example, the Pillow compatibility error initially seemed cryptic, but by reading it carefully, I identified the version mismatch and found a solution.

Documentation became my best friend. Docker's official documentation, GitHub Actions reference, and Python package documentation provided answers when I was stuck. Learning to navigate technical documentation is a critical skill for any developer.

---

## Areas for Further Exploration

While this assignment provided a solid foundation, several areas warrant deeper study:

**Docker Compose:** Managing multi-container applications where the QR code generator might interact with a database or web server.

**Container Orchestration:** Learning Kubernetes for managing containers at scale in production environments.

**Security Scanning:** Using tools like Docker Scan or Trivy to identify vulnerabilities in container images.

**Optimization:** Creating smaller images using multi-stage builds and alpine Linux base images.

**Monitoring:** Implementing logging and monitoring solutions for containerized applications.

---

## Conclusion

This assignment transformed my understanding of application deployment and modern development practices. I moved from abstract knowledge of containers to practical experience building, running, and deploying Docker images. The challenges I faced—dependency management, authentication configuration, and tooling unfamiliarity—provided valuable learning opportunities that deepened my understanding.

Most importantly, I now appreciate why containerization has become the industry standard for application deployment. The benefits of consistency, isolation, and portability solve real problems that developers face daily. As I continue developing web APIs in this course, I'll apply containerization from the start, building deployment-ready applications that can run anywhere.

The integration of Docker with GitHub Actions showed me how modern DevOps practices automate tedious tasks, allowing developers to focus on writing code rather than managing infrastructure. This automated pipeline—commit code, test automatically, build containers, deploy to registry—is the workflow used by software teams worldwide.

Overall, this assignment provided not just technical skills but a mindset shift toward thinking about applications holistically, from development through deployment and maintenance. These are foundational skills for any modern software developer, and I'm grateful for the practical, hands-on approach that made these concepts concrete rather than abstract.

---

## Resources Utilized

- Docker Official Documentation: https://docs.docker.com
- Docker Desktop for Mac: https://docs.docker.com/desktop/install/mac-install/
- DockerHub: https://hub.docker.com
- GitHub Actions Documentation: https://docs.github.com/en/actions
- Python qrcode Library: https://pypi.org/project/qrcode/
- Pillow Documentation: https://pillow.readthedocs.io/
- Course Materials and Assignment Instructions
- Stack Overflow for troubleshooting specific errors

---

