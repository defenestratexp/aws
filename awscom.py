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
  for item in myset:
    print item.split()

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
  #Iterate through the line items for the string that denotes this is the line containg the instance-id information
  for item in myset:
    searchstr = 'INSTANCES'
    if searchstr in item:
      targetlist = item.split()
      myinstanceid = targetlist[7]
  #mytargetline = re.sub(r'\s+', ' ', myset[2])
  #mytargetlist = mytargetline.split()
  #myinstanceid = mytargetlist[7]
  return myinstanceid
  
# Function to obtain the instance name
def getname(private_ip):

  #Obtain instance id
  myinstanceid = getid(private_ip)

  #Command setup
  LOCAL_AWS = 'aws'
  LOCAL_AWS_SERVICE = 'ec2'
  LOCAL_AWS_ARG1 = 'describe-instances'
  DRYRUN = '--dry-run'
  LOCAL_AWS_ARG2 = '--filters'
  LOCAL_AWS_ARG3 = 'Name=private-ip-address,Values=%s' % private_ip

  #Command execution
  procout = subprocess.Popen([LOCAL_AWS, LOCAL_AWS_SERVICE, LOCAL_AWS_ARG1, LOCAL_AWS_ARG2, LOCAL_AWS_ARG3],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  myset = list(procout.stdout)
  
  #Iterate through the line items for the string that denotes this is the line contating the name information
  for item in myset:
    searchstr = 'Name'
    if searchstr in item:
      targetlist = item.split()
      myinstancename = targetlist[2]
  return myinstancename

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
