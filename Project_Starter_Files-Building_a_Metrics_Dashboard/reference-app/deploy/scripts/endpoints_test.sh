#!/bin/bash

echo "Test Backend"
kubectl port-forward -n observability svc/backend --address 0.0.0.0 30010:8080 &
for i in {1..20}
do
    curl -s localhost:30010 > /dev/null
    curl -s localhost:30010/404 > /dev/null
done
kill %1
echo "Done Testing Backend"
