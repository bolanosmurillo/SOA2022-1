terraform {
  backend "gcs" {
    bucket = "soa-p1-347007-tfstate"
    prefix = "env/prod"
  }
}
