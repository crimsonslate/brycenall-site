from boto3.session import Session


def get_secret(secret_name: str, region_name: str = "us-east-1") -> str:
        session = Session()
        client = session.client(
            service_name="secretsmanager",
            region_name=region_name
        )
        secret = client.get_secret_value(**{"SecretId": secret_name}).get("SecretString", "")
        return secret
