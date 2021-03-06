# Copyright 2019-2020 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from klio_cli.commands import base


class TestPipeline(base.BaseDockerizedPipeline):
    DOCKER_LOGGER_NAME = "klio.job.test"

    def __init__(self, job_dir, klio_config, docker_runtime_config):
        super().__init__(job_dir, klio_config, docker_runtime_config)
        self.requires_config_file = False

    def _get_environment(self):
        envs = super()._get_environment()
        envs["KLIO_TEST_MODE"] = "true"
        return envs

    def _get_command(self, pytest_args):
        return ["test"] + pytest_args
