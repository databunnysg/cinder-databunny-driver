# Overview  

 This is cinder storage driver charm support to use freenas/truenas core/truenas scale integration for OpenStack Block Storage.  
 Cinder is the block storage service for the Openstack project.  

 Charmhub repository link: https://charmhub.io/cinder-databunny-driver

Driver was repackaged to [https://github.com/databunnysg/databunnystoragedriver](https://github.com/databunnysg/databunnystoragedriver) with further fix to support Truenas core (tested freenas 11.3). Limited support on Truenas scale as for now! (maynot work)
And published as pypi package [pypi databunnystoragedriver package](https://pypi.org/project/databunnystoragedriver/).  

> **Note**: The driver code forked from (ixsystems cinder driver)[https://github.com/iXsystems/cinder]   

[![Alt text](https://img.youtube.com/vi/B5XjPMOJmtE/0.jpg)](https://www.youtube.com/watch?v=B5XjPMOJmtE)

# Usage  
Usage is simple:  
Step 1:  
  Create or modify a driver config file, lets say: driverconfigfile.yaml  
  Modify the config paramerter to exactly match your freenas/truenas configuration.  
Step 2:  
  juju deploy ch:cinder-databunny-driver  
  juju relate cinder-databunny-driver:storage-backend cinder:storage-backend  
  juju config cinder-databunny-driver --file=driverconfigfile.yaml  
Step 3:  
  waiting for cinder-databunny-driver become active  
  login to openstack dashboard, create volume type and Update Volume Type Metadata volume_backend_name databunnystorage  

  Wait for cinder-databunny-driver juju status become active and now you can use openstack dashboard create volume with volume type databunnystore, those volume will be provision and managed by freenas/truenas  

## Configuration  

  Create a yaml config file with configuration reflecting your freenas/truenas configuration  

  Save it as an yaml file for example configfilesample.yaml.  
  Then run below command:  
  juju config cinder-databunny-driver --file=configfilesample.yaml  


<pre>
  cinder-databunny-driver:  
    ixsystems_server_hostname : 10.0.50.211  
    ixsystems_server_port : "80"  
    ixsystems_server_iscsi_port : "3260"  
    ixsystems_api_version : "2.0"  
    ixsystems_volume_backend_name : databunnystorage  
    ixsystems_vendor_name : iXsystem  
    ixsystems_storage_protocol : iscsi  
    ixsystems_transport_type : http  
    ixsystems_login : root  
    ixsystems_password : "password"  
    ixsystems_datastore_pool : pool  
    ixsystems_dataset_path : pool/cinder  
    ixsystems_reserved_percentage : "0"  
    ixsystems_iqn_prefix : iqn.2005-10.org.freenas.ctl  
    ixsystems_portal_id : "1"  
    ixsystems_initiator_id : "1"  
    iscsi_helper : tgtadm  
    volume_dd_blocksize : 1M  
    volume_driver : driver.iscsi.FreeNASISCSIDriver  
</pre>
# Documentation  



# Bugs  



