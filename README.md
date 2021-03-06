# Cluster UI

Run commands or an interactive session in the cluster.

## Usage

    Usage: cui [options] [command]

    Submit a UI job and connect to it when it begins to run. If <command> is
    specified, it is executed on the remote machine. Otherwise, the current shell
    ($SHELL) is executed.

    To connect a UI job that's already running, pass its ClusterId to the '-i'
    option. Use the special ID 'any' to automatically select a suitable running job.

    By default, cui will use glexec to switch to the grid user after connecting to
    the UI job; pass the '-g' option to disable glexec.

    After the connection is terminated, the UI job's temporary directory including
    its submit file, log file and any files transferred back from the remote
    machine will be removed. To prevent cleanup, pass the '-P' option; since no
    temporary directory is created when connecting to an existing job with '-i',
    cleanup does not occur in that case, either.


    Options:
      -v VERBOSE, --verbose=VERBOSE
                            set logging level to VERBOSE
      -P, --persist         leave UI job in the queue
      -d SUBMIT_DIR, --submit-dir=SUBMIT_DIR
                            create submit directory under SUBMIT_DIR
      -i ID, --id=ID        connect to existing job ID
      -p, --preserve        preserve temporary job directory
      -x, --x509            disable X509 proxy detection
      -h, --help            show this help message and exit
