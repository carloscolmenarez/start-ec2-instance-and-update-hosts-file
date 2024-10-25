# Start EC2 Instance and Update Hosts System File

A Python script to start your **AWS EC2 instance** and update your computer's `hosts` file with the instance's public IP address for as many hosts as you want. All in one step!

## What does it do?

1. Starts the EC2 instance.
2. Retrieves the instance's public IP.
3. Update the system `hosts` file with the public IP for the urls specified in the `hosts.txt` file (one per line).

## Requirements

- Python 3.6 or higher.
- An AWS account with access key credentials. Learn [how to create access keys in AWS](https://github.com/carloscolmenarez/start-ec2-instance-and-update-hosts-file/wiki/How-to-create-access-keys-in-AWS).
- Administrator or root permissions to write the `hosts` system file.

## Dependencies

Install the required dependencies using `pip`:


### For Windows ![alt text](https://raw.githubusercontent.com/carloscolmenarez/start-ec2-instance-and-update-hosts-file/refs/heads/master/images/windows_logo.png):

```bash
pip install boto3 python-dotenv pywin32
```

### For Linux ![alt text](https://raw.githubusercontent.com/carloscolmenarez/start-ec2-instance-and-update-hosts-file/refs/heads/master/images/linux-logo.png):
```bash
sudo pip install boto3 python-dotenv
```

## Installation and Configuration

1. Clone the repository:

    ```bash
    git clone https://github.com/carloscolmenarez/start-ec2-instance-and-update-hosts-file.git
    cd start-ec2-instance-and-update-hosts-file
    ```

2. Create a `.env` file in the root directory of the project with the following content:

    ```
    INSTANCE_ID=your_instance_id
    AWS_ACCESS_KEY_ID=your_access_key_id
    AWS_SECRET_ACCESS_KEY=your_secret_access_key
    AWS_REGION=eu-west-1
    HOSTS_PATH=C:\Windows\System32\drivers\etc\hosts
    ```

    Replace `your_instance_id`, `your_access_key_id`, `your_secret_access_key`, and `eu-west-1` with your instance ID, AWS credentials (Access Key), and region. 
    
    In Linux ![alt text](https://raw.githubusercontent.com/carloscolmenarez/start-ec2-instance-and-update-hosts-file/refs/heads/master/images/linux-logo.png), the `HOSTS_PATH` usually is `/etc/hosts`.

3. Create a `hosts.txt` file in the root directory of the project with the hosts you want to add/update in your `hosts` system file, using the public IP of the EC2 instance (one host per line) See `hosts.txt.example` for reference.

## Usage

### On Windows ![alt text](https://raw.githubusercontent.com/carloscolmenarez/start-ec2-instance-and-update-hosts-file/refs/heads/master/images/windows_logo.png):

- Open a terminal as an administrator an run:

```bash
python start_ec2_instance.py
```

### On Linux ![alt text](https://raw.githubusercontent.com/carloscolmenarez/start-ec2-instance-and-update-hosts-file/refs/heads/master/images/linux-logo.png):


```bash
sudo python start_ec2_instance.py
```

## Create a Desktop Shortcut (Only for Windows ![alt text](https://raw.githubusercontent.com/carloscolmenarez/start-ec2-instance-and-update-hosts-file/refs/heads/master/images/windows_logo.png)):

If you prefer not to use the terminal, you can create a Windows desktop shortcut:

- Run the ``create_windows_shortcut.py`` script to create a desktop shortcut called "Start EC2 Instance and Update Hosts". You can then run the script with a single (or double) click.

```bash
python create_windows_shortcut.py
```

Now you will have a shortcut in your desktop to run the script just in one click (or two).

## Notes

- Ensure you have administrator permissions to modify ``hosts`` file.
- Do not share your AWS credentials. Use secure methods to manage them.

## License

This project is licensed under the MIT License. See the LICENSE file for details.