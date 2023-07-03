#!/usr/bin/python3
"""
Command Interpreter Console
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

def do_quit(self, arg):
    """Quit the command to exit the program\n"""
    return True

def do_EOF(self, arg):
    """EOF command to exit the program\n"""
    return True

def do_create(self, arg):
    """
    Create a new Instance of the Base Model,
    Saves it to a JSON File and print the ID
    """
    if not arg:
        print('** class name missing **')
        return
    
    args = arg.split()
    if args[0] not in self.valid_cls:
        print("** class doesn't exist **")
        return

    obj = eval(args[0])()
    obj.save()
    print(obj.id)

def do_show(self, arg):
        """Print the string representation of an instance
        based on the class name and id\n"""
        if not arg:
            print("** class name missing **")
            return

        li_arg = arg.split()
        try:
            model = storage.all()[f"{li_arg[0]}.{li_arg[1]}"]
            print(model)
        except KeyError:
            print("** no instance found **")
        except IndexError:
            if li_arg[0] not in self.valid_cls:
                print("** class doesn't exist **")
            elif len(li_arg) == 1:
                print("** instance id missing **")
            else:
                print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
