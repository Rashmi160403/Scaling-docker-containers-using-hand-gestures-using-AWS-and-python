#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import boto3

def lambda_handler(event, context):
  
    ssm_client = boto3.client('ssm', region_name='ap-south-1')
    
    cmd = { "commands": [ "docker run -dit ubuntu:14.04" ] }
    
    ssm_client.send_command(DocumentName="AWS-RunShellScript", InstanceIds=["i-01377b34903a0e27c"], Parameters=cmd )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Docker Launched!')
    }

