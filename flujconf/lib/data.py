#data parsing 

    #sections = self.get_sections()
    #def __init__(self):
        #self.flist = flist
        #self.config = self.build_config()

def get_value(var):
    """return data as dict, or a single variable. if varibable is a section name, returns all varbiables in that section""" 
    data = ()
    for section in sections:
        if section[var]:
            data = (section, section[var])
    return data
 
def put(var, val):
    """save data"""

def write(fname):
    """write data to file"""

def is_section(name):
    """return true if name is section (general, input, etc)"""


def build_section(name, flist):
    """rebuild a section as a dictionary with a list of elements as value"""
    section = {}
    item = {}
    if not name[0] == '[' and not name[-1] == ']':
        name = '[%s]' % name
    if name in flist:
        index = flist.index(name) 
        index = index+1
        for i in flist[index:]:
            if not i[0] == '[' and not i[-1] == ']':
                cols = i.split()
                #var, val = i.split('=') 
                var, val = cols[0], cols[2]
                var, val = var.strip(), val.strip()
                item[var] = val
            else: 
                break
        name = name.strip('[')
        name = name.strip(']')
        section[name] = item
    return section

def build_config(flist):
    """the whole config as a dict"""
    cfg = {}
    for name in get_sections(flist):
        section = build_section(name, flist)
        cfg[name] = section[name]
    return cfg        

def get_sections(flist):
    """return a list of sections in cfg (general, input, etc)"""
    sections = []
    for i in flist:
        if not i[0] == '[' and not i[-1] == ']': 
            pass
        else:
           i = i.strip(']')
           i = i.strip('[')
           sections.append(i)
    return sections 

def get_servers(sections):
    """get one or more servers from cfg and return list"""
    servers = []
    for i in sections: 
        if 'cast' in i:
            servers.append(i)
    return servers

    
