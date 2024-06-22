# prefect-serve-example

Example of using `prefect.serve` with Kubernetes.

## Getting Started

The example assumes you have a Kubernetes cluster running locally. Tested with Docker-Desktop provided Kubernetes.

```bash
docker build . -t serve-flows:latest

kubectl create secret generic prefect-api-key --from-literal=key=<YOUR-API-KEY>
kubectl create secret generic prefect-api-url --from-literal=key=https://api.prefect.cloud/api/accounts/<ACCOUNT-ID>/workspaces/<WORKSPACE-ID>

kubectl apply -f deployment.yaml

python submit.py 10
```
