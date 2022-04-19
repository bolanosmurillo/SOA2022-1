resource "google_storage_bucket" "function_bucket" {
    name     = "${var.project}-function-prod"
    location = var.region
}

resource "google_storage_bucket" "input_bucket" {
    name     = "${var.project}-input-prod"
    location = var.region
}