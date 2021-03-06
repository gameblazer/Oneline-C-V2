#Oneline V2
#  @author Nadir Hamid
#  @license MIT


#import bson
import json
import os
import re
import ast
ONELINE_SETTINGS = dict(
   root_dir="/usr/local/onelinev2/"
)

def parse(message):
  return parse_v2( message )
def pack(message):
   return pack_v2( message )

def parse_v1(message):
  if isinstance(message,str):
    literal = ast.literal_eval(message.__str__())
    return bson.loads(bytearray(literal).__str__())
  return message
def pack_v1(message):
  if isinstance(message,dict):
    bytes = map(ord, bson.dumps(message)).__str__()
    return bytes
  return message

def parse_v2(message):
  return json.loads( message )
def pack_v2(message):
  return json.dumps( message )

 



def parse_config(object_given):
  class_name = object_given.__class__  
  file_name = "/usr/local/onelinev2/conf/{0}.{1}".format(class_name, "conf")
  config_dict = {}
  if os.path.isfile(file_name):
      file = open(file_name, "r+")
      for i in file.readlines():
          token= i.split("=")
          if len(token)>0:
             key = trim_key(token[0])
             value = trim_value(token[1])
             config_dict[key]=value
      file.close()
  return config_dict
            
             

def trim_key(value):      
  return re.sub("^\s+|\s+$", "", value)
def trim_value(value):
  return re.sub("^\"|\"$", re.sub("^\s+|\s+$", "", value))




## by default all communication is singular
def singular(message):
  jsonmsg=json.dumps(message)
  return ["singular",jsonmsg]
## multicast a message
## this just needs to add the multicast = 1 flag which will
## tell the Oneline server to send to all
## people listening on this module
def multicast(message):
  jsonmsg=json.dumps(message)
  return ["multicast",jsonmsg]
   


## basics for getting configurations
## and  other things 
class Oneline_V2_Util(object):
  # OnelineV2 module configs are json based
  # @param  module_name the name of the module
  @staticmethod
  def get_config(module_name):
    full_name="{0}/{1}.conf".format(ONELINE['root_dir'], "conf/"+ module_name)
    if os.path.isfile( full_name ):
      file = json.loads(open( ONELINE_SETTINGS['root_dir'] + "/conf/{0}.conf".format(module_name ).read()) )
      return file
    return dict()

class Oneline(object):
  ## parse and pack a BSON
  ## message
  ## @paramany message, dict based
  @staticmethod
  def pack( dict ):
      return oneline_pack_message(dict)
  @staticmethod
  ## parse a BSON message
  ## @param msg raw  BSON msg
  def parse( msg ):
      return oneline_parse_message( msg )
  ## run the pipeline
  ## @param module  to be used
  @staticmethod 
  def run( msg ):
      return msg







