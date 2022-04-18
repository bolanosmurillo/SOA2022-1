resource "google_storage_bucket" "function_bucket" {
    name     = "${var.project}-function"
}

resource "google_storage_bucket" "input_bucket" {
    name     = "${var.project}-input"
} 
