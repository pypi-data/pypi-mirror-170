set -ex

DOCKER_BUILDKIT=1 docker build \
    --pull \
    --build-arg BUILD_ENV=prod \
    --build-arg PACKAGE_VERSION \
    --secret id=netrc,src=${HOME}/.netrc \
    --secret id=x509,src=${LIGO_CERTIFICATE_PATH} \
    --progress=plain \
    -t ${CONTAINER_TEST_IMAGE} .
