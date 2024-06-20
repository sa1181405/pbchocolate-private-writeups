def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def decode_song(song_lines, code_lines):
    result = ''
    for line in code_lines:
        codes = line.strip().split()
        for code in codes:
            line_num, char_num = map(int, code.split('.'))
            result += song_lines[line_num - 1][char_num - 1]
    return result

def main():
    song_lines = read_file('song.txt')
    code_lines = read_file('code.txt')
    decoded_song = decode_song(song_lines, code_lines)
    print(decoded_song)

if __name__ == "__main__":
    main()

# this was made with chatgpt
