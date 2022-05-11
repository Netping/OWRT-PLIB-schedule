#!/usr/bin/python3
import os
import platform
import pkg_resources

# Информация о модулях и библиотеках которые должны быть установлены в зависимости от архитектуры устр-ва
arch_info = {
    'x86_64': {
        'modules_info': {
            'schedule': '1.1.0',
        },
        'modules_files_dir': '/usr/lib/python3.7/site-packages',
        'libs_info': [],
        'libs_files_dir': '',
    },
}

def get_arch():
    arch = platform.uname().machine
    return arch

def test_module_lib_exists():
    print("\n")
    try:
        arch_section = arch_info[get_arch()]
    except:
        print("unknown ARCHITECTURE :(")
        exit(-1)
    for module in arch_section['modules_info']:
        try:
            dist = pkg_resources.get_distribution(module)
            modname, modversion, modlocation = dist.key, dist.version, dist.location
            print(f"{module}: {modname} {modversion} {modlocation}")
            assert module == modname
            assert arch_section['modules_info'][module] == modversion
            assert arch_section['modules_files_dir'] == modlocation
        except:
            print(f"{module} did not pass the test")
            assert False
    for lib in arch_section['libs_info']:
        try:
            print(f"{lib}")
            isexists = os.path.exists(arch_section['libs_files_dir'] + lib)
            assert isexists
        except:
            print(f"{lib} did not pass the test")
            assert False