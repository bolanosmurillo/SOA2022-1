#Se especifica un backend remoto con Google Cloud Storage
terraform {
  backend "gcs" {
    bucket = "proyecto1-luis-tfstate"
    prefix = "env/dev"
  }
}
