#!/usr/bin/env python

#python wrappers for aws cli operations

##########################
#### IMPORT LIBRARIES ####
##########################

import subprocess
import os
import re
#############################
#### END LIBRARY IMPORTS ####
#############################

##############################
#### FUNCTION DEFINITIONS ####
##############################

# Function to obtain all instance information
def getall(private_ip):
  
  #Command setup
  LOCAL_AWS = 'aws'
  LOCAL_AWS_SERVICE = 'ec2'
  LOCAL_AWS_ARG1 = 'describe-instances'
  DRYRUN = '--dry-run'
  LOCAL_AWS_ARG2 = '--filters'
  LOCAL_AWS_ARG3 = 'Name=private-ip-address,Values=%s' % private_ip
 
  #Command execution
  procout = subprocess.Popen([LOCAL_AWS, LOCAL_AWS_SERVICE, LOCAL_AWS_ARG1, LOCAL_AWS_ARG2, LOCAL_AWS_ARG3],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  myset=list(procout.stdout)
  print myset

# Function to obtain an instance-id
def getid(private_ip):

  #Command setup
  LOCAL_AWS = 'aws'
  LOCAL_AWS_SERVICE = 'ec2'
  LOCAL_AWS_ARG1 = 'describe-instances'
  DRYRUN = '--dry-run'
  LOCAL_AWS_ARG2 = '--filters'
  LOCAL_AWS_ARG3 = 'Name=private-ip-address,Values=%s' % private_ip

  #Command execution
  procout = subprocess.Popen([LOCAL_AWS, LOCAL_AWS_SERVICE, LOCAL_AWS_ARG1, LOCAL_AWS_ARG2, LOCAL_AWS_ARG3],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  myset=list(procout.stdout)
  mytargetline = re.sub(r'\s+', ' ', myset[2])
  mytargetlist = mytargetline.split()
  myinstanceid = mytargetlist[7]
  return myinstanceid
  


##########################
#### END FUNCTON DEFS ####
##########################

##############
#### MAIN ####
##############

def main():
  print "Main function"

if __name__ == "__main__":
  main()
