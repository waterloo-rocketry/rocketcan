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
******************

Common Instance IDs
===================

.. list-table:: Common Instance IDs
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Instance Name
     - ID
   * - ANY
     - Any board
     - 0x00
   * - GROUND
     - Board on ground
     - 0x01
   * - ROCKET
     - Board on rocket
     - 0x02
   * - PAYLOAD
     - Board in payload
     - 0x03"""

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

    inst_id = 4
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
    print('Packet Format\n#####################\n')
    print('**Note:** All multi-byte data field are big-endian\n')
    print('Message Packet Format Definition\n********************************\n')
    
    for msg in rocketcan['messages']:
        print(msg['name'].data + ' (0x' + '{:03X}'.format(msg['id'].data) + ')')
        print('=' * (len(msg['name'].data) + 8))
        if 'desc' in msg:
            print(msg['desc'].data + '\n')

        if 'field' in msg:
            line_1 = '+'
            line_2 = '|'
            line_3 = '+'
            line_4 = '|'
            line_5 = '+'
            next_byte = 0

            if(msg['timestamp'] == 2):
                line_1 += '--------+---------+'
                line_2 += ' Byte 0 | Byte 1  |'
                line_3 += '========+=========+'
                line_4 += ' 2 byte timestamp |'
                line_5 += '--------+---------+'
                next_byte += 2

            for field in msg['field']:
                byte_str = 'Byte '
                if(field['width'].data == 1):
                    byte_str += str(next_byte)
                else:
                    byte_str = byte_str + str(next_byte) + '-' + str(next_byte + field['width'].data - 1)
                if(len(byte_str) > len(field['name'].data)):
                    box_width = len(byte_str)
                    line_1 = line_1 + '-' * (box_width + 2) + '+'
                    line_2 = line_2 + ' ' + byte_str + ' |'
                    line_3 = line_3 + '=' * (box_width + 2) + '+'
                    line_4 = line_4 + ' ' + field['name'].data + ' ' * (box_width - len(field['name'].data)) + ' |'
                    line_5 = line_5 + '-' * (box_width + 2) + '+'
                else:
                    box_width = len(field['name'].data)
                    line_1 = line_1 + '-' * (box_width + 2) + '+'
                    line_2 = line_2 + ' ' + byte_str + ' ' * (box_width - len(byte_str)) + ' |'
                    line_3 = line_3 + '=' * (box_width + 2) + '+'
                    line_4 = line_4 + ' ' + field['name'].data + ' |'
                    line_5 = line_5 + '-' * (box_width + 2) + '+'
                    next_byte += field['width'].data

            print(line_1)
            print(line_2)
            print(line_3)
            print(line_4)
            print(line_5 + '\n')

            for field in msg['field']:
                if 'enum' in field:
                    print('| **' + field['name'].data + ':** ' + field['desc'].data + ', see `' + field['enum'].data + '`_')
                elif 'bitfield' in field:
                    print('| **' + field['name'].data + ':** ' + field['desc'].data + ', see `' + field['bitfield'].data + '`_')
                else:
                    print('| **' + field['name'].data + ':** ' + field['desc'].data)
            print('')

    print('Enums Definition\n****************\n')
    for enum in rocketcan['enums']:
        print(enum['name'].data)
        print('=' * len(enum['name'].data) + '\n')
        print(enum['desc'].data + '\n')
        print('.. list-table:: ' + enum['name'].data + ' Enum Values')
        print('   :widths: 25 60 15\n   :header-rows: 1\n')
        print('   * - Enum Name\n     - Description\n     - ID')
        enum_value_id = 0
        for value in enum['value']:
            if 'value' in value:
                enum_value_id = value['value'].data
            print('   * - ' + value['name'].data)
            if 'desc' in value:
                print('     - ' + value['desc'].data)
            else:
                print('     - No Description')
            print('     - 0x' + '{:02X}'.format(enum_value_id))
            enum_value_id += 1
        print('')

    print('Bitfields Definition\n*********************\n')
    for bitfield in rocketcan['bitfields']:
        print(bitfield['name'].data)
        print('=' * len(bitfield['name'].data) + '\n')
        print(bitfield['desc'].data + '\n')
        print('.. list-table:: ' + bitfield['name'].data + ' Bitfield bits')
        print('   :widths: 25 60 15\n   :header-rows: 1\n')
        print('   * - Bitfield Name\n     - Description\n     - Offset')
        bit_offset = 0
        for bit in bitfield['bits']:
            print('   * - ' + bit['name'].data)
            if 'desc' in bit:
                print('     - ' + bit['desc'].data)
            else:
                print('     - No Description')
            print('     - 0x' + '{:02X}'.format(bit_offset))
            bit_offset += 1
        print('')
