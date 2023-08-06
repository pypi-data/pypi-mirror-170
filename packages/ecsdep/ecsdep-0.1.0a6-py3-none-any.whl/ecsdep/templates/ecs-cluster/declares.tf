terraform {
  required_version = ">= 1.1.2"
  backend "s3" {
    bucket  = "states-data"
    key     = "terraform/ecs-cluster/skitai-cluster/terraform.tfstate"
    region  = "ap-northeast-2"
    encrypt = true
    acl     = "bucket-owner-full-control"
  }
}

provider "aws" {
  region  = "ap-northeast-1"
}

variable "cluster_name" {
  default = "skitai-cluster"
}

variable "instance_type" {
  default = "t3.micro"
}

variable "ami" {
  default = "amzn2-ami-ecs-hvm-*-x86_64-*"
}

variable "cors_hosts" {
  default = ["http://localhost:5000", "https://skitai.sns.co.kr", "https://skitai-qa.sns.co.kr"]
}

variable "cert_name" {
  default = "sns.co.kr"
}

variable "public_key_file" {
  default = "/my/config/path/public-key.pem"
}

variable "autoscale" {
  default = {
    desired = 1
    min = 1
    max = 20
    cpu = 70
    memory = 50
  }
}

variable "az_count" {
  default = 2
}