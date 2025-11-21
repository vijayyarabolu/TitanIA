#!/bin/bash
# Update system
yum update -y

# Install Docker
yum install -y docker
service docker start
usermod -a -G docker ec2-user

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Install Git
yum install -y git

# Clone Repository (Replace with your repo URL)
# git clone https://github.com/yourusername/TitanIA.git /home/ec2-user/TitanIA
# For now, we assume you will scp the files or clone manually. 
# This script sets up the environment.

# Create app directory
mkdir -p /home/ec2-user/app
cd /home/ec2-user/app

# --- FREE TIER OPTIMIZATION: Add Swap Space ---
# t2.micro has only 1GB RAM. We need swap to run AI models + Docker.
dd if=/dev/zero of=/swapfile bs=128M count=16
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo "/swapfile swap swap defaults 0 0" >> /etc/fstab
# ----------------------------------------------

echo "Docker installed & Swap configured. Ready to deploy TitanIA."
