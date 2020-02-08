# [rights]  Copyright 2020 brianddk at github https://github.com/brianddk
# [license] Apache 2.0 License https://www.apache.org/licenses/LICENSE-2.0
# [repo]    https://github.com/brianddk/pypaperwallet
# [btc]     BTC-b32: bc1qwc2203uym96u0nmq04pcgqfs9ldqz9l3mz8fpj
# [tipjar]  https://gist.github.com/brianddk/3ec16fbf1d008ea290b0

# [Chocolatey] choco install -y msys2
# [MSYS2]      pacman -S mingw-w64-x86_64-gtk3
# python37 -m pip install WeasyPrint mnemoic qrcode[pil] pycoin
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall\{7dcd91a2-41cd-4c70-8641-3ec79e4e686e}

# TODO
# from pycoin import __path__ as pycoin_path                                                                                        
# from pkgutil import iter_modules                                                                                                                    
# from importlib import import_module
# g = pkgutil.iter_modules([pycoin_path[0] + r"\symbols"])                                                                          
# for i in g:                                                                                                         
    # listvar.append(import_module('pycoin.symbols.' + i.name, 'network'))

from pypaperwallet.pdf_wallet import mk_wallet

mk_wallet('sample.pdf')
