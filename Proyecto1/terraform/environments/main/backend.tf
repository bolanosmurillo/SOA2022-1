terraform {
  backend "gcs" {
    bucket = "proyectosoa2022"
    prefix = "env/prod"
  }
}