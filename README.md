# digdag-server
Digdag server with Docker Compose

## Usage

```
digdag push helloworld --project helloworld

digdag push python-sample --project python-sample

digdag push python-sample2 --project python-sample2
digdag secret --project python-sample2 --set test=env-test
digdag secrets --project python-sample2 --set test-json=@python-sample2/test.json
```
