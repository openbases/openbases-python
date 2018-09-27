#!/bin/bash

usage () {

    echo "Usage:

    This entrypoint connects you to the executables provided by openbases
    Python within the container. You could just as easily exec one of these
    commands to the container, but this entrypoint makes this easy to do
    with just 'run':

         ob-validate: validate a paper.md for an Open Journals submission
           docker run <container> validate --help
           docker run <container> validate paper --help

           # The repository with the paper, LICENSE, etc. is in $PWD
           docker run -v $PWD:/data <container> validate --infile /data/paper.md
           docker run -it -v $PWD/:/data <container> validate paper --infile /data/paper.md


         ob-icons: produce
           docker run <container> icons --help
           docker run <container> icons

         ob-paper: generate a paper.pdf for an Open Journals submission
           docker run <container> paper --help
           docker run <container> paper

         ob-badges: generate markdown badges!
           docker run <container> badges --help
           docker run <container> badges

         or just ask to see this global help!
         docker run <container> help
         "
}

if [ $# -eq 0 ]; then
    usage
    exit
fi

while true; do
    case ${1:-} in
        -h|--help|help)
            usage
            exit
        ;;
        paper)
            shift
            exec ob-paper "$@"
            exit 0
        ;;
        validate)
            shift
            exec ob-validate paper "$@"
            exit 0
        ;;
        icons)
            shift
            exec ob-icons "$@"
            exit 0
        ;;
        badges|badge)
            shift
            exec ob-badge "$@"
            exit 0
        ;;
        -*)
            echo "Unknown option: ${1:-}"
            usage
            exit 1
        ;;
        *)
            break
        ;;
    esac
done
