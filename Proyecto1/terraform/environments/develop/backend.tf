terraform {
  backend "gcs" {
    bucket = "soa1"
    prefix = "env/dev"
  }
}





