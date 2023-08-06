# VPC ----------------------------------------------
data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "main" {
    cidr_block           = "10.0.0.0/16"
    enable_dns_hostnames = true
    tags = {
        Name = var.cluster_name
    }
}

resource "aws_subnet" "public" {
    count = var.az_count
    vpc_id                  = aws_vpc.main.id
    cidr_block              = cidrsubnet (aws_vpc.main.cidr_block, 8, var.az_count + count.index)
    availability_zone       = data.aws_availability_zones.available.names [count.index]
    map_public_ip_on_launch = true
    tags = {
        Name = "${var.cluster_name}-net-public-${count.index}"
    }
}

resource "random_shuffle" "subnets" {
  input        = [ for each in aws_subnet.public: each.id ]
  result_count = 1
}

# gateways ----------------------------------------------
resource "aws_internet_gateway" "external" {
    vpc_id = aws_vpc.main.id
}

resource "aws_route_table" "main" {
    vpc_id = aws_vpc.main.id
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.external.id
    }
}

resource "aws_route_table_association" "external-pub" {
    count = var.az_count
    subnet_id      = aws_subnet.public [count.index].id
    route_table_id = aws_route_table.main.id
}
