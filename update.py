import cv2
from pyzbar.pyzbar import decode

import os
import json
import argparse
from datetime import datetime


ConfigFilePath = os.path.join(os.path.dirname(__file__),
                              'config.json')


def read_qrcode(path: str) -> str:
    """Reads a QR code from an image file and returns the decoded data as a string.

    Args:
        path (str): The file path to the image containing the QR code.

    Returns:
        str: The decoded data from the QR code.

    Raises:
        IndexError: If no QR code is found in the image.
    """
    image = cv2.imread(path)
    decoded = decode(image)
    return decoded[0].data.decode('utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='使用图片直接更新 config.json 配置文件')
    parser.add_argument('-u', '--update', type=str, help='二维码文件的路径')
    parser.add_argument('-d', '--disable', default=False, action='store_true',
                        help='禁用备用群更新（当人数超过 200 人时使用）')
    args = parser.parse_args()

    # Read current config
    with open(ConfigFilePath, 'r') as handler:
        config = json.load(handler)
        backup_link = config['backupGroupQR']
        backup_status = config['backupGroupStatus']
        udpate_date = config['lastUpdated']

    args = parser.parse_args()
    if args.update:
        try:
            backup_link = read_qrcode(args.update)
            udpate_date = datetime.now().strftime('%Y-%m-%d')
        except Exception as error:
            print(f'文件 {args.update} 读取失败: {error}')
            exit(1)
    elif args.disable:
        backup_status = 'full'
        udpate_date = datetime.now().strftime('%Y-%m-%d')
    else:
        parser.print_help()

    # Write config file back
    with open(ConfigFilePath, 'w') as handler:
        config['backupGroupQR'] = backup_link
        config['backupGroupStatus'] = backup_status
        config['lastUpdated'] = udpate_date
        json.dump(config, handler, indent=4)
