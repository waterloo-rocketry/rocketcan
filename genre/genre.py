import argparse
from strictyaml import load,Map,Str,HexInt,Int,Seq,YAMLError,Optional

def main():
    argparser = argparse.ArgumentParser(prog = 'Waterloo Rockery CAN message generator',
                                        description = 'Generate canlib, parsley message definition and documentation');
    argparser.add_argument('yaml_filename')
    argparser.add_argument('-f', '--format')
    args = argparser.parse_args()

    yaml_str = open(args.yaml_filename, 'r').read()
    schema = Map({
        "messages" : Seq(Map({
            "name":Str(),
            Optional("desc"):Str(),
            "id":HexInt(),
            "timestamp":Int(),
            "field":Seq(Map({
                "name":Str(),
                "width":Int(),
                Optional("desc"):Str(),
                Optional("unit"):Str(),
                Optional("enum"):Str(),
                Optional("bits"):Seq(Map({
                    "name":Str(),
                    "width":Int(),
                    Optional("desc"):Str(),
                    Optional("unit"):Str(),
                    Optional("enum"):Str(),
                }))
            }))})),
        "boards" : Seq(Map({
            "name":Str(),
            "desc":Str(),
            "id":HexInt(),
            Optional("inst"):Seq(Map({
                "name":Str(),
                "desc":Str(),
            }))
        })),
        "enums" : Seq(Map({
            "name":Str(),
            "value":Seq(Map({
                "name":Str(),
                Optional("desc"):Str()
            }))
        }))
    })

    try:
        rocketcan = load(yaml_str,schema)

        if(args.format == 'message-types-h'):
            print('// Auto generated file, do not edit directly\n')

            print('#ifndef _CANLIB_MESSAGE_TYPES_H\n#define _CANLIB_MESSAGE_TYPES_H\n')
            for msg in rocketcan['messages']:
                print("#define MSG_" + msg['name'].data + " " + hex(msg['id'].data))

            print('')

            for board in rocketcan['boards']:
                print('#define BOARD_TYPE_ID_' + board['name'].data + ' ' + hex(board['id'].data))

            print('')

            for board in rocketcan['boards']:
                if "inst" in board:
                    inst_id = 1
                    for inst in board['inst']:
                        print('#define BOARD_INST_ID_' + board['name'].data + '_' + inst['name'].data + ' ' + hex(inst_id))
                        inst_id += 1
                    print('')

            for enum in rocketcan['enums']:
                first = True
                print('enum ' + enum['name'].data + ' {')
                for val in enum['value']:
                    if(first):
                        print('   ' + val['name'].data + ' = 0,')
                    else:
                        print('   ' + val['name'].data + ',')
                    first = False
                print('};\n')

            print('#endif')
        elif(args.format == 'message-types-py'):
            print('msg_type = {')
            for msg in rocketcan['messages']:
                print('    \'' + msg['name'].data + '\':' + hex(msg['id'].data) + ',')
            print('}')

            print('board_id = {')
            for board in rocketcan['boards']:
                print('    \'' + board['name'].data + '\':' + hex(board['id'].data) + ',')
            print('}')

            for enum in rocketcan['enums']:
                print(enum['name'].data + ' = {')
                enum_val_count = 0
                for val in enum['value']:
                    print('    \'' + val['name'].data + '\':' + hex(enum_val_count) + ',')
                    enum_val_count += 1
                print('}')

        else:
            print("Incorrect output format")

    except YAMLError as error:
        print(error)

if __name__ == '__main__':
    main()
