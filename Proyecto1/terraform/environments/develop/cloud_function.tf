data "archive_file" "source" {
    type        = "zip"
    source_dir  = "../../../cloud_function"
    output_path = "/tmp/cloud_function.zip"
}
resource "google_storage_bucket_object" "zip" {
    source       = data.archive_file.source.output_path
    content_type = "application/zip"

    # Append to the MD5 checksum of the files's content
    # to force the zip to be updated as soon as a change occurs
    name         = "src-${data.archive_file.source.output_md5}.zip"
    bucket       = google_storage_bucket.function_bucket.name

}

resource "google_cloudfunctions_function" "function" {
    name                  = "Vision"
    runtime               = "python37"  # of course changeable

    # Get the source code of the cloud function as a Zip compression
    source_archive_bucket = google_storage_bucket.function_bucket.name
    source_archive_object = google_storage_bucket_object.zip.name

    # Must match the function name in the cloud function `main.py` source code
    entry_point           = "main" 



}