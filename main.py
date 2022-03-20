#!/usr/bin/env python3
import struct


class Rental:
    def __init__(self, rom_bytes):
        self.bytes = rom_bytes

    @property
    def name(self):
        NAME_OFFSET = 48
        MAX_NAME = 11
        TEXT_TERMINATOR = '\0'
        name_bytes = self.bytes[NAME_OFFSET:NAME_OFFSET + MAX_NAME]
        name = name_bytes.decode('utf-8').split(TEXT_TERMINATOR)[0]
        return name

    @property
    def pokdex(self):
        ID_OFFSET = 0
        ID_SIZE = 1
        id_bytes = self.bytes[ID_OFFSET:ID_OFFSET + ID_SIZE]
        id_val = struct.unpack('>B', id_bytes)[0]
        return id_val


def load_z64_pika_rentals(rom_file):
    OFFSET = 0x8A7350  # 0x008A6480 for Petit Cup
    RENTAL_HEADER_LENGTH = 4
    RENTAL_LENGTH = 0x43 + 0x11  # Struct length + padding?

    rom_file.seek(OFFSET)
    rental_header_bytes = rom_file.read(RENTAL_HEADER_LENGTH)
    num_rentals = struct.unpack('>L', rental_header_bytes)[0]
    assert 0 < num_rentals < 151, f'found {num_rentals} rentals'

    rentals = tuple(
        Rental(rom_file.read(RENTAL_LENGTH)) for _ in range(num_rentals)
    )

    return rentals


def main():
    with open('rev2.z64', 'rb') as rom_file:
        rentals = load_z64_pika_rentals(rom_file)
    print(len(rentals), 'rentals')
    for rental in rentals[:5]:
        print(rental.pokdex)
        print(rental.name)


if __name__ == '__main__':
    main()
