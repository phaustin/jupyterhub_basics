# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'jupyterhub_test'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image = 'phaustin/notebook:sep23'
notebook_dir = "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'net_test'
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir,
                            "/Users/phil/repos/a301_2020/sat_data": 
                            {"bind": '/home/jovyan/work/sat_data', "mode": "ro"},
                            "/Users/phil/repos/a301_2020/a301_lib": 
                            {"bind": '/home/jovyan/work/a301_lib', "mode": "ro"},
                            "/Users/phil/repos/a301_2020/data_share": 
                            {"bind": '/home/jovyan/work/data_share', "mode": "rw"},
                           }


# delete containers when the stop
c.DockerSpawner.remove = True
