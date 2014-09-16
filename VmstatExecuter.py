'''
Created on 16 wrz 2014

@author: zbyszko



'''
from CommandExecuter import CommandExecuter
from subprocess import check_output
import json
from string import split
import time


class VmstatExecuter(CommandExecuter):
    '''
    Class for vmstat data
    '''

    def to_vmstat_object(self, data_raw):
        data = map(int, data_raw)
        return {"timestamp" : int(time.time() * 1000),
                "proc":{"r":data[0], "b":data[1]},
            "memory":
            {"swpd":data[2],
                "free":data[3],
                "buff":data[4],
                "cache":data[5]},
            "swap":
            {"si":data[6],
                "so":data[7]},
            "io":
            {"bi":data[8],
                "bo":data[9]},
            "system":
            {"in":data[10],
                "cs":data[11]},
            "cpu":
            {"us":data[12], "sy":data[13], "id":data[14], "wa":data[15], "st":data[16]}}


    def get_json_output(self):
        vmstat_out = check_output("vmstat", shell=False)
        data = split(split(vmstat_out, "\n")[2])
        return json.dumps(self.to_vmstat_object(data))




print VmstatExecuter().get_json_output()