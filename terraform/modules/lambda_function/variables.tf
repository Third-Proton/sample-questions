##################################################################################
# VARIABLES
##################################################################################
variable "function_name" {
  type = string
}

variable "handler" {
  type = string
}

variable "filename" {
  type = string
}

variable "memory_size" {
  type = number
  default = 512
}

variable "runtime" {
  type = string
  default = "nodejs12.x"
}

variable "timeout" {
  type = number
  default = 60
}

variable "iam_role" {
  type = string
}

variable "env_vars" {
  type = map(string)
  default = {}
}

variable "schedule_expression" {
  type = string
  default = ""
}
