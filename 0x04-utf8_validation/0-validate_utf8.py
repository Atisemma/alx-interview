#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
    data (list of int): A list of integers where each integer represents
                        1 byte of data

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit (8th bit from left) is set
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set
    mask2 = 1 << 6

    for num in data:
        # Get only the 8 least significant bits of the number
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine how many bytes the UTF-8 character has
            mask = mask1
            while byte & mask:
                n_bytes += 1
                mask = mask >> 1

            # 1-byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    # All characters must be complete
    return n_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105,
            115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
