
terraform {
  backend "gcs" {
    bucket = var.buckedName
    prefix = "env/prod"
  }
}
