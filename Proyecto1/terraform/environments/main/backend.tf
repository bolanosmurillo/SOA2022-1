terraform {
  backend "gcs" {
    bucket = "soabucket1"
    prefix = "env/prod"
  }
}