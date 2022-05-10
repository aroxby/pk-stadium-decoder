#!/usr/bin/env python3
from enum import Enum


class Type(Enum):
    NORMAL = 0
    FIGHTING = 1
    FLYING = 2
    POISON = 3
    GROUND = 4
    ROCK = 5
    BIRD = 6
    BUG = 7
    GHOST = 8
    FIRE = 20
    WATER = 21
    GRASS = 22
    ELECTRIC = 23
    PSYCHIC = 24
    ICE = 25
    DRAGON = 26

    def __str__(self):
        MAPPING = {
            self.BIRD: 'Bird',
            self.BUG: 'Bug',
            self.ELECTRIC: 'Electric',
            self.FIGHTING: 'Fighting',
            self.FIRE: 'Fire',
            self.FLYING: 'Flying',
            self.GHOST: 'Ghost',
            self.GRASS: 'Grass',
            self.GROUND: 'Ground',
            self.ICE: 'Ice',
            self.NORMAL: 'Normal',
            self.POISON: 'Poison',
            self.PSYCHIC: 'Psychic',
            self.ROCK: 'Rock',
            self.WATER: 'Water',
        }
        name = MAPPING.get(self, f'<Type {self.value}>')
        return name


class Move(Enum):
    NONE = 0
    POUND = 1
    KARATECHOP = 2
    DOUBLESLAP = 3
    COMETPUNCH = 4
    MEGAPUNCH = 5
    PAYDAY = 6
    FIREPUNCH = 7
    ICEPUNCH = 8
    THUNDERPUNCH = 9
    SCRATCH = 10
    VICEGRIP = 11
    GUILLOTINE = 12
    RAZORWIND = 13
    SWORDSDANCE = 14
    CUT = 15
    GUST = 16
    WINGATTACK = 17
    WHIRLWIND = 18
    FLY = 19
    BIND = 20
    SLAM = 21
    VINEWHIP = 22
    STOMP = 23
    DOUBLEKICK = 24
    MEGAKICK = 25
    JUMPKICK = 26
    ROLLINGKICK = 27
    SANDATTACK = 28
    HEADBUTT = 29
    HORNATTACK = 30
    FURYATTACK = 31
    HORNDRILL = 32
    TACKLE = 33
    BODYSLAM = 34
    WRAP = 35
    TAKEDOWN = 36
    THRASH = 37
    DOUBLEEDGE = 38
    TAILWHIP = 39
    POISONSTING = 40
    TWINEEDLE = 41
    PINMISSILE = 42
    LEER = 43
    BITE = 44
    GROWL = 45
    ROAR = 46
    SING = 47
    SUPERSONIC = 48
    SONICBOOM = 49
    DISABLE = 50
    ACID = 51
    EMBER = 52
    FLAMETHROWER = 53
    MIST = 54
    WATERGUN = 55
    HYDROPUMP = 56
    SURF = 57
    ICEBEAM = 58
    BLIZZARD = 59
    PSYBEAM = 60
    BUBBLEBEAM = 61
    AURORABEAM = 62
    HYPERBEAM = 63
    PECK = 64
    DRILLPECK = 65
    SUBMISSION = 66
    LOWKICK = 67
    COUNTER = 68
    SEISMICTOSS = 69
    STRENGTH = 70
    ABSORB = 71
    MEGADRAIN = 72
    LEECHSEED = 73
    GROWTH = 74
    RAZORLEAF = 75
    SOLARBEAM = 76
    POISONPOWDER = 77
    STUNSPORE = 78
    SLEEPPOWDER = 79
    PETALDANCE = 80
    STRINGSHOT = 81
    DRAGONRAGE = 82
    FIRESPIN = 83
    THUNDERSHOCK = 84
    THUNDERBOLT = 85
    THUNDERWAVE = 86
    THUNDER = 87
    ROCKTHROW = 88
    EARTHQUAKE = 89
    FISSURE = 90
    DIG = 91
    TOXIC = 92
    CONFUSION = 93
    PSYCHIC = 94
    HYPNOSIS = 95
    MEDITATE = 96
    AGILITY = 97
    QUICKATTACK = 98
    RAGE = 99
    TELEPORT = 100
    NIGHTSHADE = 101
    MIMIC = 102
    SCREECH = 103
    DOUBLETEAM = 104
    RECOVER = 105
    HARDEN = 106
    MINIMIZE = 107
    SMOKESCREEN = 108
    CONFUSERAY = 109
    WITHDRAW = 110
    DEFENSECURL = 111
    BARRIER = 112
    LIGHTSCREEN = 113
    HAZE = 114
    REFLECT = 115
    FOCUSENERGY = 116
    BIDE = 117
    METRONOME = 118
    MIRRORMOVE = 119
    SELFDESTRUCT = 120
    EGGBOMB = 121
    LICK = 122
    SMOG = 123
    SLUDGE = 124
    BONECLUB = 125
    FIREBLAST = 126
    WATERFALL = 127
    CLAMP = 128
    SWIFT = 129
    SKULLBASH = 130
    SPIKECANNON = 131
    CONSTRICT = 132
    AMNESIA = 133
    KINESIS = 134
    SOFTBOILED = 135
    HIJUMPKICK = 136
    GLARE = 137
    DREAMEATER = 138
    POISONGAS = 139
    BARRAGE = 140
    LEECHLIFE = 141
    LOVELYKISS = 142
    SKYATTACK = 143
    TRANSFORM = 144
    BUBBLE = 145
    DIZZYPUNCH = 146
    SPORE = 147
    FLASH = 148
    PSYWAVE = 149
    SPLASH = 150
    ACIDARMOR = 151
    CRABHAMMER = 152
    EXPLOSION = 153
    FURYSWIPES = 154
    BONEMERANG = 155
    REST = 156
    ROCKSLIDE = 157
    HYPERFANG = 158
    SHARPEN = 159
    CONVERSION = 160
    TRIATTACK = 161
    SUPERFANG = 162
    SLASH = 163
    SUBSTITUTE = 164
    STRUGGLE = 165

    def __str__(self):
        MAPPING = {
            self.NONE: '-',
            self.ABSORB: 'Absorb',
            self.ACIDARMOR: 'Acid Armor',
            self.ACID: 'Acid',
            self.AGILITY: 'Agility',
            self.AMNESIA: 'Amnesia',
            self.AURORABEAM: 'Aurora Beam',
            self.BARRAGE: 'Barrage',
            self.BARRIER: 'Barrier',
            self.BIDE: 'Bide',
            self.BIND: 'Bind',
            self.BITE: 'Bite',
            self.BLIZZARD: 'Blizzard',
            self.BODYSLAM: 'Body Slam',
            self.BONECLUB: 'Bone Club',
            self.BONEMERANG: 'Bonemerang',
            self.BUBBLE: 'Bubble',
            self.BUBBLEBEAM: 'Bubblebeam',
            self.CLAMP: 'Clamp',
            self.COMETPUNCH: 'Comet Punch',
            self.CONFUSERAY: 'Confuse Ray',
            self.CONFUSION: 'Confusion',
            self.CONSTRICT: 'Constrict',
            self.CONVERSION: 'Conversion',
            self.COUNTER: 'Counter',
            self.CRABHAMMER: 'Crabhammer',
            self.CUT: 'Cut',
            self.DEFENSECURL: 'Defense Curl',
            self.DIG: 'Dig',
            self.DISABLE: 'Disable',
            self.DIZZYPUNCH: 'Dizzy Punch',
            self.DOUBLEKICK: 'Double Kick',
            self.DOUBLETEAM: 'Double Team',
            self.DOUBLEEDGE: 'Double-Edge',
            self.DOUBLESLAP: 'Doubleslap',
            self.DRAGONRAGE: 'Dragon Rage',
            self.DREAMEATER: 'Dream Eater',
            self.DRILLPECK: 'Drill Peck',
            self.EARTHQUAKE: 'Earthquake',
            self.EGGBOMB: 'Egg Bomb',
            self.EMBER: 'Ember',
            self.EXPLOSION: 'Explosion',
            self.FIREBLAST: 'Fire Blast',
            self.FIREPUNCH: 'Fire Punch',
            self.FIRESPIN: 'Fire Spin',
            self.FISSURE: 'Fissure',
            self.FLAMETHROWER: 'Flamethrower',
            self.FLASH: 'Flash',
            self.FLY: 'Fly',
            self.FOCUSENERGY: 'Focus Energy',
            self.FURYATTACK: 'Fury Attack',
            self.FURYSWIPES: 'Fury Swipes',
            self.GLARE: 'Glare',
            self.GROWL: 'Growl',
            self.GROWTH: 'Growth',
            self.GUILLOTINE: 'Guillotine',
            self.GUST: 'Gust',
            self.HARDEN: 'Harden',
            self.HAZE: 'Haze',
            self.HEADBUTT: 'Headbutt',
            self.HIJUMPKICK: 'Hi Jump Kick',
            self.HORNATTACK: 'Horn Attack',
            self.HORNDRILL: 'Horn Drill',
            self.HYDROPUMP: 'Hydro Pump',
            self.HYPERBEAM: 'Hyper Beam',
            self.HYPERFANG: 'Hyper Fang',
            self.HYPNOSIS: 'Hypnosis',
            self.ICEBEAM: 'Ice Beam',
            self.ICEPUNCH: 'Ice Punch',
            self.JUMPKICK: 'Jump Kick',
            self.KARATECHOP: 'Karate Chop',
            self.KINESIS: 'Kinesis',
            self.LEECHLIFE: 'Leech Life',
            self.LEECHSEED: 'Leech Seed',
            self.LEER: 'Leer',
            self.LICK: 'Lick',
            self.LIGHTSCREEN: 'Light Screen',
            self.LOVELYKISS: 'Lovely Kiss',
            self.LOWKICK: 'Low Kick',
            self.MEDITATE: 'Meditate',
            self.MEGADRAIN: 'Mega Drain',
            self.MEGAKICK: 'Mega Kick',
            self.MEGAPUNCH: 'Mega Punch',
            self.METRONOME: 'Metronome',
            self.MIMIC: 'Mimic',
            self.MINIMIZE: 'Minimize',
            self.MIRRORMOVE: 'Mirror Move',
            self.MIST: 'Mist',
            self.NIGHTSHADE: 'Night Shade',
            self.PAYDAY: 'Pay Day',
            self.PECK: 'Peck',
            self.PETALDANCE: 'Petal Dance',
            self.PINMISSILE: 'Pin Missile',
            self.POISONGAS: 'Poison Gas',
            self.POISONSTING: 'Poison Sting',
            self.POISONPOWDER: 'Poisonpowder',
            self.POUND: 'Pound',
            self.PSYBEAM: 'Psybeam',
            self.PSYCHIC: 'Psychic',
            self.PSYWAVE: 'Psywave',
            self.QUICKATTACK: 'Quick Attack',
            self.RAGE: 'Rage',
            self.RAZORLEAF: 'Razor Leaf',
            self.RAZORWIND: 'Razor Wind',
            self.RECOVER: 'Recover',
            self.REFLECT: 'Reflect',
            self.REST: 'Rest',
            self.ROAR: 'Roar',
            self.ROCKSLIDE: 'Rock Slide',
            self.ROCKTHROW: 'Rock Throw',
            self.ROLLINGKICK: 'Rolling Kick',
            self.SANDATTACK: 'Sand-Attack',
            self.SCRATCH: 'Scratch',
            self.SCREECH: 'Screech',
            self.SEISMICTOSS: 'Seismic Toss',
            self.SELFDESTRUCT: 'Selfdestruct',
            self.SHARPEN: 'Sharpen',
            self.SING: 'Sing',
            self.SKULLBASH: 'Skull Bash',
            self.SKYATTACK: 'Sky Attack',
            self.SLAM: 'Slam',
            self.SLASH: 'Slash',
            self.SLEEPPOWDER: 'Sleep Powder',
            self.SLUDGE: 'Sludge',
            self.SMOG: 'Smog',
            self.SMOKESCREEN: 'Smokescreen',
            self.SOFTBOILED: 'Softboiled',
            self.SOLARBEAM: 'Solarbeam',
            self.SONICBOOM: 'Sonicboom',
            self.SPIKECANNON: 'Spike Cannon',
            self.SPLASH: 'Splash',
            self.SPORE: 'Spore',
            self.STOMP: 'Stomp',
            self.STRENGTH: 'Strength',
            self.STRINGSHOT: 'String Shot',
            self.STRUGGLE: 'Struggle',
            self.STUNSPORE: 'Stun Spore',
            self.SUBMISSION: 'Submission',
            self.SUBSTITUTE: 'Substitute',
            self.SUPERFANG: 'Super Fang',
            self.SUPERSONIC: 'Supersonic',
            self.SURF: 'Surf',
            self.SWIFT: 'Swift',
            self.SWORDSDANCE: 'Swords Dance',
            self.TACKLE: 'Tackle',
            self.TAILWHIP: 'Tail Whip',
            self.TAKEDOWN: 'Take Down',
            self.TELEPORT: 'Teleport',
            self.THRASH: 'Thrash',
            self.THUNDERWAVE: 'Thunder Wave',
            self.THUNDER: 'Thunder',
            self.THUNDERBOLT: 'Thunderbolt',
            self.THUNDERPUNCH: 'Thunderpunch',
            self.THUNDERSHOCK: 'Thundershock',
            self.TOXIC: 'Toxic',
            self.TRANSFORM: 'Transform',
            self.TRIATTACK: 'Tri Attack',
            self.TWINEEDLE: 'Twineedle',
            self.VICEGRIP: 'Vicegrip',
            self.VINEWHIP: 'Vine Whip',
            self.WATERGUN: 'Water Gun',
            self.WATERFALL: 'Waterfall',
            self.WHIRLWIND: 'Whirlwind',
            self.WINGATTACK: 'Wing Attack',
            self.WITHDRAW: 'Withdraw',
            self.WRAP: 'Wrap',
        }
        name = MAPPING.get(self, f'<Move {self.value}>')
        return name
