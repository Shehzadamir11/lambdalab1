# Pollinate Assignement
## CICD Creation with API and Database Integration
The project is build using serverless AWS Services.Which are mentioned below
-Code Build
-Serverless API gateway
-Lambda Function
-Dynamo DB
-Cloud formation
-Github Integration with CodeBuild


## Manual to run the project
1:Create the Infrastucture via AWS Cloud Formation template (template.yml file)
2:Create Github repository 
3:Link the Github with Code build and use buildspec.yml file for phases, you can use ubnutu standarad build availble in the configuration
4:Apply the following policiy to you Build project IAM role for interacting with the Lambda function
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
###
