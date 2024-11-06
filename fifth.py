import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Načte binární soubor z cesty file_name,
    přečte prvních header_length bytů a vrátí je.
    """
    try:
        with open(file_name, 'rb') as file:
            return file.read(header_length)
    except Exception as e:
        print(f"Chyba při čtení souboru {file_name}: {e}")
        return None


def is_jpeg(file_name):
    """
    Zkontroluje, zda soubor začíná sekvencí jpeg_header.
    """
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header if header else False


def is_gif(file_name):
    """
    Zkontroluje, zda soubor začíná sekvencí gif_header1 nebo gif_header2.
    """
    header = read_header(file_name, len(gif_header1))
    return header == gif_header1 or header == gif_header2 if header else False


def is_png(file_name):
    """
    Zkontroluje, zda soubor začíná sekvencí png_header.
    """
    header = read_header(file_name, len(png_header))
    return header == png_header if header else False


def print_file_type(file_name):
    """
    Vypíše typ souboru na základě jeho hlavičky.
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    try:
        file_name = sys.argv[1]  # Čte název souboru z příkazové řádky
        print_file_type(file_name)
    except IndexError:
        print("Chyba: Název souboru není uveden.")
    except Exception as e:
        print(f"Neočekávaná chyba: {e}")