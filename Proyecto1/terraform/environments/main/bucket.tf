resource "google_storage_bucket" "function_bucket" {
  name = "${var.project_id}-function"
  location = "us-central1"
}

resource "google_storage_bucket" "input_bucket" {
  name = "${var.project_id}-input"
  location = "us-central1"
  force_destroy=true
}