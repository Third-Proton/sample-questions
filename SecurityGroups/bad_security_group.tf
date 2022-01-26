resource "aws_security_group" "server_access" {
  name        = "server-access-sg"
  vpc_id      = aws_vpc.main.id

  ingress {
    description      = "Allow HTTP and HTTPS access"
    from_port        = 80
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["10.0.0.0/8"]
  }

  ingress {
    description      = "Allow SSH access"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "Allow RDP access"
    from_port        = 3389
    to_port          = 3389
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "Allow MySQL access"
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    cidr_blocks      = ["10.32.25.0/24"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}