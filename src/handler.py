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

    time.sleep(job_input.get('mock_delay', 0))

    if job_input.get('mock_error', False):
        raise Exception('Mock error')

    if job_input.get('mock_crash', False):
        os._exit(1)

    return job_input.get('mock_return', 'Hello World!')


runpod.serverless.start({"handler": handler})
