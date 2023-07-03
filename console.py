#!/usr/bin/python3
"""
Command Interpreter Console
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

if __name__ == '__main__':
    HBNBCommand().cmdloop()