resource "google_storage_bucket" "function_bucket" {
    name     = "${var.project_id}-function-prod"
    location = var.region
}

resource "google_storage_bucket" "input_bucket" {
    name     = "${var.project_id}-input-prod"
    location = var.region
}