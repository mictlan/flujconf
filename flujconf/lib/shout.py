#twist and shout
from interface import menu
from app import darkice
import file
import os, sys
from time import sleep
import data
## example to use popen to get a pid or any other output
## pid = popen("pgrep jackd")
## pid = pid.read().strip('\n')

class shout(object):
    """menu, binary: (darkice, mpd, etc), start, stop, restart, config. if config is specified we build a configuration from it. if not we use defaults."""
    
    def __init__(self, configfile='/home/radio/.darkice.cfg'):
        self.cpath = '/home/radio/.darkice.cfg'
        if configfile == '':
            self.configfile = '/home/radio/.darkice.cfg'
        else:
            self.configfile = configfile
        self.defaults = {'icecast2-0': {'bitrateMode':'vbr','format':'vorbis','quality':'0.1','server':'localhost','port': '8000', 'password': 'hackme', 'mountPoint': 'flujos.ogg'},'input': {'device': 'jack', 'sampleRate': '44100', 'channel':'2','bitsPerSample':'16'}, 'general':{'duration': '0', 'bufferSecs':'5','reconnect':'yes'}}
        if self.get_data(configfile) == None:
            self.config = self.defaults
        else: 
            #self.data = self.get_data(configfile)
            #self.config = self.data.config
            self.config = self.get_data(configfile)
        self.basic_opts = ['server', 'port', 'password', 'mountPoint']

    def get_data(self, fname):
        if file.exists(fname) == 1:
            cfg = file.read(fname)
            return data.build_config(cfg)
        else:
            print "Utilizando configuracion predeterminado"
            return  None 

    def start(self):
        """how does shout start up. first configuration (if not supplied). tests and checks. then finally starts"""
        #os.system('clear')
        msg = """
esos son los elementos basicos para trasmitir.
si estas contento con el configuracion puedes empezar 
a transmitir teclando <intro>. sino pues cambiar el opcion eligiendo su 
numero."""
        options = []
        for i in self.basic_opts:
            ice = self.config['icecast2-0']
            if ice.has_key(i):
                options.append((i, ice[i]))
        from interface import menu
        footer =  """
P) Regresar todos los campos a valores (P)redeterminados
O) Otras (O)pciones 
S) (S)alir"
intro|enter) Iniciar transmission
______________________"""
        bmenu = menu(options, 'configuration', msg, footer)
        opt = bmenu.display()
        if opt == 'S':
            bmenu.bye_bye()
        elif opt == 'O':
            self.options_menu()
        elif opt == 'P':
            self.config = self.defaults
            self.start()
        elif opt == '':
            file.write(self.config, self.cpath)
            if not self.get_depends():
                self.start_app('darkice') 
            else:
                os.system('clear')
                print 'dependencias'
                for d in self.get_depends():
                    print 'nuestra configuracion depende de: %s' % d
                    print 'vamos asegurar que estan corriendo %s' % d
                    if self.is_not_running(d):
                        print """
%s no esta corriendo, intentaremos arrancarlo
en el caso de alguna falla intenta reiniciarlo manualmente""" % d
                        if d == 'jackd':
                            os.system('jack.ctl stop')
                            os.system('jack.ctl start')
                            sleep(2)
                        elif d == 'icecast2':
                            os.system('sudo /etc/init.d/icecast2 restart')
                            sleep(2)
                        self.start()
                    else: 
                        print "%s esta corriendo, avanzando" % d
                self.start_app('darkice')
                self.start()
           
 
        else:
            self.catch_options(options, opt) 
            self.start()            
   
    def options_menu(self):
        footer = """
S) (S)alir"                                
intro|enter) Volver a Menu Anterior 
 ______________________"""
        msg = ''
        title = 'Opciones'
        options = ['Editar Configuracion Manualmente','Leer Manual de Configuracion de darkice', 'Manejar Musica']
        #moptions = self.get_more_options()
        amenu = menu(options, title, msg, footer)
        opt = amenu.display()
        if opt == '':
            self.start()
        elif opt == '1':
            cmd = 'nano %s' % self.configfile
            os.system(cmd)
            self.options_menu()
        elif opt == '2':
            cmd = 'man darkice.cfg' 
            os.system(cmd)
            self.options_menu()
        elif opt == '3':
            cmd = 'ncmpc' 
            os.system(cmd)
            self.options_menu()
        if opt == 'S':
            amenu.bye_bye()
 
    def catch_options(self, options, opt):
        opt = int(opt)-1
        if type(options[opt]) == type(()):
            key = options[opt][0]
            msg = 'entra nuevo valor de %s: ' % key 
            self.config['icecast2-0'][key] = raw_input(msg) 
        elif type(options[opt]) == type('s'):
            msg = 'entra nuevo valor de %s: ' % options[opt] 
            self.config['icecast2-0'][options[opt]] = raw_input(msg)
            

    def is_not_running(self, app):
        """is application running"""
        a = os.system("pgrep %s" % app)
        return a

    def start_app(self, binary):
        """choose which app to start and call app.start() app class should have a start, stop, pre_start, post_stop functions and app.pid attribute"""
        if binary == 'mpd':
            app = mpd()
        elif binary == 'darkice':
            app = darkice(self.configfile)
        else: 
            print "unknown app"
            sys.exit()
        app.start() 
        
    def stop_app(self, binary):
        cmd = 'killall %s' % binary
        os.system(cmd)
    
    def get_servers(self):
        """get one or more servers from cfg and return list"""
        servers = []
        for i in self.config:
            if 'cast' in i:
                servers.append(self.config[i]['server'])
        return servers
 
    def get_depends(self):
        config = self.config
        depends = []
        device = config['input']['device']
        if device == 'jack':
            depends.append('jackd')
        servers = self.get_servers()
        for server in servers:
            if server == 'localhost':
                depends.append('icecast2')
        return depends

   # def get_more_options():
   #     opts = []
   #     opts.append(('abrir reproducor de musica',''))
