variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "name_s3_raw_bucket"{
    description = "S3 bucket Raw"
    type = string
    default = "crimes-raw-dev"
}

variable "name_s3_curated_bucket"{
    description = "S3 bucket Curated"
    type = string
    default = "crimes-curated-dev"
}

variable "name_s3_job_dev_bucket"{
    description = "S3 bucket JOBA"
    type = string
    default = "jobs-files-dev"
}
