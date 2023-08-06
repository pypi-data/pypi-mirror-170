import os

import click

from . import launchable
from ..utils.file_name_pattern import jvm_test_pattern


@click.option('--bare',
              help='outputs class names alone',
              default=False,
              is_flag=True
              )
@click.argument('source_roots', required=True, nargs=-1)
@launchable.subset
def subset(client, bare, source_roots):
    def file2test(f: str):
        if jvm_test_pattern.match(f):
            f = f[:f.rindex('.')]   # remove extension
            # directory -> package name conversion
            cls_name = f.replace(os.path.sep, '.')
            return [{"type": "class", "name": cls_name}]
        else:
            return None

    for root in source_roots:
        client.scan(root, '**/*', file2test)

    def exclusion_output_handler(subset_tests, rest_tests, is_observation):
        if is_observation:
            rest_tests = []
        if client.rest:
            with open(client.rest, "w+", encoding="utf-8") as fp:
                if not bare and len(rest_tests) == 0:
                    # This prevents the CLI output to be evaled as an empty
                    # string argument.
                    fp.write('-PdummyPlaceHolder')
                else:
                    fp.write(client.separator.join(client.formatter(t)
                             for t in rest_tests))

        classes = [to_class_file(tp[0]['name']) for tp in rest_tests]
        if bare:
            click.echo(','.join(classes))
        else:
            click.echo('-PexcludeTests=' + (','.join(classes)))
    client.exclusion_output_handler = exclusion_output_handler

    if bare:
        client.formatter = lambda x: x[0]['name']
    else:
        client.formatter = lambda x: "--tests {}".format(x[0]['name'])
        client.separator = ' '

    client.run()


@click.option('--bare',
              help='outputs class names alone',
              default=False,
              is_flag=True
              )
@launchable.split_subset
def split_subset(client, bare):
    if bare:
        client.formatter = lambda x: x[0]['name']
    else:
        client.formatter = lambda x: "--tests {}".format(x[0]['name'])
        client.separator = ' '

    client.run()


def to_class_file(class_name: str):
    return class_name.replace('.', '/') + '.class'


record_tests = launchable.CommonRecordTestImpls(__name__).report_files()
