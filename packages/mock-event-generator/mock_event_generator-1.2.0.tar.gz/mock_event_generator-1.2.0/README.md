# Mock Event Generator

This package re-generates past events by shifting their time reference.

## Setting up

### Using a docker image

Containers are stored in the Gitlab's Container Registry. To access them, a [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) (with at least the read_registry scope) is required. To login:

```bash
$ echo <access-token> | docker login containers.ligo.org -u <token-name> --password-stdin
```

Upon successful login, and provided that a valid x509 certificate can be mounted in the container, the latest Docker image can be run. It contains a pre-loaded mock super-event from GraceDB playground. By creating a docker volume to be used for the mock-event-generator cache, downloaded events can be persisted.
```bash
$ docker volume create meg-cache
$ docker run --pull always -it --rm \
    -v meg-cache:/home/meguser/.cache/mock-event-generator \
    -v /tmp/x509up_u$(id -u):/tmp/x509up_u1000 \
    containers.ligo.org/emfollow/mock-event-generator:latest bash
meguser@f8e5602cb5d7:~$ meg cache list
Cache: /home/meguser/.cache/mock-event-generator
└── S220609hl
    ├── G587364     gstlal         CBC            AllSky         1338848303.813655
    ├── G587365     gstlal         CBC            AllSky         1338848303.808759
    ├── G587366     MBTAOnline     CBC            AllSky         1338848303.869315
    ├── G587367     CWB            Burst          BBH            1338848303.7873
    ├── G587368     CWB            Burst          AllSky         1338848303.7855
    └── G587369     CWB            Burst          BBH            1338848303.7875
meguser@f8e5602cb5d7:~$ meg fetch E394410
2022-06-22 13:29:32 INFO     Downloading E394410 from the production GraceDB server...
```


### Last stable from the Gitlab Package Index

A Personal access key is required (read_api scope) to access the mock-event-generator package. Add this line to your .netrc file:

```
machine git.ligo.org login <token-name> password <access-token>
```

Then:
```bash
python3.9 -m venv venv
source venv/bin/activate
pip install --extra-index-url=https://git.ligo.org/api/v4/projects/11815/packages/pypi/simple mock-event-generator
meg fetch S220609hl --source playground
```

To recreate the events in the CNAF instance (test01), a CA certificate should be added. To download it, the same token access can be used:
```bash
curl --silent --header 'Private-Token: <token-access>' --remote-name --remote-header-name https://git.ligo.org/api/v4/projects/11815/repository/files/certificate-terena-ssl-ca-3.pem/raw?ref=main
meg ca-certificate certificate-terena-ssl-ca-3.pem
```

And then:
```bash
meg create S220609hl --target cnaf
```

### Cutting edge from the git repository through pip

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install git+ssh://git@git.ligo.org/emfollow/mock-event-generator.git
meg fetch S220609hl --source playground
meg create S220609hl --target test
```

To recreate events in the CNAF instance, the steps in the previous section related to the CA certificate should be followed.


### For development purposes
Create a [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) with the read_api scope. This token is required in order to install the package [`pytest-gracedb`](https://git.ligo.org/pierre.chanial/pytest-gracedb) from Gitlab's package registry. This package provides the GraceDB test double used by the unit tests, and because it contains private information, it cannot be shared publicly in the Python Package Index. Once the token is created, add this line to your .netrc file:

```
machine git.ligo.org login <token-name> password <access-token>
```

The project uses [pre-commit](https://pre-commit.com) to ensure code quality and uniformity.
```bash
git clone git@git.ligo.org:emfollow/mock-event-generator.git
cd mock-event-generator
pip install --user pre-commit
pre-commit install
python3.9 -mvenv venv
source venv/bin/activate
pip install --extra-index-url https://git.ligo.org/api/v4/projects/11906/packages/pypi/simple -e ".[tests]"
```

To access the test01 GraceDB instance, a CA certificate should be added to the default CA bundle.
```bash
meg ca-certificate certificate-terena-ssl-ca-3.pem
```

To run the unit tests (with a mocked GraceDB server):
```bash
$ pytest
```

To run the end-to-end tests (using the playground GraceDB server):
```bash
$ pytest e2e
```


## Getting started

Once the package is installed, the executable `meg` is available.

To download all the events belonging to a super-event from the production GranceDB.

```bash
$ meg fetch S200225q --source production
```

To list the content of the cache:
```bash
$ meg cache list --include-files
```

To re-create all the events belonging to a super-event in the playground GraceDB, with the search type set to 'MDC':
```bash
$ meg create S200225q --target playground
```

To re-create a single event:
```bash
$ meg create G355462 --target playground
```

To cleanup the cache:
```bash
$ meg cache clean
```

Detailed information on the CLI usage can be displayed with the `--help` option:

```bash
$ meg --help
```
```
 Usage: meg [OPTIONS] COMMAND [ARGS]...

 Mock Event Generator.

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                           │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.    │
│ --help                        Show this message and exit.                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ ca-certificate                Add a Certification Authority certificate.                                          │
│ cache                         Event cache utilities                                                               │
│ create                        Create G-events and send them to GraceDB.                                           │
│ fetch                         Fetch G-events and store them in the cache.                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Command `fetch`

```
 Usage: meg fetch [OPTIONS] EVENTS...

 Fetch G-events and store them in the cache.

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    events      EVENTS...  G-events or S-events to be generated. [default: None] [required]                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --source                                 TEXT  GraceDB instance (production, playground, test, cnaf, mocked or    │
│                                                <URL>) from which the original events are downloaded.              │
│                                                [default: production]                                              │
│ --cache-path                             PATH  Directory where the event' data files are downloaded.              │
│                                                [default: /home/chanial/.cache/mock-event-generator]               │
│ --refresh-cache    --no-refresh-cache          If set, ignore the event's potential cache entry.                  │
│                                                [default: no-refresh-cache]                                        │
│ --help                                         Show this message and exit.                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Command `cache list`
```
Usage: meg cache list [OPTIONS]

 List the content of the cache.

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --include-files    --no-include-files          If set, also display the data files. [default: no-include-files]   │
│ --cache-path                             PATH  Directory where the event' data files are downloaded.              │
│                                                [default: /home/chanial/.cache/mock-event-generator]               │
│ --help                                         Show this message and exit.                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Command `cache clean`

```
 Usage: meg cache clean [OPTIONS]

 Remove the content of the cache.

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --cache-path        PATH  Directory where the event' data files are downloaded.                                   │
│                           [default: /home/chanial/.cache/mock-event-generator]                                    │
│ --help                    Show this message and exit.                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Command `create`
```
 Usage: meg create [OPTIONS] EVENTS...

 Create G-events and send them to GraceDB.

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    events      EVENTS...  G-events or S-events to be generated. [default: None] [required]                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --target                                     TEXT   GraceDB instance (production, playground, test, cnaf,      │
│                                                        mocked or <URL>) to which the time-translated events are   │
│                                                        sent.                                                      │
│                                                        [default: None]                                            │
│                                                        [required]                                                 │
│    --username                                   TEXT   Username for basic authentication on the target GraceDB    │
│                                                        server.                                                    │
│                                                        [default: None]                                            │
│    --password                                   TEXT   Password for basic authentication on the target GraceDB    │
│                                                        server.                                                    │
│                                                        [default: None]                                            │
│    --source                                     TEXT   GraceDB instance (production, playground, test, cnaf,      │
│                                                        mocked or <URL>) from which the original events are        │
│                                                        downloaded.                                                │
│                                                        [default: production]                                      │
│    --group                                      TEXT   Change the analysis group which identified the candidate.  │
│                                                        [default: None]                                            │
│    --search                                     TEXT   Change the type of search of the analysis pipeline. By     │
│                                                        default, the event search is changed to 'MDC'.             │
│                                                        [default: None]                                            │
│    --original-search    --no-original-search           Use the original event search type, instead of MDC.        │
│                                                        [default: no-original-search]                              │
│    --cache-path                                 PATH   Directory where the event' data files are downloaded.      │
│                                                        [default: /home/chanial/.cache/mock-event-generator]       │
│    --refresh-cache      --no-refresh-cache             If set, ignore the event's potential cache entry.          │
│                                                        [default: no-refresh-cache]                                │
│    --max-delay                                  FLOAT  Shrink the interval between the first event creation and   │
│                                                        the last upload (in seconds). By setting zero, all uploads │
│                                                        are sent at once.                                          │
│                                                        [default: None]                                            │
│    --help                                              Show this message and exit.                                │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
