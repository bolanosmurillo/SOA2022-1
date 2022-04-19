#Se especifican los buckets necesarios para el proyecto

resource "google_storage_bucket" "function_bucket" {
    name     = "${var.project}-function"
    location = var.region
}

#Se especifica el bucket de entrada del proyecto

resource "google_storage_bucket" "input_bucket" {
    name     = "${var.project}-input"
    location = var.region
} 
