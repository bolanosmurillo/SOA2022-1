terraform {
  backend "gcs" {
    bucket = "soabuilder"
    prefix = "env/dev"
  }
}





