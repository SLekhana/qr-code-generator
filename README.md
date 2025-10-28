# QR Code Generator
# QR Code Generator - Dockerized Python Application

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Docker](https://img.shields.io/badge/docker-enabled-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A containerized Python application that generates QR codes from URLs with support for custom configurations, logging, and automated CI/CD deployment.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running Locally](#running-locally)
  - [Running with Docker](#running-with-docker)
- [Docker Hub](#docker-hub)
- [GitHub Actions CI/CD](#github-actions-cicd)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🎯 Overview

This project demonstrates modern DevOps practices by containerizing a Python-based QR Code Generator application. The application generates QR codes from URLs, stores them with timestamps, and maintains operation logs. It's fully Dockerized with automated CI/CD pipelines using GitHub Actions.

**Course:** Python for Web API Development  
**Assignment:** Dockerizing Applications  
**Institution:** NJIT  

---

## ✨ Features

- 🎨 **QR Code Generation**: Creates high-quality QR codes from any URL
- 📦 **Docker Support**: Fully containerized for consistent deployment
- 🔒 **Security-First**: Runs as non-root user inside containers
- 📝 **Logging**: Comprehensive logging of all operations
- ⚙️ **Configurable**: Command-line arguments for flexible usage
- 🔄 **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions
- 💾 **Persistent Storage**: Volume mounting support for data persistence
- 🐳 **DockerHub Integration**: Publicly available container images

---

## 📦 Prerequisites

### For Local Development:
- Python 3.12 or higher
- pip (Python package manager)
- Git

### For Docker:
- Docker Desktop (Mac/Windows) or Docker Engine (Linux)
- DockerHub account (for pulling/pushing images)

### For GitHub Actions:
- GitHub account
- DockerHub account with access token

---

## 🚀 Installation

### Clone the Repository
```bash
git clone https://github.com/SLekhana/qr-code-generator.git
cd qr-code-generator
```

### Local Installation
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Mac/Linux
# OR
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 💻 Usage

### Running Locally

#### Basic Usage (Default URL)
```bash
python main.py
```

This generates a QR code for the default URL: `http://github.com/kaw393939`

#### Custom URL
```bash
python main.py --url http://www.njit.edu
```

#### Custom Output Directory
```bash
python main.py --url http://example.com --output my_qr_codes
```

#### Expected Output
```
Starting QR Code Generator...
Target URL: http://www.njit.edu
Output Directory: qr_codes
[2025-10-27 10:30:45.123456] QR Code generated for URL: http://www.njit.edu - Saved to: qr_codes/qr_code_20251027_103045.png
✓ Success! QR code saved to: qr_codes/qr_code_20251027_103045.png
```

---

### Running with Docker

#### Pull from DockerHub (Recommended)
```bash
docker pull slekhana/qr-code-generator-app:latest
docker run -d --name qr-generator slekhana/qr-code-generator-app:latest
```

#### Build Locally
```bash
# Build the Docker image
docker build -t qr-code-generator-app .

# Run the container
docker run -d --name qr-generator qr-code-generator-app
```

#### View Container Logs
```bash
docker logs qr-generator
```

#### Run with Custom URL
```bash
docker run -d --name qr-generator \
  qr-code-generator-app --url http://www.njit.edu
```

#### Run with Volume Mount (Persist QR Codes)
```bash
# Create output directory on host
mkdir -p ~/qr_codes_output

# Run container with volume mount
docker run -d --name qr-generator \
  -v ~/qr_codes_output:/app/qr_codes \
  qr-code-generator-app --url http://www.example.com

# QR codes will be saved to ~/qr_codes_output on your local machine
```

#### Container Management
```bash
# Stop container
docker stop qr-generator

# Start container
docker start qr-generator

# Remove container
docker rm qr-generator

# View running containers
docker ps

# View all containers (including stopped)
docker ps -a
```

---

## 🐳 Docker Hub

The Docker image is publicly available on DockerHub:

**Repository:** [slekhana/qr-code-generator-app](https://hub.docker.com/r/slekhana/qr-code-generator-app)

### Pull the Image
```bash
docker pull slekhana/qr-code-generator-app:latest
```

### Image Details

- **Base Image:** python:3.12-slim-bullseye
- **Size:** ~180 MB
- **Architecture:** linux/amd64
- **Security:** Runs as non-root user (myuser)

---

## 🔄 GitHub Actions CI/CD

This project includes an automated CI/CD pipeline that:

1. ✅ **Runs Tests**: Validates the application works correctly
2. 🔨 **Builds Docker Image**: Creates a new container image
3. 🚀 **Pushes to DockerHub**: Automatically deploys to DockerHub registry

### Workflow Triggers

The workflow runs automatically on:
- Push to `main` branch
- Pull requests to `main` branch

### Workflow Steps
```yaml
1. Checkout code from repository
2. Set up Python 3.12 environment
3. Install project dependencies
4. Run application tests
5. Set up Docker Buildx
6. Login to DockerHub
7. Build and push Docker image to registry
```

### View Workflow Status

Visit the [Actions tab](https://github.com/SLekhana/qr-code-generator/actions) to see workflow runs and their status.

---

## 📁 Project Structure
```
qr-code-generator/
│
├── .github/
│   └── workflows/
│       └── docker-build.yml      # GitHub Actions CI/CD workflow
│
├── main.py                        # Main application script
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker image definition
├── .gitignore                    # Git ignore patterns
├── README.md                      # Project documentation
├── REFLECTION.md                  # Assignment reflection
│
├── qr_codes/                      # Generated QR code images (created at runtime)
├── logs/                          # Application logs (created at runtime)
└── venv/                          # Virtual environment (local only)
```

---

## ⚙️ Configuration

### Command-Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--url` | string | `http://github.com/kaw393939` | URL to encode in QR code |
| `--output` | string | `qr_codes` | Output directory for QR codes |

### Environment Variables

The application can be extended to use environment variables:
```bash
export QR_OUTPUT_DIR="/custom/path"
export QR_LOG_LEVEL="DEBUG"
```

### Docker Environment Variables
```bash
docker run -d --name qr-generator \
  -e QR_OUTPUT_DIR=/app/custom_qr \
  qr-code-generator-app
```

---

## 📸 Examples

### Example 1: Generate QR Code for NJIT Website
```bash
docker run -d --name njit-qr \
  -v ~/Desktop/njit_qr:/app/qr_codes \
  qr-code-generator-app --url http://www.njit.edu
```

**Output:** QR code saved to `~/Desktop/njit_qr/qr_code_[timestamp].png`

### Example 2: Generate QR Code for GitHub Profile
```bash
python main.py --url https://github.com/SLekhana
```

**Output:** QR code saved to `qr_codes/qr_code_[timestamp].png`

### Example 3: Batch Processing Multiple URLs
```bash
# Create a script to generate multiple QR codes
for url in "http://example1.com" "http://example2.com" "http://example3.com"; do
  docker run --rm \
    -v ~/batch_qr:/app/qr_codes \
    qr-code-generator-app --url "$url"
done
```

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'qrcode'"

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Issue: "Permission denied" when writing files

**Solution:**
```bash
# Ensure output directory has correct permissions
chmod 755 qr_codes/
```

### Issue: Docker build fails with Pillow error

**Solution:**
Update `requirements.txt` to use compatible Pillow version:
```
Pillow>=10.2.0
```

### Issue: GitHub Actions fails with authentication error

**Solution:**
1. Create DockerHub access token at https://hub.docker.com/settings/security
2. Add GitHub Secrets:
   - `DOCKERHUB_USERNAME`: Your DockerHub username
   - `DOCKERHUB_TOKEN`: Your access token (not password)

### Issue: Container exits immediately

**Solution:**
Check logs to see what went wrong:
```bash
docker logs qr-generator
```

### Issue: QR codes not appearing on host machine

**Solution:**
Ensure you're using volume mounts correctly:
```bash
docker run -d --name qr-generator \
  -v $(pwd)/qr_codes_output:/app/qr_codes \
  qr-code-generator-app
```

---

## 🧪 Testing

### Run Local Tests
```bash
# Activate virtual environment
source venv/bin/activate

# Test with default URL
python main.py

# Test with custom URL
python main.py --url http://test.com

# Verify QR code was created
ls -l qr_codes/
```

### Docker Tests
```bash
# Build and test
docker build -t qr-test .
docker run --rm qr-test

# Test with volume mount
docker run --rm -v $(pwd)/test_output:/app/qr_codes qr-test
ls -l test_output/
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to all functions
- Keep functions focused and small

---

## 📄 License

This project is licensed under the MIT License - see below for details:
```
MIT License

Copyright (c) 2025 Lekhana Sandra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Author

**Lekhana Sandra**

- GitHub: [@SLekhana](https://github.com/SLekhana)
- DockerHub: [slekhana](https://hub.docker.com/u/slekhana)
- Course: Python for Web API Development
- Institution: New Jersey Institute of Technology (NJIT)

---

## 🙏 Acknowledgments

- Python qrcode library developers
- Docker community for excellent documentation
- GitHub Actions for CI/CD automation
- NJIT Computer Science Department
- Course Instructor for assignment guidance

---

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Python qrcode Library](https://pypi.org/project/qrcode/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [DockerHub](https://hub.docker.com/)
- [Python Best Practices](https://docs.python-guide.org/)

---

## 🎓 Educational Purpose

This project was created as part of a Docker containerization assignment for the Python for Web API Development course at NJIT. It demonstrates:

- Docker containerization best practices
- Security implementation (non-root users)
- CI/CD pipeline automation
- Python application development
- Git version control
- Documentation standards

---

## 📊 Project Status

![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![Docker](https://img.shields.io/badge/docker-automated-blue.svg)

**Status:** ✅ Complete and Deployed

**Last Updated:** October 27, 2025

---

## 📧 Contact

For questions or support, please open an issue on GitHub or contact the author.

---

**⭐ If you find this project useful, please consider giving it a star on GitHub!**
