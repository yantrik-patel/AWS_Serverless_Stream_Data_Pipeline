import random
import json
import datetime
import boto3


# partition_key: we will set it to some fixed value as we want processing order to be preserved when writing successive records

# If our Kinesis stream has multiple shards, AWS will hash our partition key to decide which shard will handle our records.
# we can ignore using partition key if processing order is not important or we have only one shard.


def getSessionId():
    return str(random.randint(1,10000))
    
    
def getReferrer():
    #generate random user and device ids
    x = random.randint(1,5)
    x = x * 50
    y = x + 35
    data = {}
    data['user_id'] = random.randint(x,y)
    data['device_id'] = random.choice(['mobile','computer','tablet','laptop','public_pc'])
    
    #generate random client event like user actions on website
    data['client_event'] = random.choice(['nav_bar_click','checkout','product_detail','products','selection','cart'])
    
    #generate the current time stamp
    now = datetime.datetime.now()
    str_now = now.isoformat()
    data['client_timestamp'] = str_now
    
    
    return data
    

def lambda_handler(event, context):
    #create Kinesis Client
    kinesis = boto3.client('kinesis')
    session_id = getSessionId()
    
    #generate click stream data and send it to Kinesis stream
    for i in range(10): #we can customize howmany records we want to send in one go
        data = json.dumps(getReferrer())
        kinesis.put_ecord(
            StreamName = 'myKinesisDataStream',
            Data = data,
            PartitionKey=session_id
        )
