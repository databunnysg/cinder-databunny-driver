#!/usr/bin/python
import json
import subprocess
processresult = subprocess.run("charmcraft status cinder-databunny-driver --format json", shell=True,capture_output=True, text=True)
outputjson = json.loads(processresult.stdout)
lastrevision = outputjson[0]['mappings'][0]['releases'][0]['revision']
print("last revision:"+str(lastrevision)+"\n")
processresult = subprocess.run(
    "charmcraft upload ./cinder-databunny-driver.charm" 
    , shell=True,capture_output=True, text=True)
print(processresult.stdout)
processresult = subprocess.run(
    "charmcraft release cinder-databunny-driver -c stable -r " +
    str(int(lastrevision)+1)
    , shell=True,capture_output=True, text=True)

print(processresult.stdout)