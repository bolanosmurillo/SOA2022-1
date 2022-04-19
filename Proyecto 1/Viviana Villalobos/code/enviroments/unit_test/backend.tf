terraform {
  backend "gcs" {
    bucket = "soaproyect1-tfstate"
    prefix = "env/test"
  }
}