from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb
    
)
from constructs import Construct


class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        config_table = dynamodb.Table(self,
            "ConfigTable",
            table_name="MeterConfigs",
            partition_key=dynamodb.Attribute(name="meterSize", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="projectName", type=dynamodb.AttributeType.STRING))

        mpm_jobs_table = dynamodb.Table(self,
            "MPMJobs",
            table_name="MPMJobs",
            partition_key=dynamodb.Attribute(name="userUuid", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="timestamp", type=dynamodb.AttributeType.STRING))
