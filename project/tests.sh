#!/bin/bash


cd "$(dirname "$0")"
# Run Python tests
echo "Running tests..."
python test_pipeline.py -v

# Store the exit code
TEST_EXIT_CODE=$?

# Exit with the same code as the Python tests
exit $TEST_EXIT_CODE 