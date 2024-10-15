from netmiko import ConnectHandler

device = ConnectHandler(
    host = 'ceos01',
    username = 'netobs',
    password = 'netobs',
    device_type = 'arista_eos'
)

show_run_output = device.send_command('show interface status')

print(show_run_output)
