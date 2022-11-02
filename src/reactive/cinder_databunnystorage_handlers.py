#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import charms_openstack.charm
import charms.reactive
from charmhelpers.core import hookenv as hook
import subprocess
# This charm's library contains all of the handler code associated with
# this charm -- we will use the auto-discovery feature of charms.openstack
# to get the definitions for the charm.
import charms_openstack.bus
charms_openstack.bus.discover()
import charmhelpers.core.hookenv as hookenv
from charmhelpers.fetch.python.packages import pip_install
charms_openstack.charm.use_defaults(
    'charm.installed',
    'update-status',
    'upgrade-charm',
    'storage-backend.connected',
)
@charms.reactive.when_not('storagedriver.installed')
def installdriver():
    #make sure driver is installed in parent environment not .venv 
    completeprocess = subprocess.run("/usr/bin/pip install databunnystoragedriver", shell=True)
    if completeprocess.returncode == 0:
        charms.reactive.set_flag("storagedriver.installed")
        hook.status_set(hook.WORKLOAD_STATES.WAITING,"Driver databunnystoragedriver successful installed")
        charms.reactive.set_flag('storagedriver.installed')
    else:
        hook.status_set(hook.WORKLOAD_STATES.BLOCKED,"Driver databunnystoragedriver installation failed")

@charms.reactive.when('config.changed.driver-source')
def reinstall():
    with charms_openstack.charm.provide_charm_instance() as charm:
        charm.install()
