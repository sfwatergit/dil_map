from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/hjwp/book-example.git'

def deploy():
    site_folder = '/root/www/dil/dev/wordpress/%s' % (env.user)
    source_folder = site_folder + '/source'
    # _create_directory_structure_if_necessary(site_folder)
    # _get_latest_source(source_folder)
    # _update_settings(source_folder, env.host)
    # _update_virtualenv(source_folder)
    # _update_static_files(source_folder)
    # _update_database(source_folder)

