#!/bin/bash

mkdir -p .test
echo "${TEST_JSON}" > /test.json

exec "$@"
