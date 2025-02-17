import argparse
from strictyaml import load,Map,Str,HexInt,Int,Seq,YAMLError,Optional

from message_types_h import gen_message_types_h
from message_types_py import gen_message_types_py
from rst import gen_board_id_rst, gen_packet_format_rst

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
            Optional("field"):Seq(Map({
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
            Optional("doc-link"):Str(),
            Optional("inst"):Seq(Map({
                "name":Str(),
                "desc":Str(),
            }))
        })),
        "enums" : Seq(Map({
            "name":Str(),
            "desc":Str(),
            "prefix":Str(),
            "value":Seq(Map({
                "name":Str(),
                Optional("value"):Int(),
                Optional("desc"):Str()
            }))
        }))
    })

    try:
        rocketcan = load(yaml_str,schema)

        if(args.format == 'message-types-h'):
            gen_message_types_h(rocketcan)
        elif(args.format == 'message-types-py'):
            gen_message_types_py(rocketcan)
        elif(args.format == 'board-id-rst'):
            gen_board_id_rst(rocketcan)
        elif(args.format == 'packet-format-rst'):
            gen_packet_format_rst(rocketcan)
        else:
            print("Incorrect output format")

    except YAMLError as error:
        print(error)

if __name__ == '__main__':
    main()
