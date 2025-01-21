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

def gen_board_id_rst(rocketcan):
    print(board_id_rst_header)

    for board in rocketcan['boards']:
        print('   * - ' + board['name'].data)
        if 'doc-link' in board:
            print('     - :doc:`' + board['desc'].data + '<' + board['doc-link'].data + '>`')
        else:
            print('     - ' + board['desc'].data)
        print('     - 0x' + '{:02X}'.format(board['id'].data))
