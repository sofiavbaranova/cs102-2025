def encrypt_atbash(plaintext: str) -> str:
    """Шифрует переданный текст с помощью шифра Атбаш"""
    result = []

    a_lower = ord("а")
    z_lower = ord("я")
    a_upper = ord("А")
    z_upper = ord("Я")

    n_lower = z_lower - a_lower + 1
    n_upper = z_upper - a_upper + 1

    for ch in plaintext:
        code = ord(ch)

        if a_lower <= code <= z_lower:
            i = code - a_lower + 1
            j = n_lower - i + 1
            new_code = a_lower + (j - 1)
            result.append(chr(new_code))

        elif a_upper <= code <= z_upper:
            i = code - a_upper + 1
            j = n_upper - i + 1
            new_code = a_upper + (j - 1)
            result.append(chr(new_code))

        else:
            result.append(ch)

    return "".join(result)
