# Start EC2 Instance and Update Hosts File for Windows

A Python script to start an EC2 instance on AWS and update the Windows `hosts` file with the instance's public IP address for many hosts as you want. All in one step!

# What it does?

- Launch the EC2 instance.
- Get the instance public IP.
- Updates the Windows hosts file with the public IP address for the hosts specified in the urls.txt file.

## Requirements

- Python 3.6 or higher
- An AWS account with an access key credential
- Administrator permissions on the Windows system to modify the `hosts` file

## Dependencies

- boto3
- python-dotenv
- pywin32

The necessary dependencies can be installed using `pip`:

```bash
pip install boto3 python-dotenv pywin32
```

## Configuration

1. Clone the repository:

    ```
    git clone https://github.com/carloscolmenarez/start-ec2-instance-and-update-hosts-file.git
    cd start-ec2-instance-and-update-hosts-file
    ```

2. Create a .env file in the root directory of the project with the following content:

    ```
    INSTANCE_ID=your_instance_id
    AWS_ACCESS_KEY_ID=your_access_key_id
    AWS_SECRET_ACCESS_KEY=your_secret_access_key
    AWS_REGION=eu-west-1
    HOSTS_PATH=C:\Windows\System32\drivers\etc\hosts
    ```

    Replace `your_instance_id`, `your_access_key_id`, `your_secret_access_key`, and `eu-west-1` with your instance ID, AWS credentials (Access Key) and region.

3. Create a hosts.txt file in the root directory of the project with all the hosts you want to create/update in your Windows `hosts` file with the public IP of the EC2 instance (one host per line). See hosts.txt.example file.

### How to create access keys in AWS:

- Log in AWS Management Console.
- In the navigation bar on the upper right, choose your user name, and then choose Security credentials.
- In the access key section, click on "Create access key" button.
- Select the "Third-party service" option and click next.
- Set a description tag a click on "Create access key" button to finish.



## Usage

Run the script ``create_windows_shortcut.py`` once to create a Windows "Start EC2 Instance and update hosts" shortcut in your desktop to run the script in one click.

```bash
python create_windows_shortcut.py
```

Or, if you prefer to use the terminal, run (as administrator):

```bash
python start_ec2_instance.py
```

## Notes

- Make sure you have administrator permissions to modify the ``hosts`` file.
- Do not share your AWS credentials. Use secure methods to manage them.

## License

This project is licensed under the MIT License. See the LICENSE file for details.