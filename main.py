#!/usr/bin/env python3
from dataclasses import dataclass
import struct


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
    types: tuple[int, int]  # TODO: Enum?
    moves: tuple[int, int, int, int]  # TODO: Enum?
    exp: int
    stat_exp: Stats
    pp: tuple[int, int, int, int]
    stats: Stats
    nickname: str


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
        return self._unpack_bytes(OFFSET, 2)

    @property
    def moves(self):
        OFFSET = 9
        return self._unpack_bytes(OFFSET, 4)

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



def load_z64_pika_rentals(rom_file):
    OFFSET = 0x8A7350  # 0x008A6480 for Petit Cup
    RENTAL_HEADER_LENGTH = 4
    RENTAL_LENGTH = 0x43 + 0x11  # Struct length + padding?

    rom_file.seek(OFFSET)
    rental_header_bytes = rom_file.read(RENTAL_HEADER_LENGTH)
    num_rentals = struct.unpack('>L', rental_header_bytes)[0]
    assert 0 < num_rentals < 151, f'found {num_rentals} rentals'

    rentals = tuple(
        RentalDecoder(rom_file.read(RENTAL_LENGTH)).create_pokemon()
        for _ in range(num_rentals)
    )

    return rentals


def main():
    with open('rev2.z64', 'rb') as rom_file:
        rentals = load_z64_pika_rentals(rom_file)
    print(len(rentals), 'rentals')
    for rental in rentals:
        print(rental.nickname)


if __name__ == '__main__':
    main()
