provider "aws" {
  region = "us-east-1"
}

module "lambda" {
  source = "../modules/lambda_function"

  function_name = "my-function"
  filename = "./mylambda.zip"
  handler = "lambda_function.handler"
}