docker_tag=reticulok
python_version=3.8


build:
	python3 -m build


# used for troubleshooting the package in a particular python3 version
docker-build:
	docker build \
		--no-cache \
		--rm \
		--tag=$(docker_tag)-$(python_version) \
		--build-arg PYTHON_VERSION=$(python_version) \
		.


# run a new container with the particular version of python
docker-bash:
	docker run \
		-ti \
		--name $(docker_tag)-$(python_version) \
		$(docker_tag)-$(python_version) \
		bash


# if the container has already been initiated, re-enter using docker exec
docker-exec:
	docker exec -ti $(docker_tag)-$(python_version) bash
