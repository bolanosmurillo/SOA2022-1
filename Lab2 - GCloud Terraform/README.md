This is a minimal Laboratory to deploy a cloud function into your GCP environment

Pre-requisites:

1. Install gcloud in your local machine
2. Install terraform in your local machine

Steps:
1. Log into your GCP account from the command line using: gcloud auth login, gcloud auth application-default login 
2. Create a GCP project 
3. Create a git repo and add the following structure to your project: 
```
project
│   README.md
│
└───terraform
│   │   backend.tf
│   │   bucket.tf
│   │   cloud_function.tf
│   │   main.tf
│   │   variables.tf
│   │
│   └───modules
│       │   ...
│   
└───cloud_funciton
    │   main.py
    │   requirements.txt
```

4. Fill the code in the files as the guide explains
5. cd into the terraform folder
6. In the cli execute terraform init, terraform plan and terraform apply once the changes are ready
7. Check your app function