# Django Celery: Enhancing Django with Asynchronous Task Processing

## Overview
Celery is an open-source asynchronous task queue or job queue based on distributed message passing. While it supports scheduling, its primary focus is on real-time operations. Celery provides a simple, flexible, and reliable system for processing vast amounts of messages, equipping operations with the necessary tools to effectively manage such a distributed system.

## Use Case
Celery serves as a distributed task queue system seamlessly integrated with Django, enabling the execution of asynchronous tasks. These tasks may include sending emails, processing background jobs, and more. This guide, dated September 28, 2023, will walk you through the steps to integrate and use Celery with a Django project.

## Key Features
- **Flexibility:** Written in Python, Celery is versatile and can be implemented in any programming language.
- **Scalability:** Capable of running on a single machine, multi-machine, or across a data center.

## Celery in Django
Celery, as a task queue/job queue, excels in distributed message passing. While it emphasizes real-time operations, it also supports scheduling. Tasks, the execution units in Celery, run concurrently on single or multiple worker servers.

## Implementation Steps
1. **Virtual Environment Setup:**
    ```bash
    virtualenv venv
    ```

2. **Installation:**
    ```bash
    pip install django
    pip install celery
    pip install redis  # Used as a broker
    ```

3. **Project Creation:**
    - Create a Django project and app.

4. **Celery Configuration:**
    - Create `celery.py` in the project-level folder.
    - Configure Celery in `settings.py`.

5. **Task Creation:**
    - Inside the app, create a task file for defining tasks.

6. **Task Triggering:**
    - Utilize Celery tasks in views or wherever necessary.

7. **Start Celery Worker:**
    - Begin the Celery worker to execute the tasks.

This setup allows Django to leverage Celery's capabilities for handling asynchronous tasks efficiently.

---

# Celery API: A Quick Reference

The Celery API defines a standardized set of execution options and offers three primary methods:

1. **`apply_async(args[, kwargs[, …]])`:**
    - Sends a task message.
  
2. **`delay(*args, **kwargs)`:**
    - A shortcut to send a task message. However, it does not support execution options.
  
3. **`calling (__call__)`:**
    - Applying an object supporting the calling API (e.g., `add(2, 2)`) implies that the task will not be executed by a worker but in the current process instead. In this case, a message won't be sent.

## Quick Cheat Sheet
- **`T.delay(arg, kwarg=value)`:**
    - Star arguments shortcut to `.apply_async`. (`T.delay(*args, **kwargs)` calls `.apply_async(args, kwargs)`).

- **`T.apply_async((arg,), {'kwarg': value})`:**
    - `T.apply_async(countdown=10)`: Executes in 10 seconds from now.

- **`T.apply_async(eta=now + timedelta(seconds=10))`:**
    - Executes in 10 seconds from now, specified using `eta`.

- **`T.apply_async(countdown=60, expires=120)`:**
    - Executes in one minute from now but expires after 2 minutes.

- **`T.apply_async(expires=now + timedelta(days=2))`:**
    - Expires in 2 days, set using `datetime`.

- **`T.apply_async((arg,), {'kwarg': value}, countdown=60, expires=120)`:**
    - Args: List of positional arguments to pass to the function.
    - kwargs: A dictionary of keyword arguments to pass to the function.
    - countdown: The number of seconds to delay the task from the current task.
    - expires: The maximum time until the task is considered expired and not executed if not started.

**`delay()`:**
   - This is a shorthand for `apply_async()` with default options, making it more convenient to enqueue a task.

**`T.delay(args1, args2, keyword_arg='value')`:**
   - Used as simple function arguments.

---

# AsyncResult Object in Celery: Managing Asynchronous Task Results

The `AsyncResult` object in Celery represents the result of an asynchronous task that has been enqueued for execution. When you enqueue a task in Celery, it returns an `AsyncResult`, allowing you to effectively manage the task and retrieve its result once it's completed. This object comes with various methods and attributes for interacting with the task.

## Attributes
- **`result`:** The result of the task.
- **`status`:** The status of the task execution.
- **`state`:** The current state of the task.
- **`task_id`:** The unique identifier assigned to the task.
- **`id`:** The identifier of the `AsyncResult` object.
- **`expires`:** The expiration time of the task result.

## Methods
- **`ready()`:** Checks if the task has been completed and the result is ready for retrieval.
- **`successful()`:** Checks if the task has been executed successfully.
- **`failed()`:** Checks if the task has failed during execution.
- **`get()`:** Retrieves the result of the task.

To store task results in the backend, you can use the `django-celery-results` package. Install it using the following command:
```bash
pip install django-celery-results
```
Configure your Celery settings to use Django as the result backend:
```bash
CELERY_RESULT_BACKEND = 'django-db'
```
# Useful Commands

Install required packages:
```bash
pip install django
pip install celery
pip install redis
```
Start Celery worker:
```bash
celery -A proj worker -l info
```

Display Celery help:
```bash
celery help
```

Start Celery beat (for periodic tasks):
```bash
    celery -A proj beat -l info
```
