terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "s3_raw_bucket" {
  bucket = var.name_s3_raw_bucket
}

resource "aws_s3_bucket" "s3_curated_bucket" {
  bucket = var.name_s3_curated_bucket
}

resource "aws_s3_bucket" "s3_jobs_dev_bucket" {
  bucket = var.name_s3_curated_bucket
}

resource "aws_glue_crawler" "crawler_raw_zone" {
  database_name = "crimes_database_raw_dev"
  name          = "crawler-crimes-raw-dev"
  role          = "arn:aws:iam::730335317825:role/glue-rol"
  s3_target {
    path = "s3://crimes-raw-dev"
  }
  table_prefix = "crimes_raw_dev"
  depends_on = [aws_s3_bucket.s3_raw_bucket]
}

resource "aws_glue_crawler" "crawler_curated_zone" {
  database_name = "crimes_database_curated_dev"
  name          = "crawler-crimes-curated-dev"
  role          = "arn:aws:iam::730335317825:role/glue-rol"
  s3_target {
    path = "s3://crimes-curated-dev"
  }
  table_prefix = "crimes_curated_dev"
  depends_on = [aws_s3_bucket.s3_raw_bucket]
}

resource "aws_glue_job" "crimes_job" {
  name         = "crimes_job_dev"
  role_arn     = "arn:aws:iam::730335317825:role/glue-rol"
  max_retries  = 0
  glue_version = "4.0"
  max_capacity = 2
  timeout      = 10
  command {
    name            = "crimes_job_dev"
    python_version  = 3.0
    script_location = ""
    }
}

#resource "aws_glue_catalog_database" "crimes_database_raw_dev" {
#  name = "crimes_database_raw_dev"
#}
#
#resource "aws_glue_catalog_table" "crimes_raw_dev" {
#  name          = "crimes_raw_dev"
#  database_name = aws_glue_catalog_database.crimes_database_raw_dev.name
#  depends_on = [aws_glue_catalog_database.crimes_database_raw_dev]
#}
#
#resource "aws_glue_catalog_database" "crimes_database_curated_dev" {
#  name = "crimes_database_raw_dev"
#}
#
#resource "aws_glue_catalog_table" "crimes_curated_dev" {
#  name          = "crimes_curated_dev"
#  database_name = aws_glue_catalog_database.crimes_database_curated_dev.name
#  depends_on = [aws_glue_catalog_database.crimes_database_curated_dev]
#}

