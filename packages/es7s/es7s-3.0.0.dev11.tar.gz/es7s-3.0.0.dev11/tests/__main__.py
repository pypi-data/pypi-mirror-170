#!/usr/bin/env python
# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

import unittest


def main():
    loader = unittest.TestLoader()
    start_dir = "tests"
    suite = loader.discover(start_dir)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
