'''
IMPORTANT: This file is only used for testing purposes.
'''

import os
import sys
import time
import argparse


import runpod
from runpod.serverless.modules import rp_http


# ----------------------------- Standard Handler ----------------------------- #
def handler(job):
    '''
    The handler function that will be called by the serverless.
    '''
    job_input = _side_effects(job['input'])

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


# ----------------------------- Generator handler ---------------------------- #
def generator_handler(job):
    '''
    Generator type handler.
    '''
    job_input = _side_effects(job['input'])

    # Prepare the job output
    job_output = job_input.get('mock_return', ['Hello World!'])

    for output in job_output:
        yield output


async def async_generator_handler(job):
    '''
    Async generator type handler.
    '''
    job_input = _side_effects(job['input'])

    # Prepare the job output
    job_output = job_input.get('mock_return', ['Hello World!'])

    for output in job_output:
        yield output


# ------------------------------- Side Effects ------------------------------- #
def _side_effects(job_input):
    '''
    Modify the behavior of the handler based on the job input.
    '''
    # Mock the duration of the job
    time.sleep(job_input.get('mock_delay', 0))

    # Mock the job crashing the worker
    if job_input.get('mock_crash', False):
        os._exit(1)

    # Mock the job throwing an exception
    if job_input.get('mock_error', False):
        raise Exception('Mock error')  # pylint: disable=broad-exception-raised

    if job_input.get('mock_fail_job_done', False):
        rp_http.JOB_DONE_URL = 'http://not_found'

    return job_input


# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #
if __name__ == '__main__':
    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--generator', action='store_true', default=False,
                        help='Starts serverless with the generator_handler')
    parser.add_argument('--async_generator', action='store_true', default=False,
                        help='Starts serverless with the async_generator_handler')
    parser.add_argument('--return_aggregate_stream', action='store_true', default=False,
                        help='Aggregate the stream of generator_handler and return it as a list')

    # Pass the unknown arguments to the serverless
    args, unknown = parser.parse_known_args()
    sys.argv = [sys.argv[0]] + unknown

    # Start the serverless worker
    if args.generator:
        print('Starting serverless with generator_handler')
        print(f"return_aggregate_stream: {args.return_aggregate_stream}")

        runpod.serverless.start({
            "handler": generator_handler,
            "return_aggregate_stream": args.return_aggregate_stream
        })

    elif args.async_generator:
        print('Starting serverless with async_generator_handler')
        print(f"return_aggregate_stream: {args.return_aggregate_stream}")

        runpod.serverless.start({
            "handler": async_generator_handler,
            "return_aggregate_stream": args.return_aggregate_stream
        })

    else:
        runpod.serverless.start({"handler": handler})
