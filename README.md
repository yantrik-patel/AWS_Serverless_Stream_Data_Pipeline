# AWS_Serverless_Stream_Data_Pipeline   

This project is about handling steaming data using AWS Services.   



Following are the AWS Services I have used. 

- ***Lambda*** as data producer which mimic the web clickstream data source.
- ***AWS Kinesis datastream*** which collects the data in realtime and process it.
- ***AWS Data Firehose*** integrates the data from Kinesis data stream and writes it into S3 Bucket. We can also transform the data in Firehose using Lambda but I have not used it to simplify the process and keep project compact.
- ***S3*** is a datalake for storing the data from Firehose.

![image](https://github.com/yantrik-patel/AWS_Serverless_Stream_Data_Pipeline/assets/116425101/37c511ba-2920-42ef-a005-36f131205695)


<details>
  <summary>Setting Up Lambda</summary>

  Following are the steps to create the lambda which will act as our data source.
  - Search the 'Lambda' in the navigation search bar.
  - click the 'create function'---> Provide Function Name, Choose Runtime: Python 3.9
  - click 'Create function'.
  - Go to Code tab.
    ![image](https://github.com/yantrik-patel/AWS_Serverless_Stream_Data_Pipeline/assets/116425101/5e72ef32-50aa-47fc-9c46-1679d0beb88a)



  - I have written the python code, the file is available in this repo. File name is myLambdaDataProducer.py
  - Once the code deployment is completed go to 'configuration' and find 'permission' tab on left side. edit the role and attach Kinesis Role. So that Lambda can have access to Kinesis.
  - Now go back to Code tab and now we can Test run our code. please note down the name you provide for the Kinesis Datastream, the same name we need to use when we create Kinesis Data stream.
     
  
</details>
<details>
  <summary>Setting up Kinesis Data Stream</summary>
  
  Following are the steps we need to follow   
  - Search the 'Kinesis' in the navigation search bar.
  - click on 'Create data stream'.
  - provide the data stream name, the same name we have used in the previous step of Lambda code.
  - choose the Data stream capacity 'Provisioned' because we have limited data to process and keep 'Provisioned shards' = 2.
    ![image](https://github.com/yantrik-patel/AWS_Serverless_Stream_Data_Pipeline/assets/116425101/d3157283-27af-4ebb-95ff-498a8dae4c80)

  - click on 'Create data stream'.
  
</details>


<details>
  <summary>Setting up Amazon Data Firehose</summary>
 
  Following are the steps we need to follow   
  - Go back to main screen of Kinesis service and this time choose Amazon Data Firehose and click 'Create Firehose stream'
    
    ![image](https://github.com/yantrik-patel/AWS_Serverless_Stream_Data_Pipeline/assets/116425101/748a0c5c-9821-45d2-94e6-e6a5189fe501)

  - select source as Amazon Kinesis Data Streams.
  - select destination as S3.
  - in source setting we can browse and select the Kinesis Data Stream that we created in previous step.
  - Firehose stream name can be kept as it is or can be customised.
  - we can transform the records but in this project we are not doing so.
  - in Destination Setting, we need to select the bucket where we want to store the final output.
  - click on 'Create firehose stream'

 
</details>

   
After setting these services, we can now run our Lambda which will produce the records, this records are fetched into datastream in realtime and sent to firehose. Firehose is not real time but is almost realtime, means it will process the data and writes it into S3(in our case) within a minute or so.

<details>
  <summary>Further scope of improvement</summary>
  Further we can try using 'Transform' functionality of Firehose.   
  Also instead of storing data into S3 we can directly point Firehose to ingest data in to datawarehouse like Redshift.
</details>
