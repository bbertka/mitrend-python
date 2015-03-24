mitrend-python
======================
This is a python module for the [MiTrend](http://mitrend.com) performance analysis tool that submits assessments on behalf of an authenticated user.  It exposes the REST API made publicly available by [MiTrend](http://mitrend.com/).

## Description
Currently only a standard web interface is provided by [MiTrend](http://mitrend.com), and an API that takes well formed JSON requests. The problem with the API is that it requires multiple steps to submit a request. Specifically using the REST API, a program would have to send a request to create an assessment, then send a subsequent request to add files. Finally, a program would have to send a request to submit the assessment for analysis. The problem is that for Python code, having to submit multiple REST API requests without a library is cumbersome. This module wrapps the JSON API in an easy to use pyton module. The following use cases are supported by this module.
- Automation is desired and a Python tool chain is required, hence this module makes it easy to include [MiTrend](http://mitrend.com) functionality.
- A microservice is being prepared to handle [MiTrend](http://mitrend.com) assessment requests, so this module can easily fit in with a Web app such as Flask.

## Installation
To install just clone from git and run the setup.py script:
```
sudo python setup.py install
```
Note that python requests is required for this module to function:
```
sudo pip install requests
```

## Usage Instructions
The module provides a main method that can be used for testing and illustrated how the module should be used:
```
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
	files=[''] )

	M.create_submission()
	M.add_files()
	M.submit()
```
Please refer to the official [MiTrend API](http://mitrend.com/#api) specification for what's possible in these fields.

## Contribution
Create a fork of the project into your own reposity. Make all your necessary changes and create a pull request with a description on what was added or removed and details explaining the changes in lines of code. If approved, project owners will merge it.

Licensing
---------
Licensed under the Apache License, Version 2.0 (the “License”); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Support
-------
Please file bugs and issues at the Github issues page. For more general discussions you can contact the EMC Code team at <a href="https://groups.google.com/forum/#!forum/emccode-users">Google Groups</a> or tagged with **EMC** on <a href="https://stackoverflow.com">Stackoverflow.com</a>. The code and documentation are released with no warranties or SLAs and are intended to be supported through a community driven process.
