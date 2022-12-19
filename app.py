#!/usr/bin/env python3

import aws_cdk as cdk

from pluralsight_aws_infrastructure_cdk.pluralsight_aws_infrastructure_cdk_stack import PluralsightAwsInfrastructureCdkStack


app = cdk.App()
PluralsightAwsInfrastructureCdkStack(app, "pluralsight-aws-infrastructure-cdk")

app.synth()
