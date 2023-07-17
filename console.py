#!/usr/bin/python3
'''commandline interpreter for interface'''
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    '''command interpreter that inherits
    from cmd.Cmd module'''

    prompt = '(hbnb) '

    class_dict = {
            'Amenity': Amenity, 'BaseModel': BaseModel,
            'City': City, 'Place': Place, 'Review': Review,
            'State': State, 'User': User
            }

    def do_quit(self, line):
        '''quits the session'''
        return True

    def do_EOF(self, line):
        '''handle Ctrl-D(EOF)'''
        print()
        return True

    def emptyline(self):
        '''handles empty line'''
        pass

    def do_create(self, line):
        ''' Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.'''
        if line:
            line = line.split()[0]
            if line in self.class_dict.keys():
                new_instance = self.class_dict[line]()
                print('{}'.format(new_instance.id))
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
        '''Prints the instance of a class'''
        if line:
            line = line.split()
            if len(line) > 0:
                if line[0] not in self.class_dict.keys():
                    print('** class doesn\'t exist **')
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
           print(' ** class name missing **')

    def help_show(self):
        '''help statement for show command'''
        help_txt = ['Prints the string representation of',
                'an instance based on the class name and id']
        help_txt = ' '.join(help_txt)
        print('{}'.format(help_txt))

    def do_destroy(self, line):
        '''destroy the instance of a class'''
        if line:
            line = line.split()
            if len(line) > 0:
                if line[0] not in self.class_dict.keys():
                    print('** class doesn\'t exist **')
                if len(line) < 2:
                    print('** instance id missing **')
                    return

            all_obj = storage.all()
            obj_key = f'{line[0]}.{line[1]}'
            if obj_key in all_obj.keys():
                del all_obj[obj_key]
                storage.save()
            else :
                print('** no instance found **')                
        else:
           print(' ** class name missing **')
    
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
        '''prints instances of class'''

        all_obj = storage.all()
        obj_list = []
        if line:
            line = line.split()
            if line[0] in self.class_dict.keys():
                for key in all_obj.keys():
                    if line[0] in key:
                        obj_list.append(all_obj[key])
            else:
                print('** class doesn\'t exist **')
        else:
            for key in all_obj.keys():
                obj_list.append(all_obj[key])
        print('{}'.format(all_obj))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
