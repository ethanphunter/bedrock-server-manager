class ServerProperties(object):
    """docstring for ServerProperties."""

    def __init__(self, filename):
        super(ServerProperties, self).__init__()
        self.filename = filename
        self.serverName = ""
        self.gamemode = ""
        self.difficulty = ""
        self.allowCheats = False
        self.maxPlayers = 0
        self.onlineMode = True
        self.whiteList = False
        self.serverPort = -1
        self.serverPortv6 = -1
        self.viewDistance = 0
        self.tickDistance = 0
        self.playerIdleTimeout = 0
        self.maxThreads = 0
        self.levelName = ""
        self.levelSeed = ""
        self.defaultPlayerPermissionLevel = ""
        self.texturepackRequired = False
        self.gamemodeValues = ['survival', 'creative', 'adventure']
        self.difficultyValues = ['peaceful', 'easy', 'normal', 'hard']
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
                        else:
                            self.gamemode = value

                    elif ( name == 'difficulty' ):
                        if ( value not in self.difficultyValues):
                            errors.append('difficulty')
                        else:
                            self.difficulty = value

                    elif ( name == 'allow-cheats' ):
                        try:
                            self.allowCheats = bool(value)
                        except:
                            errors.append('allow-cheats')

                    elif ( name == 'max-players' ):
                        try:
                            i = int(value)
                            if ( i <= 0 ):
                                errors.append('max-players')
                            else:
                                self.maxPlayers = i
                        except:
                            errors.append('max-players')

                    elif ( name == 'online-mode' ):
                        try:
                            self.onlineMode = bool(value)
                        except:
                            errors.append('online-mode')

                    elif ( name == 'white-list' ):
                        try:
                            self.whiteList = bool(value)
                        except:
                            errors.append('white-list')

                    elif ( name == 'server-port' ):
                        try:
                            i = int(value)
                            if ( i not in self.serverPortValues):
                                errors.append('server-port')
                            else:
                                self.serverPort = i
                        except:
                            errors.append('server-port')

                    elif ( name == 'server-portv6' ):
                        try:
                            i = int(value)
                            if ( i not in self.serverPortv6Values):
                                errors.append('server-portv6')
                            else:
                                self.serverPortv6 = i
                        except:
                            errors.append('server-portv6')

                    elif ( name == 'view-distance' ):
                        try:
                            i = int(value)
                            if ( i <= 0 ):
                                errors.append('view-distance')
                            else:
                                self.viewDistance = i
                        except:
                            errors.append('view-distance')

                    elif ( name == 'tick-distance' ):
                        try:
                            i = int(value)
                            if ( i not in self.tickDistanceValues ):
                                errors.append('tick-distance')
                            else:
                                self.tickDistance = i
                        except:
                            errors.append('tick-distance')

                    elif ( name == 'player-idle-timeout' ):
                        try:
                            i = int(value)
                            if ( i < 0 ):
                                errors.append('player-idle-timeout')
                            else:
                                self.playerIdleTimeout = i
                        except:
                            errors.append('player-idle-timeout')

                    elif ( name == 'max-threads' ):
                        try:
                            i = int(value)
                            if ( i < 0 ):
                                errors.append('max-threads')
                            else:
                                self.maxThreads = i
                        except:
                            errors.append('max-threads')

                    elif ( name == 'level-name' ):
                        if ( len(value) == 0 ):
                            errors.append('level-name')
                        else:
                            self.levelName = value

                    elif ( name == 'level-seed' ):
                        if ( 1 == 0 ):
                            errors.append('level-seed')
                        else:
                            self.levelSeed = value

                    elif ( name == 'default-player-permission-level' ):
                        if ( value not in self.defaultPlayerPermissionLevelValues ):
                            errors.append('default-players-permission-level')
                        else:
                            self.defaultPlayerPermissionLevel = value

                    elif ( name == 'texturepack-required' ):
                        try:
                            b = bool(value)
                            self.texturepackRequired = b
                        except:
                            errors.append('texturepack-required')

        inFile.close()

        return errors
