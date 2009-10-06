#apps that we need to start. they have start, stop, pre_start, post_stop functions as well as a pid and dependecy attibutes. 
import shout
import os
class app(object):
    
    def __init__(self):
        #depends = [] #darkice(app), for example will fill this
        self.pid = ''
        self.startupcmd = ''
        self.shutdowncmd = 'kill -9 %s' % self.pid
        #config = '' #most apps will have a config file

    def start(self):
        """start app, saving its pid file in attribute"""
        #pre_start(depends)
        pid = os.system(self.startupcmd) #this command should also return a pid
        self.pid = pid

    def stop(self, shutdowncmd):
        """stop app"""
        pid = self.pid
        os.system(shutdowncmd)
        post_stop()

    def restart(self):
        """restart"""
        self.stop()
        self.start()

    def pre_start(self, depends):
        for d in depends:
            if not d.is_running():
                print """we have a dependency on %s but it is not running
                         starting %s""" % (d.name, d.name)
                d.startupcmd() #assumimos that d is instance of app class
            else: 
                print "depedencies check out for %s, skipping" % d.name

    def post_stop(self):
        """asegurar que si arranco"""
        pass
        
class darkice(app):

    def __init__(self, config):
        self.config = config
        self.startupcmd = 'darkice -c %s' % config

