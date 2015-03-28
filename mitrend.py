#!/usr/bin/python

import json
import requests

class Mitrend:
	def __init__(self, username=None, password=None, company=None, assessment_name=None, 
		city=None, country=None, state=None, timezone=None, tags=[], attributes={}, device_type=None, files=[] ):
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
                        r = requests.post(url=url, headers=headers, 
				data=json.dumps(file_data),
				auth=(self.username, self.password) )
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
	try:
		# Add files during object instantiation if already known
		M = Mitrend(username='', password='', 
			company='',
			assessment_name='', 
			city='',
			country='', 
			state='',
			timezone='',
			tags=['', ''], 
			attributes={'source':'mitrend-python'},
			device_type='',
			files=[] )

		# Post a create assessment request
		M.create()

		# Post any new files
		M.add(files=[])

		# Submit for final assessment
		M.submit()

        except Exception as e:
		print e
		raise
