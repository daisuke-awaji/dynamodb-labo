import json
import boto3

dynamodb = boto3.resource('dynamodb')

SOURCE_TABLE = 'my-table-001'
TARGET_TABLE = 'my-table-002'

def lambda_handler(event, context):

    print(SOURCE_TABLE + "テーブルから全件取得")
    source = dynamodb.Table(SOURCE_TABLE)
    response = source.scan()
    items = response['Items']
    print(items)

    print(TARGET_TABLE + "テーブルに全件書き込み")
    target = dynamodb.Table(TARGET_TABLE)
    with target.batch_writer() as batch:
        for item in items:
            print(item)
            batch.put_item(
                Item=item
            )


lambda_handler("a", "b")

# # create a new item
    # table001.put_item(
    #     Item={
    #         'id': '0001',
    #         'user': 'awaji',
    #         'age': '26'
    #     }
    # )
    #
    # response = table001.get_item(
    #     Key={
    #         'id': '0001'
    #     }
    # )
    #
    # item = response['Item']
    #
    # print(item)
    #
    # with table001.batch_writer() as batch:
    #     for i in range(50):
    #         batch.put_item(
    #             Item={
    #                 'id': str(i),
    #                 'account_type': 'anonymous',
    #                 'username': 'user' + str(i),
    #                 'first_name': 'unknown',
    #                 'last_name': 'unknown'
    #             }
    #         )
