import argparse
import boto.s3.connection
import code
import os
import readline
import rlcompleter
import yaml


# silence pyflakes
rlcompleter.__name__


def main():
    parser = argparse.ArgumentParser(
        usage='%(prog)s',
        )
    parser.add_argument(
        '--config',
        default=os.path.expanduser('~/.botosh.yaml'),
        help='Config file to read (default %(default)s)',
        )
    args = parser.parse_args()

    with file(args.config) as f:
        config = yaml.safe_load(f)

    s3 = argparse.Namespace()

    for k, v in config.get('s3', {}).iteritems():
        conn_kwargs = dict(
            calling_format=boto.s3.connection.OrdinaryCallingFormat(),
            )
        host = boto.config.get('Boto', 's3_host')
        if host is not None:
            conn_kwargs['host'] = host
        port = boto.config.getint('Boto', 's3_port')
        if port is not None:
            conn_kwargs['port'] = port
        conn = boto.s3.connection.S3Connection(**conn_kwargs)
        setattr(s3, k, conn)

    readline.parse_and_bind('tab: complete')
    code.interact(
        banner=('Botosh: use s3 to access the Boto connections, '
                + 'press control-D to exit...'),
        local=dict(
            s3=s3,
            args=args,
            config=config,
            ),
        )
