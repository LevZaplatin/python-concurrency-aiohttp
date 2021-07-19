
echo cpu_bound_test
{ time python3 /tmp/tests/cpu_bound_test.py; } 2>&1 | tr '\n' ' ' | sed -r 's/(real|user|sys)\s+0m//g' | sed -r 's/s /\t/g'
echo

echo cpu_bound_test_with_threading
{ time python3 /tmp/tests/cpu_bound_test_with_threading.py; } 2>&1 | tr '\n' ' ' | sed -r 's/(real|user|sys)\s+0m//g' | sed -r 's/s /\t/g'
echo

echo cpu_bound_test_with_multiprocessing
{ time python3 /tmp/tests/cpu_bound_test_with_multiprocessing.py; } 2>&1 | tr '\n' ' ' | sed -r 's/(real|user|sys)\s+0m//g' | sed -r 's/s /\t/g'
echo