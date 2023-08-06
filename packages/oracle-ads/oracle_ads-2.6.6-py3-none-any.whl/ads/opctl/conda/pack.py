#!/usr/bin/env python
# -*- coding: utf-8; -*-

# Copyright (c) 2022 Oracle and/or its affiliates.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl/

import subprocess
from io import StringIO
import tempfile
import os
import datetime
import shutil
import sys
import glob
import stat

import yaml
from ads.common.decorator.runtime_dependency import (
    runtime_dependency,
    OptionalDependency,
)


@runtime_dependency(module="conda_pack", install_from=OptionalDependency.OPCTL)
def main(pack_folder_path):
    slug = os.path.basename(pack_folder_path)
    manifest_path = glob.glob(os.path.join(pack_folder_path, "*_manifest.yaml"))[0]
    with open(manifest_path) as f:
        env = yaml.safe_load(f.read())

    with tempfile.TemporaryDirectory() as td:
        process = subprocess.Popen(
            ["conda", "env", "export", "--prefix", pack_folder_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()
        if stderr:
            print(stderr)
            raise Exception(
                f"Error export environment information from {pack_folder_path}"
            )
        try:
            new_env_info = yaml.safe_load(StringIO(stdout.decode("utf-8")))
        except Exception as e:
            print(f"Error reading dependency list from {stdout}")
            raise e

        manifest = env["manifest"]
        manifest["type"] = "published"
        new_env_info["manifest"] = manifest
        with open(manifest_path, "w") as f:
            yaml.safe_dump(new_env_info, f)
        pack_file = os.path.join(td, f"{slug}.tar.gz")
        conda_pack.pack(
            prefix=pack_folder_path,
            compress_level=7,
            output=pack_file,
            n_threads=-1,
            ignore_missing_files=True,
        )
        if not os.path.exists(pack_file):
            raise RuntimeError(
                "Error creating the pack file using `conda_pack.pack()`."
            )
        shutil.copy(pack_file, pack_folder_path)


if __name__ == "__main__":
    main(sys.argv[1])
