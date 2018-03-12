import sys
import argparse
from inspector import InspectorEngine
from constants import TOPICARN


def banner():
    tag = ("""
         _____                          _  
        |_   _|                        | |            
          | | _ __  ___ _ __   ___  ___| |_ ___  _ __ 
          | || '_ \/ __| '_ \ / _ \/ __| __/ _ \| '__|
         _| || | | \__ \ |_) |  __/ (__| || (_) | |   
         \___/_| |_|___/ .__/ \___|\___|\__\___/|_|   
                       | |                            
                       |_|         
               _____            _                     
              |  ___|          (_)                    
              | |__ _ __   __ _ _ _ __   ___          
              |  __| '_ \ / _` | | '_ \ / _ \         
              | |__| | | | (_| | | | | |  __/         
              \____/_| |_|\__, |_|_| |_|\___|         
                           __/ |                      
                          |___/                       
        """)
    print(tag)


def createtag_template(engine, instanceids, tagvalue, tagkey, region, duration):
    print ("instanceids:{}\ttagvalue:{}\ttagkey:{}\tregion:{}\tduration:{}\t".format(instanceids, tagvalue, tagkey, region, duration))
    engine.create_awsscan_tag(instanceids, tagvalue, tagkey)
    targetarn = engine.create_assessment_target(tagvalue, tagvalue)
    rulepackagearns = engine.get_rulepackagearns(region)
    templatearn = engine.create_assessment_template(targetarn, tagvalue, rulepackagearns, duration)
    if TOPICARN:
        engine.subscribe_to_event(templatearn, TOPICARN)
        print("subscribe_to_event:{}".format(TOPICARN))
    return templatearn

def start_assessment(self, engine, templatearn):
    assessmentrunarn = engine.start_assessment_run(templatearn)
    print ("start_assessment_run:{}".format(assessmentrunarn))
    return assessmentrunarn

def execute(args):
    templatearn = None
    engine = InspectorEngine()
    if args.createtemplate:
        instanceids = args.instanceids.split()
        tagvalue = args.tagvalue
        tagkey = args.tagkey
        region = args.region
        duration = args.duration
        if not instanceids:
            print("[!] Missing instanceids")
            return
        if not tagvalue:
            print("[!] Missing tagvalue")
            return
        templatearn = createtag_template(engine, instanceids, tagvalue, tagkey, region, duration)
        print("templatearn is generated {}".format(templatearn))
    if args.existingtemplate:
        templatearn = args.templatearn
        if not templatearn:
            print("[!] Missing templatearn")
            return
    if args.report:
        instanceids = args.instanceids.split()
        severities = args.severities.split()
        assessmentrunarns = args.runarns.split()
        reportfile = args.reportfile
        if not instanceids:
            print("[!] Missing instanceids")
            return
        if not assessmentrunarns:
            print("[!] Missing assessmentrunarns")
            return
        if not reportfile:
            print("[!] Missing reportfile name")
            return
        engine.genearte_report(instanceids, severities, assessmentrunarns, reportfile)
    else:
        print(templatearn)
        assessmentrunarn = engine.start_assessment_run(templatearn)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Usage of InspectorEngine")

    # create a template with tags
    parser.add_argument("-c", "--createtemplate", action="store_true", help="Create a tag and a template", default=False)
    parser.add_argument("-i", "--instanceids",
                        help="EC2 instance Ids e.g 'i-0c6c57d1e60e19320 i-0c6c57d1e60e19322 i-0c6c57d1e60e19323", required=False)
    parser.add_argument("-k", "--tagkey", help="Tag key e.g 'awsscan'", default="awsscan")
    parser.add_argument("-v", "--tagvalue", help="Tag value e.g 'prod'", required=False)
    parser.add_argument("-r", "--region", help="Region e.g. 'us-east-1'", default="us-east-1")
    parser.add_argument("-d", "--duration", help="Duration seconds e.g. 600", type=int, default=3600)
    # start run
    parser.add_argument("-e", "--existingtemplate", action="store_true",
                        help="Start assessment run with existing template", default=False, required=False)
    parser.add_argument("-t", "--templatearn",
                        help="templatearn e.g 'arn:aws:inspector:us-east-1:844647875270:target/0-qGFYiMXR/template/0-FukqLaxf/run/0-05kdV7pg'", required=False)
    # generate report
    parser.add_argument(
        "-R", '--report', action="store_true", help="Genearte a report, Must add -i(instanceids), -a(runarns), -f(reportfile)", default=False)
    parser.add_argument("-a", "--runarns", help="Assessment run", required=False)
    parser.add_argument("-s", "--severities", help="Low|Medium|High|Informational|Undefined", default="High")
    parser.add_argument("-f", "--reportfile", help="report file name", required=False)

    args = parser.parse_args()
    
    if len(sys.argv) < 2:
        banner()
        parser.print_help()
    else:
        execute(args)
