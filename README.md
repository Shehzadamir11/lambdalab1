# Pollinate Assignement
## Solution Diagram
![Solution](design.jpg)
## CICD Creation with API and Database Integration
The project is build using serverless AWS Services.Which are mentioned below
1. Code Build
2. Serverless API gateway
3. Lambda Function
4. Dynamo DB
5. Cloud formation
6. Github Integration with CodeBuild


## Manual to run the project
1. Create the Infrastucture via AWS Cloud Formation template (template.yml file)
2. Create Github repository 
3. Link the Github with Code build and use buildspec.yml file for phases, you can use ubnutu standarad build availble in the configuration
4. Apply the following policiy to you Build project IAM role for interacting with the Lambda function
```javascript
{
    "Effect": "Allow",
    "Action": [
        "lambda:AddPermission",
        "lambda:RemovePermission",
        "lambda:CreateAlias",
        "lambda:UpdateAlias",
        "lambda:DeleteAlias",
        "lambda:UpdateFunctionCode",
        "lambda:UpdateFunctionConfiguration",
        "lambda:PutFunctionConcurrency",
        "lambda:DeleteFunctionConcurrency",
        "lambda:PublishVersion"
    ],
    "Resource": "arn:aws:lambda:us-east-1:your-aws-account-number:function:lambda-function1"
}
```

### Lambda Function Code is attached in the index.py
You can update it any way you want to server your purpose
### Use Requirement.txt for any external dependcies which you need to add to your project
You can update it any way you want to server your purpose
