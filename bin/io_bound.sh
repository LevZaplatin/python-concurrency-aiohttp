pip install aiohttp requests

echo io_bound_test_with_threading
python3 /tmp/tests/io_bound_test_with_threading.py

echo io_bound_test_with_multiprocessing
python3 /tmp/tests/io_bound_test_with_multiprocessing.py

echo io_bound_test_with_async
python3 /tmp/tests/io_bound_test_with_async.py