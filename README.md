# Python script for working with [Gnip](www.gnip.com) Historical PowerTrack 2.0 API under Windows
See:  the Support web site section on [Historical PowerTrack 2.0](http://support.gnip.com/apis/historical_api2.0/)  for more information.
###Note: Requires [Requests](http://docs.python-requests.org/en/master/) library - to install: 
`pip install requests`

Notes: 

- Due to limitations under Windows, this is a single-threaded version of the HPT.py client.  Downloads of jobs will take a bit longer, as each file is downloaded one at at time, but otherwise, the client is identical to the other version.
- For the destination directory, remember to use a terminating slash mark (like:  C:\download\files\ )

##HPT.py
Sample application to make calls into API and command line interface
Execute ./HPT.py to get show usage help:

```
Usage:
./HPT.py ACTION [ parameters ]
./HPT.py set-account-name ACCOUNT-NAME
./HPT.py set-username USERNAME
./HPT.py set-password PASSWORD
./HPT.py set-download-location DIRECTORY
./HPT.py create-job FILENAME.JSON
./HPT.py get-jobs [JOB_TYPE_FILTER(s) - (O)pened, (E)stimating, (Q)uoted, (A)ccepted, (R)ejected, r(U)nning, (C)ompleted, (D)elivered, (F)ailed]
./HPT.py get-job-status JOB-ID
./HPT.py accept-job JOB-ID
./HPT.py reject-job JOB-ID
./HPT.py get-job-results JOB-ID [no-files] (removes urlList from results)
./HPT.py download-job JOB-ID [start-file-number] (optional # to resume stalled jobs)
./HPT.py download-from-results RESULTS.JSON [start-file-number] (optional # to resume stalled jobs)
./HPT.py validate-job JOB-ID    (confirms all files downloaded correctly and generates summary files)
```

##ConfigFile.py
Library used to manage reading/writing to gnip.cfg file where credentials and settings are stored.

##ice_cream.json
Sample job creation JSON file.  Usage would be:

`./HPT.py create-job ice_cream.json`

---
###Feedback
Please send help requests / comments / complaints / chocolate to [@SteveDz](stevedz@twitter.com)

Note that this code is provide "As Is".  You should review and understand Python code, and be able to debug this code _on your own_ if used in a production environment.  See the License file for more legal limitations.
