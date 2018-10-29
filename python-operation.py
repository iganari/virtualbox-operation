#!/usr/bin/env python
# conding: utf-8

# 
# vb command
#

import os
import sys
# import pdb

# Usage
usage = """
Description: Manage commands for VirtualBox.

    Usage: $ vb

  Options: -h : show this help message and exit

"""

def chk_tmp_permission():
    
    chk_write = os.access('/tmp', os.W_OK)

    if chk_write is True:
        print('OK. You have Write Permisson')
        # pass
    else:
        print('NO, You do not have Write Permisson')
        sys.exit(0)

def chk_vb_command():
    import subprocess
    
    paths = [ "/usr/bin/", "/usr/local/bin/" ]

    for path in paths: 
        vb_cmd = path + 'VBoxManage'
        if os.path.isfile(vb_cmd) is True:
            # print('OK')
            # print(vb_cmd)
            break    # After this, vb_cmd exists in reality.
        else:
            print('Maybe, You do not install Virtualbox ( We could not find ' + vb_cmd + ' )')
    else:
        print('You do not install Virtualbox. Bye!')
        sys.exit(0)
    # print(vb_cmd)
    return vb_cmd

def exe_vm():
    cmd = chk_vb_command()
    print(cmd)    

    import subprocess
   
    try:
      # res = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE)
      # res = subprocess.run([ cmd, "list", "vms" ], stdout=subprocess.PIPE)
      res = subprocess.run([ cmd, "list", "vms" ], stdout=subprocess.PIPE)
      sys.stdout.buffer.write(res.stdout) # 標準出力としてターミナルに出力する
    except:
      print('Error')

def test_print():
    print('\n\n## Virtual Box List ##\n')
    print('-------------------------------------------------------')
    print(' <--- [   ALL VM   ]      |    [   Running VM   ] ---> ')     
    print('-------------------------------------------------------\n')


# main
def main():

    # Confirm whether you have write permission for /tmp
    chk_tmp_permission()

    # Check if VBoxManage is installed
    # chk_vb_command()

    # 
    # pdb.set_trace()
    exe_vm()

    # test print
    test_print()
    # test
    print('END')

if __name__ == '__main__':
    main()
