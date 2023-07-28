<div align="center">

<h1>Template | Worker</h1>

[![CI | Test Worker](https://github.com/runpod-workers/worker-template/actions/workflows/CI-test_worker.yml/badge.svg)](https://github.com/runpod-workers/worker-template/actions/workflows/CI-test_worker.yml)
&nbsp;
[![CD | Dev Docker Image](https://github.com/runpod-workers/mock-worker/actions/workflows/CD-docker_dev.yml/badge.svg)](https://github.com/runpod-workers/mock-worker/actions/workflows/CD-docker_dev.yml)

🚀 | A simple worker that can be used as a starting point to build your own custom RunPod Endpoint API worker.
</div>

## Usage

```json
{"input":
    {
        "mock_return": "Anything here will be returned as the output of the worker.",
        "mock_delay": 0, // The number of seconds to wait before returning output, raising error or crashing.
        "mock_error": false, // If true, the worker will raise an error.
        "mock_crash": false // If true, the worker will crash (kills the processes)
    }
}
```
