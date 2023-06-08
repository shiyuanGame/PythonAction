import argparse
import logging
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token_string', type=str, required=True)

    args = parser.parse_args()
    token_string = args.token_string
    pushplus_token = os.environ.get('PUSHPLUS_TOKEN', None)
    serverChan_sendkey = os.environ.get('SERVERCHAN_SENDKEY', None)
    weCom_webhook = os.environ.get('WECOM_WEBHOOK', None)
    bark_deviceKey = os.environ.get('BARK_DEVICEKEY', None)
    print('finish', token_string, pushplus_token,
          serverChan_sendkey, weCom_webhook, bark_deviceKey)
    logging.debug("test", token_string, pushplus_token,
                  serverChan_sendkey, weCom_webhook, bark_deviceKey)
    print('finish', token_string, pushplus_token,
          serverChan_sendkey, weCom_webhook, bark_deviceKey)
    pass


if __name__ == "__main__":
    main()
