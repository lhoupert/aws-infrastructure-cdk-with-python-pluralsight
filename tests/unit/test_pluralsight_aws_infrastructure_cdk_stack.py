import aws_cdk as core
import aws_cdk.assertions as assertions
from pluralsight_aws_infrastructure_cdk.pluralsight_aws_infrastructure_cdk_stack import PluralsightAwsInfrastructureCdkStack


def test_sqs_queue_created():
    app = core.App()
    stack = PluralsightAwsInfrastructureCdkStack(app, "pluralsight-aws-infrastructure-cdk")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = PluralsightAwsInfrastructureCdkStack(app, "pluralsight-aws-infrastructure-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
