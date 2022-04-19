locals {
  env = "dev"
}
provider "google" {
  project = "${var.project_id}"
}


