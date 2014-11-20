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
  #myinstanceid = getid(private_ip)

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

# Function to get the machine state
def getstate(private_ip):

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

  #Iterate through line items
  for item in myset:
    searchstr = 'STATE'
    if searchstr in item:
      targetlist = item.split()
      myinstancestate = targetlist[2]
  return myinstancestate

# Function to get the automate version from tag/metadata
def getversion(private_ip):
  
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

  #Iterate through the line items
  for item in myset:
    searchstr = 'TAGS'
    if searchstr in item:
      searchstr2 = 'Version'
      if searchstr2 in item:
        targetlist = item.split()
        mysoftwareversion = targetlist[2]
  return mysoftwareversion

#Function to get the zoo from the tag metadata
def getzoo(private_ip):

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

  #Iterate through the line items
  for item in myset:
    searchstr = 'TAGS'
    if searchstr in item:
      searchstr2 = 'Zoo'
      if searchstr2 in item:
        targetlist = item.split()
        myzooname = targetlist[2]

  return myzooname

#Function to get the Environment from the tag metadata
def getenv(private_ip):

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

  #Iterate through the line items
  for item in myset:
    searchstr = 'TAGS'
    if searchstr in item:
      searchstr2 = 'Environment'
      if searchstr2 in item:
        targetlist = item.split()
        myenvname = targetlist[2]

  return myenvname

#Function to disable the api-termination flag
def termflagbyip(private_ip):

  #Get the instance-id
  TARGETHOSTID = getid(private_ip)

  #Command setup
  LOCAL_AWS = 'aws'
  LOCAL_AWS_SERVICE = 'ec2'
  LOCAL_AWS_ARG1 = 'modify-instance-attribute'
  DRYRUN = '--dry-run'
  LOCAL_AWS_ARG2 = '--instance-id'
  LOCAL_AWS_ARG3 = '--disable-api-termination'
  LOCAL_AWS_ARG4 = "{\"Value\": false}"
 
  #Command Execution 
  subprocess.call([LOCAL_AWS, LOCAL_AWS_SERVICE, LOCAL_AWS_ARG1, LOCAL_AWS_ARG2, TARGETHOSTID, LOCAL_AWS_ARG3, LOCAL_AWS_ARG4])
 
#Function to disable the api-termination flag by instance-id
def termflagbyid(instanceid) 

  #Command setup
  LOCAL_AWS = 'aws'
  LOCAL_AWS_SERVICE = 'ec2'
  LOCAL_AWS_ARG1 = 'modify-instance-attribute'
  DRYRUN = '--dry-run'
  LOCAL_AWS_ARG3 = '--disable-api-termination'
  LOCAL_AWS_ARG4 = "{\"Value\": false}"
 
  #Command Execution 
  subprocess.call([LOCAL_AWS, LOCAL_AWS_SERVICE, LOCAL_AWS_ARG1, instanceid, TARGETHOSTID, LOCAL_AWS_ARG3, LOCAL_AWS_ARG4])

#Function to terminate an instance identified by its instance-id
def termbyid(instanceid):

  #Enable api-termination by setting the flag to false
  termflagbyid(instanceid)

  #Command setup
  LOCAL_AWS = 'aws'
  LOCAL_AWS_SERVICE = 'ec2'
  LOCAL_AWS_ARG1 = 'terminate-instances'
  DRYRUN = '--dry-run'
  LOCAL_AWS_ARG2 = '--instance-ids'
  LOCAL_AWS_IDLIST = instanceid

  #Command execution
  subprocess.call([LOCAL_AWS, LOCAL_AWS_SERVICE, LOCAL_AWS_ARG1, LOCAL_AWS_ARG2, LOCAL_AWS_IDLIST])

#Function to terminate an instance identified by its private ip address
def termbyip(private_ip):
 
  #Retrieve instance-id
  mytargetid = getid(private_ip) 

  #Enable api-termination flag
  termflagbyid(mytargetid)

  #Pass host to termbyid
  termbyid(mytargetid)

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
