terraform {
  required_version = ">= 1.1.2"
  backend "s3" {
    bucket  = "states-data"
    key     = "terraform/ecs-cluster/skitai-cluster/task-def/ecsdep/terraform.tfstate"
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

# variables -----------------------------------------------
variable "awslog_region" {
  default = "ap-northeast-1"
}

variable "stages" {
  default = {
    default = {
        env_service_stage = "qa"
        hosts = ["skitai-qa.sns.co.kr"]
        listener_priority = 100
        service_name = "ecsdep-qa"
        task_definition_name = "ecsdep-qa-task"
    }
    production = {
        env_service_stage = "production"
        hosts = ["skitai.sns.co.kr"]
        listener_priority = 101
        service_name = "ecsdep"
        task_definition_name = "ecsdep-task"
    }
  }
}

variable "service_auto_scaling" {
  default = {
    desired_count = 1
    min = 1
    max = 4
    cpu = 75
    memory = 80
  }
}

variable "exposed_container" {
  default = [{
    name = "skitai-nginx"
    port = 80
  }]
}

variable "loggings" {
  default = ["skitai-app", "skitai-nginx"]
}

variable "loadbalancing_pathes" {
  default = ["/*"]
}
