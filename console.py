#!/usr/bin/python3
'''
module that contains the entry point of the command
interpreter
'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''command interpreter that inherits
    from cmd.Cmd module'''

    prompt = '(hbnb) '
    class_dict = {'BaseModel': BaseModel}

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''handles ctrl-D ( EOF)

        Args:
            line (str): arguements to the command

        Return:
            Always return True to quit shell
        '''
        print()
        return True

    def emptyline(self):
        '''
        making sure the intepreter does nothing
        by overidinng the method
        '''
        pass

    def do_create(self, line):
        ''' Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.

        Args:
            line (str): argumnent(s) to the function.
        '''
        if line:
            line = line.split()[0]
            if line in self.class_dict.keys():
                new_instance = self.class_dict[line]()
                print('{}'.format(new_instance.id))
                new_instance.save()
            else:
                print('** class doesn\'t exist **')
        else:
            print("** class name missing **")
            return

    def help_create(self):
        '''help statement for create command'''
        help_txt = [
                'Creates a new instance of BaseModel,',
                'saves it (to the JSON file) and prints the id.',
                '\nEx: $ create BaseModel'
                ]
        help_txt = ' '.join(help_txt)
        print('{}'.format(help_txt))

    def do_show(self, line):
        '''Prints the instance of a class

        Args:
            line (str): argumnent(s) to the function.
        '''
        if line:
            line = line.split()
            if line[0] in self.class_dict.keys():
                if len(line) < 2:
                    print('** instance id missing **')
                    return

                all_obj = storage.all()
                obj_key = f'{line[0]}.{line[1]}'
                if obj_key in all_obj.keys():
                    print('{}'.format(all_obj[obj_key]))
                else:
                    print('** no instance found **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def help_show(self):
        '''help statement for show command'''
        help_txt = ['Prints the string representation of',
                    'an instance based on the class name and id']
        help_txt = ' '.join(help_txt)
        print('{}'.format(help_txt))

    def do_destroy(self, line):
        '''destroy the instance of a class

        Args:
            line (str): argumnent(s) to the function.
        '''
        if line:
            line = line.split()
            if line[0] in self.class_dict.keys():
                if len(line) < 2:
                    print('** instance id missing **')
                    return

                all_obj = storage.all()
                obj_key = f'{line[0]}.{line[1]}'
                if obj_key in all_obj.keys():
                    del all_obj[obj_key]
                    storage.save()
                else:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')

    def help_destroy(self):
        '''help statement for destroy command'''
        help_txt = [
                'Deletes an instance based on the class',
                'name and id (save the change into the JSON file).',
                '\nEx: $ destroy BaseModel 1234-1234-1234.'
                ]
        help_txt = ' '.join(help_txt)
        print(help_txt)

    def do_all(self, line):
        '''prints instances of class

        Args:
            line (str): argumnent(s) to the function.
        '''
        if line:
            line = line.split()
            if line[0] in self.class_dict.keys():
                dict_all = storage.all()
                list_all = []
                for k in dict_all.keys():
                    if line[0] in k:
                        list_all.append(str(dict_all[k]))
            else:
                print('** class doesn\'t exist **')
        else:
            dict_all = storage.all()
            list_all = []
            for k in dict_all.keys():
                list_all.append(str(dict_all[k]))
        print(list_all)

    def check_type(self, value):
        try:
            value = int(value)
            return value
            print('called')
        except ValueError:
            pass

        try:
            value = float(value)
            return value
        except ValueError:
            pass

        try:
            value = str(value)
            return value
        except ValueError:
            pass
        return ''

    def do_update(self, line):
        '''implement the update command'''
        if line:
            line = line.split()
            if line[0] in self.class_dict.keys():
                if len(line) < 2:
                    print('** instance id missing **')
                    return
                all_obj = storage.all()
                obj_key = f'{line[0]}.{line[1]}'
                if obj_key in all_obj.keys():
                    if len(line) < 3:
                        print('** attribute name missing **')
                        return
                    elif len(line) < 4:
                        print('** value missing **')
                        return

                    value = self.check_type(line[3])
                    builtins = ['id', 'created_at', 'updated_at']
                    if (value != '') and line[2] not in builtins:
                        setattr(all_obj[obj_key], str(line[2]), value)
                        all_obj[obj_key].save()

                else:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()

'''    class_dict = {
            'Amenity': Amenity, 'BaseModel': BaseModel,
            'City': City, 'Place': Place, 'Review': Review,
            'State': State, 'User': User
            }
'''
