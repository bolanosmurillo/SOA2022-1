terraform {
  backend "gcs" {
    bucket = var.buckedName
    prefix = "env/dev"
  }
}





