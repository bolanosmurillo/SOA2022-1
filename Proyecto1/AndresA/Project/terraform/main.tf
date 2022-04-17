provider "google" {
  credentials = file("/home/aalopz/.config/gcloud/application_default_credentials.json")
  project = var.project_id
  region  = var.region
} 