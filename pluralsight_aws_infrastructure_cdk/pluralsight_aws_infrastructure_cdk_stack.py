from aws_cdk import Duration, Stack
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subs
from aws_cdk import aws_sqs as sqs
from constructs import Construct


class PluralsightAwsInfrastructureCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "PluralsightAwsInfrastructureCdkQueue",
            visibility_timeout=Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "PluralsightAwsInfrastructureCdkTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))
