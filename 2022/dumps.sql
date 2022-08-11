SELECT
    user_id,
    user_name,
    SUM(change_in_bal) + credit AS credit,
    IF(SUM(change_in_bal) + credit < 0, "Yes", "No") AS credit_limit_breached
FROM (
SELECT
    U.user_id,
    U.user_name,
    U.credit,
    CASE WHEN U.user_id = T.paid_by THEN -T.amount
         WHEN U.user_id = T.paid_to THEN +T.amount
         ELSE 0
         END
    AS change_in_bal
FROM Users U
LEFT JOIN Transactions T
ON (U.user_id = T.paid_by OR U.user_id = T.paid_to)
      ) T
GROUP BY user_id;


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res


const AWS = require('aws-sdk');

AWS.config.update({

    region: 'us-east-1'

})

const s3 = new AWS.S3();

const kinesis = new AWS.Kinesis();

 

exports.handler = async (event) => {

    console.log(JSON.stringify(event));

    const bucketName = event.Records[0].s3.bucket.name;

    const keyName = event.Records[0].s3.object.key;

    const params = {

        Bucket: bucketName,

        Key: keyName

    }

    await s3.getObject(params).promise().then(async (data) => {

        const dataString = data.Body.toString();

        const payload = {

            data: dataString

        }

        await sendToKinesis(payload, keyName);

    }, error => {

        console.error(error);

    })

};

 

async function sendToKinesis(payload, partitionKey) {

    const params = {

        Data: JSON.stringify(payload),

        PartitionKey: partitionKey,

        StreamName: 'whiz-data-stream'

    }

    await kinesis.putRecord(params).promise().then(response => {

        console.log(response);

    }, error => {

        console.error(error);

    })

}



exports.handler = async (event) => {

    console.log(JSON.stringify(event));

    for (const record of event.Records) {

        const data = JSON.parse(Buffer.from(record.kinesis.data, 'base64'));

        console.log('consumer #1', data);

    }

};


2022-05-08T22:44:39.913Z	4669482e-b1d0-4203-b845-8be9963af914	INFO	{
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "test.txt",
                "sequenceNumber": "49629327876990770102694170468999615039319613623907647490",
                "data": "eyJkYXRhIjoiSGVsbG9cblxuVGhpcyBpcyBXaGl6bGFicy4uLlxuXG5DaGVjayBvdXQgb3VyIGNvdXJzZXNcblxuQnllIGJ5ZSEhIVxuIn0=",
                "approximateArrivalTimestamp": 1652049878.753
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000000:49629327876990770102694170468999615039319613623907647490",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::024666144133:role/kinesis-datastream-role",
            "awsRegion": "us-east-1",
            "eventSourceARN": "arn:aws:kinesis:us-east-1:024666144133:stream/whiz-data-stream"
        }
    ]
}



        