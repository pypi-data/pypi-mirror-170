import os
import sys
import yaml
import pprint
from pymacaron.log import pymlogger
from urllib.parse import urlparse


log = pymlogger(__name__)


class PyMacaronConfig(object):

    def __init__(self):
        """Initialize a minimal pymacaron config"""

        # Some defaults, required by pymacaron.auth
        self.jwt_issuer = None
        self.jwt_audience = None
        self.jwt_secret = None
        self.jwt_token_timeout = 86400
        self.jwt_token_renew_after = 10800
        self.default_user_id = 'PYM_DEFAULT_USER_ID'

        # Default time-limit for the slow-call report
        self.report_call_exceeding_ms = 1000


    def load_pym_config(self, path=None, env=None):
        """Search for a pym-config file and load it if found, otherwise raise an error
        for not finding any.
        """

        # Find a pym-config file
        pym_env = os.environ.get('PYM_ENV', None)
        if env:
            pym_env = env
        log.debug(f"Target environment is: [{pym_env}]")

        config_name = f'pym-config.{pym_env}.yaml'
        config_path = get_config_path(config_name, path=path)
        if not config_path:
            log.debug(f"Could not find {config_name} - Trying to find pym-config.yaml")
            config_path = get_config_path('pym-config.yaml', path=path)

        if not config_path:
            raise Exception("Failed to find pym-config!")

        self.config_path = config_path

        # Find where the apis/ directory
        self.apis_path = os.path.join(os.path.dirname(self.config_path), 'apis')
        if not os.path.exists(self.apis_path):
            raise Exception(f"Cannot find apis directory at {self.apis_path}")

        # Load all attributes defined in pym-config into self
        log.info(f"Loading config file at {config_path}")
        all_keys = []
        config_dict = {}
        with open(config_path, 'r') as stream:

            # Support versions of PyYAML with and without Loader
            import pkg_resources
            v = pkg_resources.get_distribution("PyYAML").version
            if v > '3.15':
                config_dict = yaml.load(stream, Loader=yaml.FullLoader)
            else:
                config_dict = yaml.load(stream)

            for k, v in config_dict.items():
                setattr(self, k, v)
                all_keys.append(k)

        # Validate config
        if hasattr(self, 'live_url'):
            o = urlparse(self.live_url)
            host = o.netloc
            if ':' in host:
                host = host.split(':')[0]
            self.live_host = host

        if not hasattr(self, 'live_host'):
            raise Exception("'pym-config.yaml' lacks the 'live_host' or 'live_url' key")

        # Magic here :-)
        # For all keys whose value is in the list of environment secrets, replace
        # that value with the value of the corresponding environment variable.
        if hasattr(self, 'env_secrets'):
            log.info("Substituting secret environment variable names for their values in config")
            for k in all_keys:
                if getattr(self, k) in self.env_secrets:
                    setattr(self, k, os.environ.get(getattr(self, k), k))
                    config_dict[k] = str(getattr(self, k))[0:8] + '****'

        # Print config file to log, but obfuscate secrets
        log.debug("Loaded configuration:\n%s" % pprint.pformat(config_dict, indent=4))


def get_config_path(name='pym-config.yaml', path=None):
    """Search for a file named 'name' in all the places where 'pym-config.*.yaml'
    is normally looked for.  Return a path if found, or None if not found
    """

    paths = [
        os.path.join(os.path.dirname(sys.argv[0]), name),
        '/pym/%s' % name,
        os.path.join(os.path.dirname(sys.argv[0]), 'test/%s' % name),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', name),
        os.path.join(os.getcwd(), name),
    ]

    if path:
        if not path.endswith(name):
            path = os.path.join(path, name)
        paths.append(path)

    for p in paths:
        p = os.path.abspath(p)
        log.info("Looking for file %s at %s" % (name, p))
        if os.path.isfile(p):
            return p

    return None


config = None


def get_config():
    """Find the pym-config yaml file for the current environment, as identified by
    the PYM_ENV variable. Look at all standard locations. Optionally take an
    extra location/path to look at, and/or an environment that overrides
    PYM_ENV
    """

    global config
    if not config:
        config = PyMacaronConfig()
    return config
