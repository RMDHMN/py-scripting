import ansible_runner

def run_playbook():
    r = ansible_runner.run(private_data_dir='/path/to/playbooks', playbook='site.yml')
    print("{}: {}".format(r.status, r.rc))
    for each_host_event in r.events:
        print(each_host_event['stdout'])

run_playbook()
