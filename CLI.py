import argparse
from MyServer import runServer,createServer

def processArgs(action:str,complement:str):
    action = action.lower()
    complement = complement.lower()
    if action == 'run':
        if complement == 'server':
            print('[Starting] Initializing server...')
            runServer()
    elif action == 'regen':
        if complement == 'all':
            print('[Starting] Regenerating DataBases...')
        else:
            print('[Starting] Regenerating' + complement)
    elif action == 'create':
        if complement == 'admin':
            print('[Starting] Creating Admin profile')
        elif complement == 'table':
            print('[Starting] Creatings table...')
        elif complement == 'server':
            print('[Starting] Creating server by default...')
            createServer()
    pass

def cli():
    parser = argparse.ArgumentParser(
        prog='Server',
        description='Server CLI implementation'
    )
    parser.add_argument(
        'action',
        help='Action to realize',
    )
    parser.add_argument(
        'complement',
        help='Specify the action to realize'
    )
    return parser.parse_args()

def main():
    args = cli()
    processArgs(args.action,args.complement)
    pass

if __name__ == '__main__':
    main()