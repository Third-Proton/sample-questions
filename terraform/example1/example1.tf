resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket"
  tags = {
    Name = "My Bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_acl" "my_bucket" {
  bucket = aws_s3_bucket.my_bucket.id
  acl = "private"
}

resource "aws_s3_bucket_versioning" "my_bucket" {
  bucket = aws_s3_bucket.my_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}