<div align="center">

<h1>Template | Worker</h1>

[![CI | Test Worker](https://github.com/runpod-workers/mock-worker/actions/workflows/CI-test_worker.yml/badge.svg)](https://github.com/runpod-workers/mock-worker/actions/workflows/CI-test_worker.yml)
&nbsp;
[![CD | Dev Docker Image](https://github.com/runpod-workers/mock-worker/actions/workflows/CD-docker_dev.yml/badge.svg)](https://github.com/runpod-workers/mock-worker/actions/workflows/CD-docker_dev.yml)

🚀 | A simple worker that can be used as a starting point to build your own custom RunPod Endpoint API worker. [Docker Link](https://hub.docker.com/r/runpod/mock-worker)
</div>



## Usage

```json
{"input":
    {
        "mock_return": "Anything here will be returned as the output of the worker.",
        "mock_delay": 0, // The number of seconds to wait before returning output, raising error or crashing.
        "mock_progress": {
            "updates": [],  // A list of progress updates to send back to the RunPod API.
            "wait_time": 0 // The number of seconds to wait before sending a progress update.
        },
        "mock_error": false, // If true, the worker will raise an error.
        "mock_crash": false, // If true, the worker will crash (kills the processes)
        "mock_refresh": false, // If true, the refresh_worker flag is enabled.

        "mock_external": {
            "error_job_return": false, // If true, the job will fail to return the job results.
        }

    }
}
```

### Generator Handler

To test the generator handler override the docker command with the following:

```bash
python3 -u /handler.py --generator
```

To test multiple yeild outputs, set the `mock_return` to a list of values.

```json
{"input":
    {
        "mock_return": ["value1", "value2", "value3"],
        "mock_delay": 0,
        "mock_error": false,
        "mock_crash": false
    }
}
```
