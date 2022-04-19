resource "google_storage_bucket" "function_bucket" {
    name = "${var.project_id}-function"
    location = "europe-west1"
}
resource "google_storage_bucket" "input" {
    name = "${var.project_id}-input"
    location = "europe-west1"
}