variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "name_s3_raw_bucket"{
    description = "Value of the Name tag for the S3 bucket"
    type = string
    default = "crimes-raw-dev"
}

variable "name_s3_curated_bucket"{
    description = "Value of the Name tag for the S3 bucket"
    type = string
    default = "crimes-curated-dev"
}
