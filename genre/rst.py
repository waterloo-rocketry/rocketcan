board_id_rst_header = """Board IDs
#########

Board Type IDs
**************

.. list-table:: Board Type IDs
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Name
     - ID"""

board_inst_id_str = """
Board Instance IDs
******************"""

board_inst_table_header = """   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Instance Name
     - ID"""

def gen_board_id_rst(rocketcan):
    print(board_id_rst_header)

    for board in rocketcan['boards']:
        print('   * - ' + board['name'].data)
        if 'doc-link' in board:
            print('     - :doc:`' + board['desc'].data + '<' + board['doc-link'].data + '>`')
        else:
            print('     - ' + board['desc'].data)
        print('     - 0x' + '{:02X}'.format(board['id'].data))

    print(board_inst_id_str)

    inst_id = 2
    for board in rocketcan['boards']:
        if "inst" in board:
            print('\n' + board['desc'].data)
            print('=' * len(board['desc'].data) + '\n')
            print('.. list-table:: ' + board['desc'].data + ' Instances')
            print(board_inst_table_header)
            for inst in board['inst']:
                print('   * - ' + inst['name'].data)
                print('     - ' + inst['desc'].data)
                print('     - 0x' + '{:02X}'.format(inst_id))
                inst_id += 1

def gen_packet_format_rst(rocketcan):
    print('Message Packet Format\n#####################')
    for msg in rocketcan['messages']:
        print(msg['name'].data + ' (0x' + '{:03X}'.format(msg['id'].data) + ')')
        print('*' * (len(msg['name'].data) + 8))
        if 'desc' in msg:
            print(msg['desc'].data + '\n')

        if 'field' in msg:
            line_1 = '+'
            line_2 = '|'
            line_3 = '+'
            line_4 = '|'
            line_5 = '+'
            next_byte = 0
            if(msg['timestamp'] == 3):
                line_1 += '--------+--------+--------+'
                line_2 += ' Byte 0 | Byte 1 | Byte 2 |'
                line_3 += '========+========+========+'
                line_4 += ' 3 byte timestamp         |'
                line_5 += '--------------------------+'
                next_byte += 3
            elif(msg['timestamp'] == 2):
                line_1 += '------------------+----------------+'
                line_2 += ' Byte 0           | Byte 1         |'
                line_3 += '==================+================+'
                line_4 += ' 2 byte timestamp (MED/LO)         |'
                line_5 += '------------------+----------------+'
                next_byte += 2
            for field in msg['field']:
                byte_str = 'Byte '
                if(field['width'].data == 1):
                    byte_str += str(next_byte)
                else:
                    byte_str = byte_str + str(next_byte) + '-' + str(next_byte + field['width'].data - 1)
                if(len(byte_str) > len(field['name'].data)):
                    box_width = len(byte_str)
                    line_1 = line_1 + '-' * box_width + '+'
                    line_2 = line_2 + byte_str + '|'
                    line_3 = line_3 + '=' * box_width + '+'
                    line_4 = line_4 + field['name'].data + ' ' * (box_width - len(field['name'].data)) + '|'
                    line_5 = line_5 + '-' * box_width + '+'
                else:
                    box_width = len(field['name'].data)
                    line_1 = line_1 + '-' * box_width + '+'
                    line_2 = line_2 + byte_str + ' ' * (box_width - len(byte_str)) + '|'
                    line_3 = line_3 + '=' * box_width + '+'
                    line_4 = line_4 + field['name'].data + '|'
                    line_5 = line_5 + '-' * box_width + '+'
                    next_byte += field['width'].data

            print(line_1)
            print(line_2)
            print(line_3)
            print(line_4)
            print(line_5 + '\n')

            for field in msg['field']:
                print('| **' + field['name'].data + ':** ' + field['desc'].data)
            print('')
