terraform {
  backend "gcs" {
    bucket = "project1-30566-tfstate"
    prefix = "env/dev"
  }
}