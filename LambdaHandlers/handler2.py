import boto3
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.batch import BatchProcessor, EventType, process_partial_response
from aws_lambda_powertools.utilities.data_classes.sqs_event import SQSRecord

logger = Logger()
processor = BatchProcessor(event_type=EventType.SQS)
tracer = Tracer()

lambda_client = boto3.client('lambda')


def record_handler(record: SQSRecord):
    data: dict = record.json_body
    logger.info(data)

    lambda_client.invoke(
        FunctionName=data['function_name'],
        InvocationType='Event',
        Payload=data['payload']
    )


@logger.inject_lambda_context
@tracer.capture_lambda_handler
def handler(event, context):
    return process_partial_response(
        event=event,
        record_handler=record_handler,
        processor=processor,
        context=context
    )
