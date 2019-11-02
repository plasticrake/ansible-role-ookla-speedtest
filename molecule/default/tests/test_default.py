import os
import stat

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_speedtest_file(host):
    command_path = host.find_command('speedtest')
    file = host.file(command_path)

    assert file.exists
    assert file.size > 0
    assert file.is_file
    assert file.mode & stat.S_IXUSR == stat.S_IXUSR
