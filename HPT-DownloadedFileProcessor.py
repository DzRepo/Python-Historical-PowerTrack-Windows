#!/usr/bin/env python
from __future__ import print_function
import sys
import json
import gzip
import glob

# Convert these to settings file / command line args

ActivityCallBack = None
Activities_Processed = 0
output_file = None


def set_callback(callback):
    global ActivityCallBack
    ActivityCallBack = callback


def handle_error(error):
    print("HistoricalPowerTrack.py - line: " + str(sys.exc_info()[-1].tb_lineno) + str(error))


def decompress_file(filename):
    with gzip.open(filename, 'rb') as f:
        file_content = f.read()
        return file_content


def process_activity(activity):
    try:
        if 'id' in activity:
            #    newActivity = {}
            #    newActivity["postedTime"] = activity["postedTime"]
            #    newActivity["id"] = activity["id"]
            # Actor ID
            #    print (activity["actor"]["id"][15:])
            # Tweet ID
            #    print (activity["id"][28:])
            # print(json.dumps(newActivity))
            if output_file is not None:
                output_file.write(json.dumps(activity))
#        else:
#            print ("non-activity: ", activity)
    except Exception as e:
        handle_error(e)
        sys.exit(2)


def get_files():
    global output_file
    try:
        filecount = 0
        url_list = glob.glob('*.gz')
        job_name = url_list[0][0:10] + '-combined.txt'
        print ("Creating " + job_name)
        output_file = open(job_name, 'wb')
        for url in url_list:
            print("*** Processing: ", url)
            filecount += 1
            file_text = decompress_file(url)
            lines = file_text.splitlines()
            for line in lines:
                # skip blank lines
                if len(line) > 1:
                    try:
                        activity = json.loads(line)
                        process_activity(activity)
                    except Exception as e:
                        handle_error(e)
    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    get_files()
