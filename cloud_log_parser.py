import json

#  AWS CloudTrail log (simplified JSON string)
log_json = '''
{
    "eventTime": "2026-01-04T12:00:00Z",
    "eventName": "CreateUser",
    "userIdentity": {
        "userName": "anita,rohan,rakesh,"
    },
    "resources": [
        {"resourceType": "AWS::EC2::Instance", "resourceName": "i-1234567890abcdef0"},
        {"resourceType": "AWS::S3::Bucket", "resourceName": "my-bucket"}
    ]
}
'''

#  Converting JSON string into dictionary
log_dict = json.loads(log_json)

#  Extracting usernames string and split into list
users_string = log_dict["userIdentity"]["userName"]
users_list = users_string.split(",")   # split by comma

# Step 3: Replace placeholder bucket name if needed
for resource in log_dict["resources"]:
    if resource["resourceType"] == "AWS::S3::Bucket":
        resource["resourceName"] = resource["resourceName"].replace("my-bucket", "prod-bucket")

# Print results
print("Users List:", users_list)
print("Updated Resources:", log_dict["resources"])
