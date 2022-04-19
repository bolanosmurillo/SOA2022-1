terraform {
  backend "gcs" {
    bucket = "moon-347702-tfstate"
    prefix = "env/dev"
  }
}





