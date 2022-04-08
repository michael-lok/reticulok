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


docker-bash:
	docker run -ti $(docker_tag)-$(python_version) bash
