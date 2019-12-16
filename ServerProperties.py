class ServerProperties(object):
    """docstring for ServerProperties."""

    def __init__(self, filename):
        super(ServerProperties, self).__init__()
        self.filename = filename
        self.serverName = ""
        self.gamemodeValues = ['survival', 'creative', 'adventure']
        self.difficulty = ['peaceful', 'easy', 'normal', 'hard']
        self.serverPortValues = range(1, 65536)
        self.serverPortv6Values = range(1, 65536)
        self.defaultPlayerPermissionLevelValues = ['visitor', 'member', 'operator']
        self.tickDistanceValues = range(4, 13)

    def validate(self):
        inFile = open(self.filename, 'r')
        errors = []
        for l in inFile:
            clean = l.strip()
            if ( len(clean) >= 1) :
                if ( clean[0] != "#" ):
                    name, value = clean.split("=")
                    value = value.strip()
                    if ( name == 'server-name' ):
                        if ( len(value) > 0):
                            self.serverName = value
                        else:
                            errors.append('server-name')

                    elif ( name == 'gamemode' ):
                        if ( value not in self.gamemodeValues ):
                            errors.append('gamemode')

                    elif ( name == 'difficulty' ):
                        if ( value not in self.difficulty):
                            errors.append('difficulty')

                    elif ( name == 'allow-cheats' ):
                        try:
                            b = bool(value)
                        except:
                            errors.append('allow-cheats')

                    elif ( name == 'max-players' ):
                        try:
                            i = int(value)
                            if ( i <= 0 ):
                                errors.append('max-players')
                        except:
                            errors.append('max-players')

                    elif ( name == 'online-mode' ):
                        try:
                            b = bool(value)
                        except:
                            errors.append('online-mode')

                    elif ( name == 'white-list' ):
                        try:
                            b = bool(value)
                        except:
                            errors.append('white-list')

                    elif ( name == 'server-port' ):
                        try:
                            i = int(value)
                            if ( i not in self.serverPortValues):
                                errors.append('server-port')
                        except:
                            errors.append('server-port')

                    elif ( name == 'server-portv6' ):
                        try:
                            i = int(value)
                            if ( i not in self.serverPortv6Values):
                                errors.append('server-portv6')
                        except:
                            errors.append('server-portv6')

                    elif ( name == 'view-distance' ):
                        try:
                            i = int(value)
                            if ( i <= 0 ):
                                errors.append('view-distance')
                        except:
                            errors.append('view-distance')

                    elif ( name == 'tick-distance' ):
                        try:
                            i = int(value)
                            if ( i not in self.tickDistanceValues ):
                                errors.append('tick-distance')
                        except:
                            errors.append('tick-distance')

                    elif ( name == 'player-idle-timeout' ):
                        try:
                            i = int(value)
                            if ( i < 0 ):
                                errors.append('player-idle-timeout')
                        except:
                            errors.append('player-idle-timeout')

                    elif ( name == 'max-threads' ):
                        try:
                            i = int(value)
                            if ( i < 0 ):
                                errors.append('max-threads')
                        except:
                            errors.append('max-threads')

                    elif ( name == 'level-name' ):
                        if ( len(value) == 0 ):
                            errors.append('level-name')

                    elif ( name == 'level-seed' ):
                        if ( 1 == 0 ):
                            errors.append('level-seed')

                    elif ( name == 'default-player-permission-level' ):
                        if ( value not in self.defaultPlayerPermissionLevelValues ):
                            errors.append('default-players-permission-level')

                    elif ( name == 'texturepack-required' ):
                        try:
                            b = bool(value)
                        except:
                            errors.append('texturepack-required')

        inFile.close()

        return errors
