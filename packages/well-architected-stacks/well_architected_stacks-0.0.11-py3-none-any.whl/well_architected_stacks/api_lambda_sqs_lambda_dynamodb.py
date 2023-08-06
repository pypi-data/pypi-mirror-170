import aws_cdk
import constructs
import well_architected_constructs

from . import well_architected_stack


class ApiLambdaSqsLambdaDynamodb(well_architected_stack.Stack):

    def __init__(self, scope: constructs.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dynamodb_table = self.create_dynamodb_table(
            partition_key="id",
        )

        sqs_queue = aws_cdk.aws_sqs.Queue(
            self, 'SqsQueue',
            visibility_timeout=aws_cdk.Duration.seconds(300)
        )

        self.create_sqs_subscribing_lambda(
            sqs_queue=sqs_queue,
            dynamodb_table=dynamodb_table,
        )

        sqs_publishing_lambda = self.create_sqs_publishing_lambda(sqs_queue)

        well_architected_constructs.api_lambda.create_http_api_lambda(
            self, lambda_function=sqs_publishing_lambda,
            error_topic=self.error_topic,
        )
        well_architected_constructs.api_lambda.create_rest_api_lambda(
            self, lambda_function=sqs_publishing_lambda,
            error_topic=self.error_topic,
        )

    def create_dynamodb_table(self, partition_key):
        return well_architected_constructs.dynamodb_table.DynamodbTableConstruct(
            self, "DynamodbTable",
            partition_key=partition_key,
            error_topic=self.error_topic,
        ).dynamodb_table

    def create_lambda_function(
        self, function_name=None,
        environment_variables=None, concurrent_executions=None,
    ):
        return well_architected_constructs.lambda_function.create_python_lambda_function(
            self, function_name=function_name,
            environment_variables=environment_variables,
            concurrent_executions=concurrent_executions,
            error_topic=self.error_topic,
            lambda_directory=self.lambda_directory,
        )

    def create_sqs_publishing_lambda(
        self, sqs_queue:aws_cdk.aws_sqs.Queue
    ):
        lambda_function = self.create_lambda_function(
            function_name='api_lambda_sqs_lambda_dynamodb_publisher',
            environment_variables={
                'SQS_QUEUE_URL': sqs_queue.queue_url
            },
        )
        sqs_queue.grant_send_messages(lambda_function)
        return lambda_function

    def create_sqs_subscribing_lambda(
        self, sqs_queue: aws_cdk.aws_sqs.Queue=None,
        dynamodb_table:aws_cdk.aws_dynamodb.Table=None,
    ):
        lambda_function = self.create_lambda_function(
            function_name='api_lambda_sqs_lambda_dynamodb_subscriber',
            concurrent_executions=2,
            environment_variables={
                'SQS_QUEUE_URL': sqs_queue.queue_url,
                'DYNAMODB_TABLE_NAME': dynamodb_table.table_name
            },
        )
        lambda_function.add_event_source(aws_cdk.aws_lambda_event_sources.SqsEventSource(sqs_queue))
        sqs_queue.grant_consume_messages(lambda_function)
        dynamodb_table.grant_read_write_data(lambda_function)
        return lambda_function
