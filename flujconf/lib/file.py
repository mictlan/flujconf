#file reading and writing


def exists(f):
    try:
        file = open(f)
    except IOError:
        exists = 0
    else:
        exists = 1
    return exists

def read(file):
    """read config from file, retrun a list"""
    config = []
    f = open(file, 'r')
    for line in f.readlines():
        line = line.strip('\n')
        sline = line.strip()
        if not sline or sline.startswith('#'): continue
        if not line.strip():
            continue
        if line.startswith('#'):
            continue
        #if i != '':
        config.append(line) 
    return config

def write(data, pconf):
    """write config data to config file."""
    conf = open(pconf,'w')
    for section in data:
        s = '[%s]\n' % section
        conf.write(s)
        #conf.write('[general]')
        #for i in t.config['general']:
        for item in data[section]:
            l = "%s = %s\n" %  (item, data[section][item])
            conf.write(l)
    conf.close()
    #for i in t.config['input']:
    #    l = "%s = %s" %  (i, t.config['general'][i])
        
    conf.close()
