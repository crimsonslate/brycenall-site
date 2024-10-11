import boto3
from botocore.exceptions import ClientError


def get_secret(secret_name: str, region_name: str = "us-east-1") -> str:
        session = boto3.session.Session()
        client = session.client(
            service_name="secretsmanager",
            region_name=region_name
        )

        try:
            secret_value_response = client.get_secret_value(SecretId=secret_name)
        except ClientError as e:
            raise e

        return secret_value_response["SecretString"]
