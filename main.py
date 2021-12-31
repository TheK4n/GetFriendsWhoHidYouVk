# coding: utf-8
from src.utils import get_shadows_friends_ids, get_id_from_url, get_url_from_id
from sys import argv


def main(*args):
    for i in get_shadows_friends_ids(get_id_from_url(args[0])):
        print(get_url_from_id(i))


if __name__ == '__main__':
    main(*argv[1:])
