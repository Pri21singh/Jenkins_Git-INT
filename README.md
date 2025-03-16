# Python Application with Jenkins CI/CD Pipeline

This repository contains a basic Python application integrated with Jenkins for continuous integration and deployment (CI/CD). The application is configured to automatically trigger builds using a polling-based approach whenever changes are made to the code in the GitHub repository.

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Jenkins Setup](#jenkins-setup)
4. [Pipeline Configuration](#pipeline-configuration)
5. [Testing and Verification](#testing-and-verification)
6. [CI/CD Workflow](#cicd-workflow)
7. [Conclusion](#conclusion)

## Overview

This project demonstrates how to configure a basic Python application with a Jenkins pipeline that:
- Polls GitHub for changes every 2 minutes.
- Runs the build and test process whenever changes are detected in the GitHub repository.
- Sends notifications to a specified email in case of build success or failure.

## Prerequisites

Before running this project, make sure you have the following:

- **Jenkins Server**: A working Jenkins setup with the necessary plugins.
  - Git Plugin
  - Pipeline Plugin
  - Email Extension Plugin
- **GitHub Repository**: A GitHub repository containing the Python application.
- **Personal Access Token (PAT)**: A GitHub PAT for Jenkins to access the repository.
- **Email Configuration**: Set up email notifications in Jenkins.

## Jenkins Setup

To set up Jenkins for this Python application:

1. **Install Jenkins Plugins**:
   - Ensure that the **Git**, **Pipeline**, and **Email Extension** plugins are installed in Jenkins.

2. **Configure GitHub Integration**:
   - In Jenkins, navigate to **Manage Jenkins** → **Configure System**.
   - Under **GitHub**, add your GitHub repository URL and configure authentication using your **Personal Access Token (PAT)**.

3. **Create Jenkins Pipeline Job**:
   - Go to Jenkins → **New Item** → **Pipeline**.
   - Name your job (e.g., `python-ci-pipeline`).
   - Configure it to use the **Pipeline script from SCM** option and point it to your GitHub repository.

## Pipeline Configuration

This project uses a **Jenkinsfile** to define the CI/CD pipeline. The file includes the following stages:

1. **Checkout**: Clones the repository from GitHub.
2. **Build**: Simulates the build process for the Python application (e.g., package the app, etc.).
3. **Test**: Runs basic tests (e.g., Python tests or unit tests).
4. **Notification**: Sends a success or failure notification via email.