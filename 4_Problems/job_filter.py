# cell magic command to write the contents of this cell to a file called job_filter.py
# Problem Statement:
# Create a module named job_filter with a function filter_by_location that takes a list of job postings and a location and returns a list of job postings in that location. 
# Import this module and use the function to filter job postings in 'New York'. Use the variable of job_postings shown below.
def filter_by_location(job_postings,location):
    return list(i for i in job_postings if location in i['location'])
def filter_by_location2(job_postings,location):
    contain=lambda x: location in x['location']
    return list(filter(contain,job_postings))
