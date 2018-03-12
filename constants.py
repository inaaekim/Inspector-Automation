RULE_MAP = {
    # Oregon
    "us-west-2": {
        "CVE": "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p",
        "CIS": "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-H5hpSawc",
        "Best Practices": "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ",
        "Behavior Analysis": "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-vg5GGHSD"
    },
    # N.Virginia
    "us-east-1": {
        "CVE": "arn:aws:inspector:us-east-1:316112463485:rulespackage/0-gEjTy7T7",
        "CIS": "arn:aws:inspector:us-east-1:316112463485:rulespackage/0-rExsr2X8",
        "Best Practices": "arn:aws:inspector:us-east-1:316112463485:rulespackage/0-R01qwB5Q",
        "Behavior Analysis": "arn:aws:inspector:us-east-1:316112463485:rulespackage/0-gBONHN9h"
    },
    # add your region here
    # check https://docs.aws.amazon.com/inspector/latest/userguide/inspector_rules-arns.html
}

TOPICARN = "arn:aws:sns:{region}:{yourccount}:{topicname}"
