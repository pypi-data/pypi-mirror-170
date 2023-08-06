set -ex

IMAGE=mock-event-generator:dev-0.0.0
LIGO_CERTIFICATE_PATH=/tmp/x509up_u$(id -u)

DOCKER_BUILDKIT=1 docker build \
    --pull \
    --secret id=netrc,src=${HOME}/.netrc \
    --secret id=x509,src=${LIGO_CERTIFICATE_PATH} \
    --progress=plain \
    -t ${IMAGE} .
