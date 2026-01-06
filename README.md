# python-devops-automation
DevOps Python automation reduces manual infrastructure work by 70%+.  CI/CD pipelines, AWS cloud integration, Kubernetes orchestration,  backup automation, log parsing. Production-ready scripts for modern  cloud platforms. Infrastructure automation made easy.  

## 1. cloud_log_parser.py  

A small, practical script that shows how to parse a cloud style JSON log, extract users, and replace placeholder values. The example is self contained so it runs without AWS credentials and is easy to adapt for real automation.  

### What it does  
- Loads a mock JSON log string into a Python dictionary.  
- Splits a comma separated user string into a list of users.  
- Replaces placeholder resource names with real values.  
- Prints the parsed users and the updated resources.  

### Why this is useful  
- Demonstrates common DevOps tasks such as log parsing and config updates.  
- Easy to extend to real data sources like AWS CloudTrail or boto3 responses.  

### Quick usage  
Save the script as cloud_log_parser.py and run with python 

### Output:The script prints the users list and the updated resources dictionary.  

### Notes and tips
- The script uses only the standard json module so there are no external dependencies.  
- For production use, replace the mock JSON with data from AWS CLI or boto3.  
- If you need to handle flexible spacing or complex patterns, consider using regular expressions.  
- Keep secrets out of source files. Use environment variables or a secrets manager for credentials.


## 2.log_error_filter_regex.py

Production-ready DevOps log parser that automates error detection and extraction from multi-line application logs using compiled regex patterns. Designed for real-time monitoring, CI/CD pipelines, and infrastructure alerting systems.  

### Problem Solved  
Manual log scanning is slow, error-prone, and unscalable. This script automates ERROR-level message extraction, enabling:  
- Instant error detection: No manual grepping required   
- Zero false positives: Word-boundary matching ensures accuracy  
- Real-time integration: Pipe into alerting systems (Slack, PagerDuty, monitoring platforms)   
- Production-grade reliability: Optimized regex performance, type hints, PEP 257 standard

### Key Features  
- Compiled regex patterns for optimized performance on large log volumes  
- Word-boundary matching (\bERROR\b) avoids false positives  
- Modular design for integration into monitoring pipelines

### How It Works

| Step | Description |
|------|-------------|
| **1. Load logs** | Read multi-line log text from file or pipeline |
| **2. Compile pattern** | Pre-compile `\bERROR\b` regex for performance |
| **3. Process lines** | Iterate through each log line efficiently |
| **4. Extract matches** | Return only ERROR-level entries |

### Example

**Input:** Multi-line log with INFO, WARNING, ERROR messages  
**Output:** Only ERROR-level lines extracted for alerting/analysis

### Use Cases & Benefits

| Scenario | Benefit |
|----------|---------|
| **Production monitoring** | Detect database failures, pod crashes, connection timeouts instantly |
| **Deployment automation** | Fail build if ERROR detected in deployment logs |
| **Log aggregation** | Filter ELK/Splunk/CloudWatch logs for critical events |
| **Incident response** | Rapid error extraction enables faster MTTR (Mean Time To Resolution) |
| **Compliance** | Automated error tracking for audit logs and security events |

## How It Helps DevOps Automation

### Real-Time Error Detection
```bash
python log_error_filter_regex.py < /var/log/app.log | while read error; do
    send_slack_alert "$error"
done
```
**Note** : Currently we have hardcoded the log text. In case we want to use input redirection , the following addition needs to be done inorder to use the log file as input

```
import sys

if __name__ == "__main__":
    LOG_DATA = sys.stdin.read()  # Read from stdin instead of hardcoded string
    
    for line in find_error_lines(LOG_DATA):
        print(line)
```


### CI/CD Pipeline Integration (Jenkins/GitLab)
```groovy
stage('Parse Logs') {
    steps {
        sh 'python log_error_filter_regex.py < deployment.log > errors.txt'
        sh 'if [ -s errors.txt ]; then exit 1; fi'  // Fail build on errors
    }
}
```







