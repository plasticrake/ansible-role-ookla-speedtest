# Role Name

An Ansible Role that installs [Ookla Speedtest CLI](https://www.speedtest.net/apps/cli).

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    speedtest_package_state: present

The state of the speedtest package install. If you want to always update to the latest version, change this to `latest`.

    speedtest_remove_conflicts: yes

Whether to remove conflicting packages (`speedtest-cli`)

### Debian / Ubuntu

    speedtest_repo_install_key: 379CE192D401AB61
    speedtest_apt_repository: "deb https://ookla.bintray.com/debian generic main"

### RedHat / CentOS / Fedora

    speedtest_yum_repo_url: https://bintray.com/ookla/rhel/rpm
    speedtest_yum_dest: /etc/yum.repos.d/bintray-ookla-rhel.repo

## Dependencies

None.

## Example Playbook

    - hosts: servers
      roles:
        - ansible-role-ookla-speedtest
      become: yes

## License

MIT
