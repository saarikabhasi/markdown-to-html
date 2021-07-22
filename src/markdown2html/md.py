#!/usr/bin/env
import argparse
from . import markdown as md

def markdown(value=None):
   md_object = md.markdown(value)
   return md_object.markdown_parser()

def main():
   parser =argparse.ArgumentParser('Input a file')
   parser.add_argument('-f',type=argparse.FileType('r'))
   args = parser.parse_args()

   if args.f:
      print(markdown(value=args.f.read())) 




    



    
    
    


    



