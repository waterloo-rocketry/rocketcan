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
