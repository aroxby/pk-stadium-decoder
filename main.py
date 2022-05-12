#!/usr/bin/env python3
from dataclasses import dataclass
import struct

import xlsxwriter

from pokemon_data import Move, Type


def mem_to_z64(addr):
    # Offset found by guess and check may vary between roms
    return addr - 0x3000


class CONSTANTS:
    class RENTAL_OFFSETS:
        # Source: https://datacrystal.romhacking.net/wiki/Pok%C3%A9mon_Stadium:ROM_map
        class PETIT:
            Z64 = mem_to_z64(0x8A9480)
        class PIKA:
            Z64 = mem_to_z64(0x8AA350)
        class PRIME_R1:
            Z64 = mem_to_z64(0x8AC130)
        class POKE:
            Z64 = mem_to_z64(0x8AF220)
        class GYMS:
            Z64 = mem_to_z64(0x8B2780)
        class PRIME_R2:
            Z64 = mem_to_z64(0x8C6900)


@dataclass
class Stats:
    hp: int
    attack: int
    denfense: int
    speed: int
    special: int


@dataclass
class Pokemon:
    pokdex: int
    level: int
    types: tuple[Type, Type]
    moves: tuple[Move, Move, Move, Move]
    exp: int
    stat_exp: Stats
    pp: tuple[int, int, int, int]
    stats: Stats
    nickname: str

    def as_dict(self):
        data = {
            'Pokedex Number': self.pokdex,
            'Nickname': self.nickname.title(),
            'Level': self.level,
            'HP': self.stats.hp,
            'Attack': self.stats.attack,
            'Defense': self.stats.denfense,
            'Speed': self.stats.speed,
            'Special': self.stats.special,
            'Exp': self.exp,
            'Type 1': str(self.types[0]),
            'Type 2': str(self.types[1]),
            'Move 1': str(self.moves[0]),
            'Move 2': str(self.moves[1]),
            'Move 3': str(self.moves[2]),
            'Move 4': str(self.moves[3]),
            'PP Move 1': self.pp[0],
            'PP Move 2': self.pp[1],
            'PP Move 3': self.pp[2],
            'PP Move 4': self.pp[3],
            'HP Stat Exp': self.stat_exp.hp,
            'Attack Stat Exp': self.stat_exp.attack,
            'Defense Stat Exp': self.stat_exp.denfense,
            'Speed Stat Exp': self.stat_exp.speed,
            'Special Stat Exp': self.stat_exp.special,
        }
        return data


class RentalDecoder:
    def __init__(self, rom_bytes):
        self.bytes = rom_bytes

    def _unpack_nibbles(self, offset, count):
        count_bytes = int(count/2 + 0.5)
        data_bytes = self.bytes[offset:offset + count_bytes]
        read_bytes = struct.unpack('>' + 'B' * count_bytes, data_bytes)
        read_nibbles = []
        for read_byte in read_bytes:
            read_nibbles.append(read_byte & 0x0F)
            read_byte >>= 4
            read_nibbles.append(read_byte & 0x0F)
        nibbles = tuple(read_nibbles[:count])
        return nibbles

    def _unpack_bytes(self, offset, count):
        val_bytes = self.bytes[offset:offset + count]
        vals = struct.unpack('>' + 'B' * count, val_bytes)
        return vals

    def _unpack_byte(self, offset):
        return self._unpack_bytes(offset, 1)[0]

    def _unpack_shorts(self, offset, count):
        val_bytes = self.bytes[offset:offset + count * 2]
        vals = struct.unpack('>' + 'H' * count, val_bytes)
        return vals

    def _unpack_short(self, offset):
        return self._unpack_shorts(offset, 1)[0]

    def _unpack_longs(self, offset, count):
        val_bytes = self.bytes[offset:offset + count * 4]
        vals = struct.unpack('>' + 'L' * count, val_bytes)
        return vals

    def _unpack_long(self, offset):
        return self._unpack_longs(offset, 1)[0]

    def _unpack_string(self, offset):
        MAX_LEN = 11  # Common to generation
        TEXT_TERMINATOR = '\0'  # Common to rom family
        val_bytes = self.bytes[offset:offset + MAX_LEN]
        val = val_bytes.decode('ISO-8859-1').split(TEXT_TERMINATOR)[0]
        val = self._fix_string_symbols(val)
        return val

    @staticmethod
    def _fix_string_symbols(val):
        return val.replace('¾', '♀').replace('©', '♂')

    @property
    def pokdex(self):
        OFFSET = 0
        return self._unpack_byte(OFFSET)

    @property
    def level(self):
        OFFSET = 4
        return self._unpack_byte(OFFSET)

    @property
    def types(self):
        OFFSET = 6
        type_ids = self._unpack_bytes(OFFSET, 2)
        types = tuple(Type(type_id) for type_id in type_ids)
        return types

    @property
    def moves(self):
        OFFSET = 9
        move_ids = self._unpack_bytes(OFFSET, 4)
        moves = tuple(Move(move_id) for move_id in move_ids)
        return moves

    @property
    def trainer_id(self):
        OFFSET = 14
        return self._unpack_short(OFFSET)

    @property
    def experience(self):
        OFFSET = 16
        return self._unpack_long(OFFSET)

    @property
    def stat_exp(self):
        OFFSET = 20
        return self._unpack_shorts(OFFSET, 5)

    @property
    def ivs(self):
        OFFSET = 30
        return self._unpack_nibbles(OFFSET, 4)

    @property
    def pps(self):
        OFFSET = 32
        return self._unpack_bytes(OFFSET, 4)

    @property
    def stats(self):
        OFFSET = 38
        return self._unpack_shorts(OFFSET, 5)

    @property
    def nickname(self):
        OFFSET = 48
        return self._unpack_string(OFFSET)

    @property
    def trainer_name(self):
        OFFSET = 59
        return self._unpack_string(OFFSET)

    @staticmethod
    def _create_stats_obj(stat_vals):
        stats = Stats(
            hp=stat_vals[0],
            attack=stat_vals[1],
            denfense=stat_vals[2],
            speed=stat_vals[3],
            special=stat_vals[4],
        )
        return stats

    def create_stat_exp(self):
        stat_exp_vals = self.stat_exp
        return self._create_stats_obj(stat_exp_vals)

    def create_stats(self):
        stat_vals = self.stats
        return self._create_stats_obj(stat_vals)

    def create_pokemon(self):
        pokemon = Pokemon(
            pokdex=self.pokdex,
            level=self.level,
            types=self.types,
            moves=self.moves,
            exp=self.experience,
            stat_exp=self.create_stat_exp(),
            pp=self.pps,
            stats=self.create_stats(),
            nickname=self.nickname,
        )
        return pokemon


def load_rentals(rom_file, offset):
    RENTAL_HEADER_LENGTH = 4
    RENTAL_LENGTH = 0x43 + 0x11  # Struct length + padding?

    rom_file.seek(offset)
    rental_header_bytes = rom_file.read(RENTAL_HEADER_LENGTH)
    num_rentals = struct.unpack('>L', rental_header_bytes)[0]
    assert 0 < num_rentals < 151, f'found {num_rentals} rentals'

    rentals = tuple(
        RentalDecoder(rom_file.read(RENTAL_LENGTH)).create_pokemon()
        for _ in range(num_rentals)
    )

    return rentals


def write_worksheet(sheetname, data, workbook):
    worksheet = workbook.add_worksheet(sheetname)
    bold_format = workbook.add_format({'bold': True})
    worksheet.write_row(0, 0, data[0].keys(), bold_format)
    for i, row_data in enumerate(data, 1):
        worksheet.write_row(i, 0, row_data.values())


def main():
    sheets_to_create = {
        'Pika Cup': CONSTANTS.RENTAL_OFFSETS.PIKA.Z64,
        'Petit Cup': CONSTANTS.RENTAL_OFFSETS.PETIT.Z64,
        'Poke Cup': CONSTANTS.RENTAL_OFFSETS.POKE.Z64,
        # TODO: Are the rentals for both rounds the same?
        'Prime Cup (Round 1)': CONSTANTS.RENTAL_OFFSETS.PRIME_R1.Z64,
        'Prime Cup (Round 2)': CONSTANTS.RENTAL_OFFSETS.PRIME_R2.Z64,
        'Gym Leader Castle': CONSTANTS.RENTAL_OFFSETS.GYMS.Z64,
    }

    with open('a2dc9d1.z64', 'rb') as rom_file:
        with xlsxwriter.Workbook('Pokemon Stadium Rentals.xlsx') as workbook:
            for sheet_name, rental_offset in sheets_to_create.items():
                rentals = load_rentals(rom_file, rental_offset)
                write_worksheet(
                    sheet_name, tuple(rental.as_dict() for rental in rentals), workbook
                )


if __name__ == '__main__':
    main()
