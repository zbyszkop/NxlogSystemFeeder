'''
Created on 16 wrz 2014

@author: zbyszko
'''
from CommandExecuter import CommandExecuter
from subprocess import check_output
import json
from string import split


class UptimeExecuter(CommandExecuter):
    '''
    classdocs
    '''


    def get_json_output(self):
        uptime_out = check_output("uptime", shell=False)
        raw_uptime = split(uptime_out)
        return json.dumps({"uptime":
                    {"1m": raw_uptime[7][:-1].replace(",","."),
                     "5m": raw_uptime[8][:-1].replace(",","."),
                     "15m": raw_uptime[9].replace(",","."),
                     }
                    })


print UptimeExecuter().get_json_output()