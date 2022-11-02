#!/usr/bin/python
import json
import subprocess

charmcraft upload ./cinder-databunny-driver.charm
charmcraft release cinder-databunny-driver -r 4 -c stable