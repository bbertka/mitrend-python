#!/usr/bin/python

import json
import requests

class Mitrend:
    def __init__(self, username=None, password=None, company=None, assessment_name=None, city=None, country=None, state=None, timezone=None, tags=[], attributes={}, device_type=None, files=[] ):
        """ Creates the initial MiTrend object """
        self.username = username
        self.password = password
        self.company = company
        self.assessment_name = assessment_name
        self.city = city
        self.state = state
        self.country = country
        self.timezone = timezone
        self.tags = tags
        self.attributes = attributes
        self.device_type = device_type
        self.files = files
        self.job_id = None
        self.submission = {}

    def create(self):
        """ Creates the initial submission """
        data = { 'company': self.company,
            'assessment_name': self.assessment_name,
            'city': self.city,
            'country': self.country,
            'state': self.state,
            'timezone': self.timezone,
            'attributes':self.attributes,
            'tags': self.tags }
        url = 'https://app.mitrend.com/api/assessments'
        headers = {'Content-Type': 'application/json'}
        r = requests.post( url='https://app.mitrend.com/api/assessments',
            headers=headers, data=json.dumps(data),
            auth=(self.username, self.password) )
        self.job_id = json.loads(r.content)['id']
        return True

    def add(self, files=[]):
        """ Loop through the files and add to the job """
        headers = {'Content-Type': 'application/json'}
        self.files.extend(files)
        for furl in self.files:
            file_data = {'device_type': self.device_type, 'ftp_url':furl}
            url = "https://app.mitrend.com/api/assessments/%s/files" % self.job_id
            r = requests.post(url=url, headers=headers, data=json.dumps(file_data), auth=(self.username, self.password) )
        return True

    def submit(self):
        """ Submits the job with job_id """
        if not self.job_id:
            return None
        url = "https://app.mitrend.com/api/assessments/%s/submit" % self.job_id
        r = requests.post(url=url, auth=(self.username, self.password) )
        self.submission = json.loads(r.content)
        return True

if __name__=="__main__":
    """ Creates a new MiTrend submission """
    import argparse
    parser = argparse.ArgumentParser(description="command line interface to  MiTrend performance analysis tool that submits assessments on behalf of an authenticated user")
    # required arguments
    parser.add_argument("username", help="your Mitrend userid (email)")
    parser.add_argument("password", help="your Mitrend password")
    parser.add_argument("customername", help="the name of the customer for this assessment")

    # optional arguments
    parser.add_argument("-a", "--assessmentname", help="name for your assessment (in quotes)")
    parser.add_argument("-c", "--city", help="customer city")
    #parser.add_argument("-co", "--country", help="customer country")
    #parser.add_argument("-s", "--state", help="customer state or territory")
    #parser.add_argument("-t", "--timezone", help="customer time zone")
    parser.add_argument("-d", "--devicetype", help="type of assessment")
    #parser.add_argument("-g", "--tags", help="comma separated list of tags for this assessment")
    #parser.add_argument("-a", "--attributes", help="list of attributes in the form of "key:value")
    parser.add_argument("-f", "--file", help="ftp url or zip file name")

    args = parser.parse_args()

    try:
        # Add files during object instantiation if already known
        # not adding country, state, or timezone as these require specific codes
        # not adding tags either as yet... they're harder on the CLI
        # known device_types are "EMC_Symmetrix" and "EMC_Grabs"
        M = Mitrend(username=args.username, password=args.password,
            company=args.customername if args.customername else '',
            assessment_name=args.assessmentname if args.assessmentname else '',
            city=args.city if args.city else '',
            device_type=args.devicetype if args.devicetype else '',
            attributes={'source':'mitrend-python'},
            files=[args.file] if args.file else [] )

           # country='',
           # state='',
           # timezone='',
           # tags=['', ''],

        # Post a create assessment request
        M.create()

        # Post any new files
        M.add(files=[])

        # Submit for final assessment
        M.submit()

    except Exception as e:
        print e
    raise


