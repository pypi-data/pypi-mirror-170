# Async SQS consumer

This is a simple asynchronous worker for consuming messages from AWS SQS

### Usage
```python
from async_sqs_consumer.worker import (
    Worker,
)

worker = Worker(
    queue_url="https://sqs.us-east-1.amazonaws.com/xxxxxxx/queue_name"
)


@worker.task("report")
async def report(text: str) -> None:
    print(text)

worker.start()

```
