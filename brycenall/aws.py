from boto3.session import Session


def get_secret(secret_name: str, region_name: str = "us-east-1") -> str:
    client = Session().client(service_name="secretsmanager", region_name=region_name)
    secret = client.get_secret_value(**{"SecretId": secret_name})["SecretString"]
    return secret
