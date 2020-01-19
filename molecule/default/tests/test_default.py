import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_config_exists(host):
    assert host.file('/etc/netatalk/afp.conf').exists


def test_line_in_config(host):
    conf_file = host.file('/etc/netatalk/afp.conf')
    assert 'valid users = "root"' in conf_file.content_string
    # assert conf_file.contains('valid_users = "root"')
