from aws_cdk import Stack
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class LambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_function = _lambda.function(
            self,
            "WelcomeHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.asset("lambda-api"),
            handler="welcome.handler",
        )

        apigw.lambdaRestApi(self, "Endpoint", handler=hello_function)
