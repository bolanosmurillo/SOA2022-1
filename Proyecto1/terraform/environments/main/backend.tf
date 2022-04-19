
terraform {
  backend "gcs" {
    bucket = "buidsoa"
    prefix = "env/prod"
  }
}
