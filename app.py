#!/usr/bin/env python3

import aws_cdk as cdk

from pluralsight_aws_infrastructure_cdk.lambda_stack import LambdaStack

app = cdk.App()
LambdaStack(app, "LambdaStack")

app.synth()
