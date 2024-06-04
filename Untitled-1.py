# import boto3
# import sys

# def create_certificate(domain_name, validation_method):
#     client = boto3.client('acm')
#     response = client.request_certificate(
#         DomainName=domain_name,
#         ValidationMethod=validation_method
#     )
#     return response

# def delete_certificate(certificate_arn):
#     client = boto3.client('acm')
#     response = client.delete_certificate(
#         CertificateArn=certificate_arn
#     )
#     return response

# def export_certificate(certificate_arn, passphrase):
#     client = boto3.client('acm')
#     response = client.export_certificate(
#         CertificateArn=certificate_arn,
#         Passphrase=passphrase
#     )
#     return response

# def renew_certificate(certificate_arn):
#     client = boto3.client('acm')
#     response = client.renew_certificate(
#         CertificateArn=certificate_arn
#     )
#     return response

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python script.py <operation> [parameters...]")
#         sys.exit(1)

#     operation = sys.argv[1]

#     if operation == 'create':
#         if len(sys.argv) != 4:
#             print("Usage: python script.py create <domain_name> <validation_method>")
#             sys.exit(1)
#         domain_name = sys.argv[2]
#         validation_method = sys.argv[3]
#         print(create_certificate(domain_name, validation_method))

#     elif operation == 'delete':
#         if len(sys.argv) != 3:
#             print("Usage: python script.py delete <certificate_arn>")
#             sys.exit(1)
#         certificate_arn = sys.argv[2]
#         print(delete_certificate(certificate_arn))

#     elif operation == 'export':
#         if len(sys.argv) != 4:
#             print("Usage: python script.py export <certificate_arn> <passphrase>")
#             sys.exit(1)
#         certificate_arn = sys.argv[2]
#         passphrase = sys.argv[3].encode()  # passphrase should be a bytes object
#         print(export_certificate(certificate_arn, passphrase))

#     elif operation == 'renew':
#         if len(sys.argv) != 3:
#             print("Usage: python script.py renew <certificate_arn>")
#             sys.exit(1)
#         certificate_arn = sys.argv[2]
#         print(renew_certificate(certificate_arn))

#     else:
#         print("Invalid operation. Available operations: create, delete, export, renew")










# python script.py create example.com DNS

# python script.py delete arn:aws:acm:region:account:certificate/certificate-id

# python script.py export arn:aws:acm:region:account:certificate/certificate-id "your-passphrase"

# python script.py renew arn:aws:acm:region:account:certificate/certificate-id






















# To implement this script on Jenkins, you need to set up a Jenkins job that can execute the Python script with the necessary parameters. Below is a step-by-step guide to achieve this:

# Prerequisites
# Jenkins installed: Make sure Jenkins is up and running.
# AWS CLI and boto3: Ensure that AWS CLI is installed on the Jenkins server and that boto3 is installed in the environment where the job will run.
# AWS Credentials: Ensure that AWS credentials are configured on the Jenkins server. You can configure this in a few ways:
# Using environment variables (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY).
# Using an AWS credentials file (~/.aws/credentials).
# Using an IAM role attached to the Jenkins server if it's running on AWS.
# Step-by-Step Guide
# Step 1: Install Necessary Plugins
# Install the Python Plugin for Jenkins to enable running Python scripts.
# Install the Pipeline Plugin to create Jenkins pipelines if not already installed.
# Step 2: Create a Jenkins Pipeline Job
# Go to Jenkins Dashboard: Click on "New Item".
# Enter Job Name: Choose a name for your job.
# Select Pipeline: Select "Pipeline" and click "OK".
# Step 3: Configure the Pipeline Script
# You can use a pipeline script (Jenkinsfile) to configure the job. Here's an example pipeline script that runs the Python script with different operations.



# pipeline {
#     agent any

#     # environment {
#     #     AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
#     #     AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
#     #     AWS_DEFAULT_REGION = 'your-aws-region'
#     # }

#     parameters {
#         choice(name: 'OPERATION', choices: ['create', 'delete', 'export', 'renew'], description: 'Choose the operation')
#         string(name: 'DOMAIN_NAME', defaultValue: '', description: 'Domain name for certificate creation')
#         string(name: 'VALIDATION_METHOD', defaultValue: 'DNS', description: 'Validation method for certificate creation')
#         string(name: 'CERTIFICATE_ARN', defaultValue: '', description: 'Certificate ARN for delete/export/renew')
#         string(name: 'PASSPHRASE', defaultValue: '', description: 'Passphrase for exporting certificate')
#     }

#     stages {
#         stage('Install Dependencies') {
#             steps {
#                 sh 'pip install boto3'
#             }
#         }

#         stage('Run Python Script') {
#             steps {
#                 script {
#                     def operation = params.OPERATION
#                     def domainName = params.DOMAIN_NAME
#                     def validationMethod = params.VALIDATION_METHOD
#                     def certificateArn = params.CERTIFICATE_ARN
#                     def passphrase = params.PASSPHRASE

#                     if (operation == 'create') {
#                         sh "python script.py create ${domainName} ${validationMethod}"
#                     } else if (operation == 'delete') {
#                         sh "python script.py delete ${certificateArn}"
#                     } else if (operation == 'export') {
#                         sh "python script.py export ${certificateArn} ${passphrase}"
#                     } else if (operation == 'renew') {
#                         sh "python script.py renew ${certificateArn}"
#                     }
#                 }
#             }
#         }
#     }
# }












# Step 4: Set Up AWS Credentials
# Use Jenkins credentials store to securely manage AWS credentials.
# Add credentials (aws-access-key-id and aws-secret-access-key) in Jenkins and use them in the pipeline script as shown in the environment block.
# Step 5: Add the Python Script to Jenkins
# Store your Python script (script.py) in a version control system (e.g., GitHub).
# Configure the Jenkins job to check out the script from your repository.







# pipeline {
#     agent any

#     environment {
#         AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
#         AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
#         AWS_DEFAULT_REGION = 'your-aws-region'
#     }

#     parameters {
#         choice(name: 'OPERATION', choices: ['create', 'delete', 'export', 'renew'], description: 'Choose the operation')
#         string(name: 'DOMAIN_NAME', defaultValue: '', description: 'Domain name for certificate creation')
#         string(name: 'VALIDATION_METHOD', defaultValue: 'DNS', description: 'Validation method for certificate creation')
#         string(name: 'CERTIFICATE_ARN', defaultValue: '', description: 'Certificate ARN for delete/export/renew')
#         string(name: 'PASSPHRASE', defaultValue: '', description: 'Passphrase for exporting certificate')
#     }

#     stages {
#         stage('Checkout Code') {
#             steps {
#                 git 'https://github.com/your-repo/your-script-repo.git'
#             }
#         }

#         stage('Install Dependencies') {
#             steps {
#                 sh 'pip install boto3'
#             }
#         }

#         stage('Run Python Script') {
#             steps {
#                 script {
#                     def operation = params.OPERATION
#                     def domainName = params.DOMAIN_NAME
#                     def validationMethod = params.VALIDATION_METHOD
#                     def certificateArn = params.CERTIFICATE_ARN
#                     def passphrase = params.PASSPHRASE

#                     if (operation == 'create') {
#                         sh "python script.py create ${domainName} ${validationMethod}"
#                     } else if (operation == 'delete') {
#                         sh "python script.py delete ${certificateArn}"
#                     } else if (operation == 'export') {
#                         sh "python script.py export ${certificateArn} ${passphrase}"
#                     } else if (operation == 'renew') {
#                         sh "python script.py renew ${certificateArn}"
#                     }
#                 }
#             }
#         }
#     }
# }







# Step 6: Run the Job
# Save the Jenkins job configuration.
# Trigger the job manually and select the required parameters.
# This setup will enable you to manage AWS certificates using Jenkins by providing appropriate parameters for different operations.






# import fitz

# input_file = "/home/khanak/Downloads/Impactsure Technologies- Increment Letter 2024 (Khanak Rawal,) (1).pdf"
# input_file1 = "/home/khanak/Downloads/Impactsure Technologies- Increment Letter 2024 (Khanak Rawal,)1.pdf"
# output_file = "/home/khanak/Downloads/Impactsure Technologies- Increment Letter 2024 (Khanak Rawal) with-sign.pdf"
# barcode_file = r"/home/khanak/Downloads/khanak_signature.png"

# def test_func(input_file,input_file1):
#     doc = fitz.open(input_file)
#     for page in doc:
#         page.wrap_contents()
#         # do some other stuff
#     doc.save(input_file1)

# test_func(input_file,input_file1)
# # define the position (upper-right corner)
# image_rectangle = fitz.Rect(450,20,550,1320)

# # retrieve the first page of the PDF
# file_handle = fitz.open(input_file1)
# first_page = file_handle[0]
# img = open(barcode_file, "rb").read()
# # add the image
# first_page.insert_image(image_rectangle, stream=img)

# file_handle.save(output_file)




















#import boto3
import sys

def create_certificate(domain_name, validation_method):
    # client = boto3.client('acm')
    # response = client.request_certificate(
    #     DomainName=domain_name,
    #     ValidationMethod=validation_method
    # )
    return "Create certificate done"

def delete_certificate(certificate_arn):
    # client = boto3.client('acm')
    # response = client.delete_certificate(
    #     CertificateArn=certificate_arn
    # )
    return "Delete certificate done"

def export_certificate(certificate_arn, passphrase):
    # client = boto3.client('acm')
    # response = client.export_certificate(
    #     CertificateArn=certificate_arn,
    #     Passphrase=passphrase
    # )
    return "Export certificate done"

def renew_certificate(certificate_arn):
    # client = boto3.client('acm')
    # response = client.renew_certificate(
    #     CertificateArn=certificate_arn
    # )
    return "Renew certificate done"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <operation> [parameters...]")
        sys.exit(1)

    operation = sys.argv[1]

    if operation == 'create':
        if len(sys.argv) != 4:
            print("Usage: python script.py create <domain_name> <validation_method>")
            sys.exit(1)
        domain_name = sys.argv[2]
        validation_method = sys.argv[3]
        print(create_certificate(domain_name, validation_method))

    elif operation == 'delete':
        if len(sys.argv) != 3:
            print("Usage: python script.py delete <certificate_arn>")
            sys.exit(1)
        certificate_arn = sys.argv[2]
        print(delete_certificate(certificate_arn))

    elif operation == 'export':
        if len(sys.argv) != 4:
            print("Usage: python script.py export <certificate_arn> <passphrase>")
            sys.exit(1)
        certificate_arn = sys.argv[2]
        passphrase = sys.argv[3].encode()  # passphrase should be a bytes object
        print(export_certificate(certificate_arn, passphrase))

    elif operation == 'renew':
        if len(sys.argv) != 3:
            print("Usage: python script.py renew <certificate_arn>")
            sys.exit(1)
        certificate_arn = sys.argv[2]
        print(renew_certificate(certificate_arn))

    else:
        print("Invalid operation. Available operations: create, delete, export, renew")


