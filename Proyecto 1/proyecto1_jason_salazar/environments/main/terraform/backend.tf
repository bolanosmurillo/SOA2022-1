terraform {
  backend "gcs" {
    bucket = "project1-prod-346217-tfstate"
  }
}