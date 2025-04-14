import pytest
from unittest.mock import patch
from lambda_function import lambda_handler
import json

def test_lambda_handler():
    event = {'pathParameters': {'id': 'visitorCountId'}}
    context = {}

    with patch('boto3.resource') as mock_dynamodb:
        mock_table = mock_dynamodb.return_value.Table.return_value
        mock_table.get_item.return_value = {
            'Item': {'id': 'visitorCountId', 'count': 5}
        }

        response = lambda_handler(event, context)

        assert response['statusCode'] == 200

        # Parse the stringified JSON body
        body = json.loads(response['body'])

        assert body['id'] == 'visitorCountId'
        assert body['count'] == 5