# Serverless Contact Form for Resume Website

## Live Demo
[My Resume Website](https://d3gpt5n0a684vu.cloudfront.net)

## Architecture
- **S3 + CloudFront**: Hosts the static resume website with HTTPS
- **API Gateway**: REST API endpoint that receives form submissions
- **Lambda (Python)**: Processes submissions, validates data, saves to database, sends email
- **DynamoDB**: Stores all contact form entries
- **SES**: Sends email notification when someone submits the form

## How It Works
1. User visits my resume website and fills out the contact form
2. JavaScript sends a POST request to API Gateway
3. API Gateway triggers the Lambda function
4. Lambda saves the submission to DynamoDB
5. Lambda sends me an email via SES
6. User sees a success message on the website

## Key Features
- Fully serverless: no servers to manage
- Auto-scaling: handles any number of requests
- Cost-effective: runs entirely on AWS Free Tier
- Secure: HTTPS with CloudFront, least-privilege IAM roles

## AWS Services Used
| Service | Purpose |
|---------|---------|
| S3 | Static website hosting |
| CloudFront | CDN + HTTPS |
| API Gateway | REST API endpoint |
| Lambda | Business logic (Python) |
| DynamoDB | NoSQL database for submissions |
| SES | Email delivery |
| IAM | Security and permissions |

## Cost
All services used are within AWS Free Tier limits:
- API Gateway: 1M requests/month
- Lambda: 1M requests/month
- DynamoDB: 25GB storage
- SES: 62,000 emails/month

**Monthly cost for personal use: $0**

## Future Improvements
- Add reCAPTCHA to prevent spam
- Deploy infrastructure with CloudFormation/Terraform
- Add email reply-to field

## Connect with Me
- [LinkedIn](https://www.linkedin.com/in/kevin-lekeaka-644641386/)
- [Email](mailto:lekeakakevin@gmail.com)
