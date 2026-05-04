import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses')

def lambda_handler(event, context):
    print("Lambda started")
    
    try:
        # Parse the incoming form data
        body = json.loads(event['body'])
        name = body.get('name')
        email = body.get('email')
        message = body.get('message')
        
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        # Create a unique ID
        submission_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        
        # Save to DynamoDB
        table = dynamodb.Table('ContactFormSubmissions')
        table.put_item(
            Item={
                'ID': submission_id,
                'name': name,
                'email': email,
                'message': message,
                'timestamp': timestamp
            }
        )
        
        print("Saved to DynamoDB successfully")
        
        # Send email notification
        email_subject = f"New Contact Form Submission from {name}"
        email_body = f"""
You received a new message from your resume website:

Name: {name}
Email: {email}
Message: {message}

Submission ID: {submission_id}
Timestamp: {timestamp}
        """
        
        ses.send_email(
            Source='lekeakakevin@gmail.com',
            Destination={'ToAddresses': ['lekeakakevin@gmail.com']},
            Message={
                'Subject': {'Data': email_subject},
                'Body': {'Text': {'Data': email_body}}
            }
        )
        
        print("Email sent successfully")
        
        # Return success
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'message': 'Message sent successfully! I will get back to you soon.'})
        }
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'error': str(e)})
        }