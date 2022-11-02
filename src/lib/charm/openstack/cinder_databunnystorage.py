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

charms_openstack.charm.use_defaults('charm.default-select-release')

from charmhelpers.fetch.python.packages import pip_install
class CinderDatabunnyDriverCharm(
        charms_openstack.charm.CinderStoragePluginCharm):

    name = 'cinder-databunny-driver'
    version_package = 'cinder-common'
    release = 'ocata'
    packages = []
    release_pkg = 'cinder-common'
    # The driver currently does not support ACTIVE-ACTIVE
    stateless = False
    # Specify any config that the user *must* set.
    mandatory_config = ['iscsi_helper','volume_dd_blocksize'
        ,'volume_driver','ixsystems_login'
        ,'ixsystems_password','ixsystems_server_hostname'
        ,'ixsystems_server_port','ixsystems_transport_type'
        ,'ixsystems_volume_backend_name','ixsystems_iqn_prefix'
        ,'ixsystems_datastore_pool','ixsystems_dataset_path'
        ,'ixsystems_vendor_name','ixsystems_storage_protocol']

    def cinder_configuration(self):
        cget = self.config.get

        driver_options_common = [
            ('iscsi_helper', cget('iscsi_helper')),
            ('volume_dd_blocksize', cget('volume_dd_blocksize')),
            ('volume_driver', cget('volume_driver')),
            ('ixsystems_login', cget('ixsystems_login')),
            ('ixsystems_password', cget('ixsystems_password')),
            ('ixsystems_server_hostname', cget('ixsystems_server_hostname')),
            ('ixsystems_server_port', cget('ixsystems_server_port')),
            ('ixsystems_transport_type', cget('ixsystems_transport_type')),
            ('ixsystems_volume_backend_name', cget('ixsystems_volume_backend_name')),
            ('ixsystems_iqn_prefix', cget('ixsystems_iqn_prefix')),
            ('ixsystems_datastore_pool', cget('ixsystems_datastore_pool')),
            ('ixsystems_dataset_path', cget('ixsystems_dataset_path')),
            ('ixsystems_vendor_name', cget('ixsystems_vendor_name')),
            ('ixsystems_storage_protocol', cget('ixsystems_storage_protocol')),      
            ('ixsystems_server_iscsi_port', cget('ixsystems_server_iscsi_port')),                                              
        ]
        return (driver_options_common)


class CinderNetAppCharmRocky(CinderDatabunnyDriverCharm):

    # Ussuri needs py3 packages.
    release = 'rocky'
    version_package = 'cinder-common'
    packages = []
