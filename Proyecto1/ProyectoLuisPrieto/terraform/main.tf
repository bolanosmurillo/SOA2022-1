#Configura el ambiente local

locals {
  env = "dev"
}

#Configura el proveedor de Google

provider "google" {
  project = var.project
  region = var.region
}
