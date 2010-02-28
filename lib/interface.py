#user interaction
import sys, os

class menu(object):
    """general menu class. basic or extedended menus. you can describe and give a title to the menu"""
    def __init__(self, options, title='', desc='', footer=''):
        self.options = options
        self.title = title
        self.desc = desc
        self.footer = footer
#        shout = shout()  this doesnt get called here but rather subclasses the menu and uses its options. 
#        self.config_data = shout['data']

    def print_title(self):
        title = self.title
        print "| %s |" % title
   #     n = len(title)+2
   #     print " "+ "-"*n
        print self.desc

    def print_options(self):
        options = self.options
        for i in options:
            index = options.index(i)
            index = index+1
            if type(i) == type(()):
                print "%s) %s [%s]: " % (index, i[0], i[1]) 
            elif type(i) == type('s'):
                print "%s) %s: " % (index, i)
            else: 
                print 'unknow type in options'
                sys.exit()
        print self.footer

    def display(self):
        """format and print menu"""
        os.system('clear')
        self.print_title() 
        print ""
        self.print_options()
        opt = self.user_prompt()
        return opt

    def user_prompt(self):
        msg = ''
        for i in self.options:
            index = self.options.index(i)
            index = index+1
            msg = msg+"|%s" % index 
        msg = msg+"|O|S|intro|: "
        opt = raw_input(msg)       
        return opt
    
    def bye_bye(self):
        os.system('clear')
        print """


                                        besitos, bye

                    """ 
        sys.exit()

class general_menu(menu):

    def menu(self):
        os.system('clear')
        print """  CONFIGURACION DE BIBLIOTECA DE AUDIO [MPD]


                1) validar biblioteca de musica
                2) actualizar biblioteca de musica
                3) reinicar daemon de musica
                4) control de musica
                S) salir
                """

        val = raw_input('[1|2|3|4|S]: ')
        if val == '1':
            print ""
            dir = raw_input('ruta a la biblioteca de audio [%s]: ' % self.library)
            self.correct_perms(dir)
            self.menu()
        if val == '2':
            print ""
            print "puede que tarda"
            self.update_db()
            self.menu()
        if val == '3':
            cmd = 'sudo /etc/init.d/jackd stop'
            os.system(cmd)
            cmd = 'sudo /etc/init.d/mpd stop'
            os.system(cmd)
            cmd = 'sudo /etc/init.d/jackd start'
            os.system(cmd)
            cmd = 'sudo /etc/init.d/mpd start'
            os.system(cmd)
            sleep(2)
            self.menu()
        if val == '4':
            cmd = 'ncmpc'
            os.system(cmd)
            self.menu()
        if val.lower() == 's':
            opciones()


    def ask_user(self, var):
        config = self.data
        val = config[var]
        msg = "%s [%s]: " % (var, val)
        userval =  raw_input(msg)
        if userval is not '':
            self.data[var] = userval
    
    def sumerize_config(self, var='all'):
        
        config = self.data
        os.system('clear')
        if var == 'all':
            print "CONFIGURACION GENERAL DE FLUJO"
            print "------------------------"
            print ""
            print "cambiar configuracion de:"
            print ""
            items = config.items()
            for i in config:
                print "[%s] %s: %s" % (items.index((i, config[i]))+1, i, config[i])
            print "------------"
            print "[S] o salir" 
            print "---------------------------"
            print "si no hay que cambiar nada, oprime [intro]"
        self.change_config_option()
    
    def change_config_option(self):
        val = raw_input('[1|2|3|4|5|S|intro]: ')        
        print ""
        ask = self.ask_user 
        if val == '3':
            ask('mount')
        elif val == '1':
            ask('passwd')
        elif val == '4': 
            ask('port')
        elif val == '5':
            ask('server')
        elif val == '2':
           ask('device') 
        elif val == 'S':
            self.bye_bye()
        elif val == "":    
            config = self.data
            self.writeconf()
            opciones() 
        self.writeconf()
        self.sumerize_config() 


    def config(self, set='basic'):
        b_c = ['server', 'port', 'mount', 'passwd', 'device']
        e_c = ['bitrateMode', 'format', 'quality', 'name', 'description', 'url', 'genre']
        if menu_set == 'basic':
            options = b_c
        elif menu_set == 'extended':
            all = b_c
        for i in e_c:
            all.append(i)
        return all

#class depends(object):

     
