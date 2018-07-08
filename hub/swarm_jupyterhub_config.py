# Example config
c = get_config()

c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.spawner_class = 'mig.SwarmSpawner'

# The name of the service that's running the hub
c.SwarmSpawner.jupyterhub_service_name = "jupyterhub"

c.SwarmSpawner.start_timeout = 60 * 10

# The name of the overlay network that everything's connected to
c.SwarmSpawner.networks = ["jh_test"]

# Before the user can select which image to spawn,
# user_options has to be enabled
c.SwarmSpawner.use_user_options = True

c.SwarmSpawner.dockerimages = [
    {'image': 'nielsbohr/base-notebook-devel:743fe46511dc',
     'name': 'Basic Python Notebook'}
]

c.SwarmSpawner.container_spec = {
    'args': ['/usr/local/bin/start-singleuser.sh'],
    'env': {'JUPYTER_ENABLE_LAB': '1'}
}

c.JupyterHub.authenticator_class = 'jhubauthenticators.DummyAuthenticator'
c.DummyAuthenticator.password = 'password'