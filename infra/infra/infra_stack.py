from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb
    
)
from constructs import Construct


class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamodb.Table(self,
            "ConfigTable",
            table_name="config-table",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.NUMBER),
            sort_key=dynamodb.Attribute(name="user_id", type=dynamodb.AttributeType.STRING))
