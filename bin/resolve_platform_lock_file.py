import sys

from pip_constraint_helpers import (
    get_constraint_file_path,
    get_runtime_python_tag,
    make_pip_cmd,
    run_cmd,
)


def main(req_dir, toxenv, *pip_args):
    constraint_file_path = get_constraint_file_path(
        req_dir=req_dir,
        toxenv=toxenv,
        python_tag=get_runtime_python_tag(),
    )
    pip_cmd = make_pip_cmd(
        pip_args=list(pip_args),
        constraint_file_path=constraint_file_path,
    )
    run_cmd(pip_cmd)


if __name__ == '__main__':
    main(*sys.argv[1:])