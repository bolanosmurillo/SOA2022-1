resource "google_storage_bucket" "function_bucket" {
    name     = "${var.project_id}-f"
    location = var.region
}

resource "google_storage_bucket" "input_bucket" {
    name     = "${var.project_id}-i"
    location = var.region
} 