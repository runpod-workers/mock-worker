'''
IMPORTANT: This file is only used for testing purposes.
'''

import os
import time

import runpod


def handler(job):
    '''
    The handler function that will be called by the serverless.
    '''
    job_input = job['input']

    # Mock the duration of the job
    time.sleep(job_input.get('mock_delay', 0))

    # Mock the job crashing the worker
    if job_input.get('mock_crash', False):
        os._exit(1)

    # Mock the job throwing an exception
    if job_input.get('mock_error', False):
        raise Exception('Mock error')

    # Prepare the job output
    job_output = job_input.get('mock_return', 'Hello World!')

    # Mock enabled refresh_worker
    if job_input.get('mock_refresh', False):
        job_output = {
            'refresh_worker': True,
            'mock_return': job_output
        }

    # Mock the job returning a value
    return job_output


runpod.serverless.start({"handler": handler})
