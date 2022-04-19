

terraform {
  backend "gcs" {
    bucket = "soavision"
    prefix = "env/dev"
  }
}
