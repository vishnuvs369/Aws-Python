# Using an Amazon S3 trigger to invoke a Lambda function

1) Create an Amazon S3 bucket and upload a test file to your new bucket. Your Lambda function retrieves   information about this file when you test the function from the console.

2) After creating the bucket, Amazon S3 opens the Buckets page,upload a test object using the Amazon S3 console

3) Create the Lambda function

     Choose Create function.

     On the Create function page, choose Use a blueprint.

     Under Blueprints, enter s3 in the search box.

     For a Python function, choose s3-get-object-python.

     Choose Configure.

     Under Basic information, do the following:

     For Function name, enter my-s3-function.

     For Execution role, choose Create a new role from AWS policy templates.
  
     For Role name, enter my-s3-function-role.

     Under S3 trigger, choose the S3 bucket that you created previously.

     Choose Create function.


 4) Review the function code

 The Lambda function retrieves the source S3 bucket name and the key name of the uploaded object from the event parameter that it receives. The function uses the Amazon S3 getObject API to retrieve the content type of the object.


5) Test in the console
      Invoke the Lambda function manually using sample Amazon S3 event data.

      To test the Lambda function using the console

      On the Code tab, under Code source, choose the arrow next to Test, and then choose Configure test events from the dropdown list.

      In the Configure test event window, do the following:

      Choose Create new test event.

      For Event template, choose Amazon S3 Put (s3-put).

      For Event name, enter a name for the test event. For example, mys3testevent.

      In the test event JSON, replace the S3 bucket name (example-bucket) and object key (test/key) with your bucket name and test file name.

      Choose Create.

      To invoke the function with your test event, under Code source, choose Test.

      The Execution results tab displays the response, function logs, and request ID


6) Test with the S3 trigger


      Invoke your function when you upload a file to the Amazon S3 source bucket.

      To test the Lambda function using the S3 trigger

      On the Buckets page of the Amazon S3 console, choose the name of the source bucket that you created earlier.

      On the Upload page, upload a few .jpg or .png image files to the bucket.

      Open the Functions page on the Lambda console.

      Choose the name of your function (my-s3-function).

      To verify that the function ran once for each file that you uploaded, choose the Monitor tab. This page shows graphs for the metrics that Lambda sends to CloudWatch. The count in the Invocations graph should match the number of files that you uploaded to the Amazon S3 bucket.


7) Clean up your resources
   
      You can now delete the resources that you created

