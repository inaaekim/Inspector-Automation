# AWS Inspector Assessment Automation

InspectorEngine will automaticlly set up Amazon Inspector assessment against EC2 instances and generate a customized finding report.

## Getting Started

It will use Boto3 (Amazon Web Service SDK for Python) to make use of Amazon Service like EC2, Inspector and so on.

It will use CIRCL CVE Search Open source to get public known information from security vulnerabilities in software and hardware along with their corresponding explosures. [CIRCL](https://www.circl.lu/services/cve-search/).

Report will be generated as JSON format.

### Prerequisites

You need to install Inspector Agents on your target EC2 instances. [Agent](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_installing-uninstalling-agents.html)

You have a SNS Topic to send messsages and subscribe to notifications if you want to receive Inspector assessment events.

### Installing

Install packages according to requirements.txt

```
pip install -r requirements.txt
```


### Configuration

Before you can begin using Boto3, you should setup authentication credentials.

If you have the [AWS CLI](https://aws.amazon.com/cli/) installed, then you can use it to configure your credentials are

```
aws configure
```

Alternatively, you can create the credential file yourself. By default, its location is at ~/.aws/credentials:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

You may also want to set a default region. This can be done in the configuration file. By default, its location is at ~/.aws/config:

```
[default]
region=us-east-1
```

### Update constants.py configuration

RULE_MAP: each region in AWS has different rule package arn.

Find rulepackagearns in your region [here](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_rules-arns.html) and update RULE_MAP.

TOPICARN: replace with your TOPIC ARN


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Create a new tag and a new template and run it

```
python main.py -c -i "i-0c6c57d1e60e12345" -k "awsscan" -v "autotest" -r "us-east-1" -d 600
```

Run a scan with existing template

```
python main.py -e "arn:aws:inspector:us-east-1:123456789012:target/0-psUXm9GN/template/0-ZoyR7tVn" 
```

Genearte a report

```
python main.py -R -a "arn:aws:inspector:us-east-1:123456789012:target/0-psUXm9GN/template/0-ZoyR7tXn" -s "High Medium" -i "i-0c6c57d1e60e19320" -f "i-0c6c57d1e60e19320_report.json"
```

### And coding style tests

Use pycodestyle

```
pycodestyle *.py
```

## Deployment


## Built With

* [Boto3](http://www.dropwizard.io/1.0.2/docs/)
* [CIRCL](https://www.circl.lu/services/cve-search/)

## Contributing


## Versioning
 

## Authors

* **Inaae Kim** - *Initial work* - [Inaae Kim](https://github.com/inaaekim)

## License


## Acknowledgments

* Improve UI
* Improve Report style
* Update assessment target
* and so on....

 


