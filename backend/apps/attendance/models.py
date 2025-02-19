import boto3
from botocore.exceptions import ClientError

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

def create_teacher_table():
    try:
        table = dynamodb.create_table(
            TableName='teachers',
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}  # Partition key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}  # String
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        print(f"Table '{table.table_name}' created successfully!")
    except ClientError as e:
        print(f"Error creating table 'teachers': {e}")

def create_class_table():
    try:
        table = dynamodb.create_table(
            TableName='classes',
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}  # Partition key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'},  # String
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        print(f"Table '{table.table_name}' created successfully!")
    except ClientError as e:
        print(f"Error creating table 'classes': {e}")

if __name__ == "__main__":
    create_teacher_table()
    create_class_table()
