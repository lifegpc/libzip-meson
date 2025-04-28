project('libzip', 'c', version: '1.11.3', meson_version: '>=1.3.0')

cc = meson.get_compiler('c')

deps = []
WIN32 = host_machine.system() in ['windows', 'cygwin']
MSVC = cc.get_id() == 'msvc'
conf = configuration_data()

enable_commoncrypto = get_option('enable_commoncrypto')
enable_gnutls = get_option('enable_gnutls')
enable_mbedtls = get_option('enable_mbedtls')
enable_openssl = get_option('enable_openssl')
have_crypto = false
if not enable_commoncrypto.disabled()
    commoncrypto_found = cc.has_header('CommonCrypto/CommonCrypto.h', required: enable_commoncrypto.enabled())
    if commoncrypto_found
        have_crypto = true
        conf.set10('HAVE_COMMONCRYPTO', true)
    endif
endif
if not have_crypto and WIN32 and get_option('enable_windows_crypto').allowed()
    have_crypto = true
    conf.set10('HAVE_WINDOWS_CRYPTO', true)
endif
if not have_crypto and not enable_openssl.disabled()
    crypto_dep = dependency('libcrypto', required: enable_openssl.enabled())
    if crypto_dep.found()
        have_crypto = true
        deps += [crypto_dep]
        conf.set10('HAVE_OPENSSL', true)
    endif
endif
if not have_crypto and not enable_gnutls.disabled()
    nettle_dep = dependency('nettle', required: enable_gnutls.enabled(), version: '>=3.0')
    gnutls_dep = dependency('gnutls', required: enable_gnutls.enabled())
    if nettle_dep.found() and gnutls_dep.found()
        have_crypto = true
        deps += [nettle_dep, gnutls_dep]
        conf.set10('HAVE_GNUTLS', true)
    endif
endif
if not have_crypto and not enable_mbedtls.disabled()
    mbedtls_dep = dependency('mbedtls', required: enable_mbedtls.enabled(), version: '>=1.0')
    if mbedtls_dep.found()
        have_crypto = true
        deps += [mbedtls_dep]
        conf.set10('HAVE_MBEDTLS', true)
    endif
endif
conf.set10('HAVE_CRYPTO', have_crypto)
mdoctool = find_program('mandoc', 'groff', required: false)
documentation_format = ''
if mdoctool.found()
    documentation_format = 'mdoc'
else
    MANTOOL = find_program('nroff', required: false)
    if MANTOOL.found()
        documentation_format = 'man'
    else
        documentation_format = 'html'
    endif
endif
python3 = find_program('python3', required: true)
archive_name = meson.project_name() + '-' + meson.project_version()
run_target('dist_', command: [python3, meson.current_source_dir() + '/' + 'dist.py', archive_name], env:['BUILDROOT=' + meson.global_build_root(), 'CURRENT=' + meson.current_source_dir()])
# TODO: Add distcheck

conf.set10('ENABLE_FDOPEN', get_option('enable_fdopen'))
conf.set('CMAKE_PROJECT_NAME', meson.project_name())
conf.set('CMAKE_PROJECT_VERSION', meson.project_version())
conf.set('libzip_VERSION', meson.project_version())
conf.set('libzip_VERSION_MAJOR', meson.project_version().split('.')[0])
conf.set('libzip_VERSION_MINOR', meson.project_version().split('.')[1])
libzip_version_patch = '0'
if meson.project_version().split('.').length() > 2
    libzip_version_patch = meson.project_version().split('.')[2]
endif
conf.set('libzip_VERSION_PATCH', libzip_version_patch)
add_project_arguments('-D__STDC_WANT_LIB_EXT1__=1', language: 'c')
default_library = get_option('default_library')
if default_library == 'shared' or default_library == 'both'
    shared_library = true
    conf.set10('ZIP_STATIC', false)
else
    shared_library = false
    conf.set10('ZIP_STATIC', true)
endif

conf.set10('HAVE__CLOSE', cc.has_function('_close'))
conf.set10('HAVE__DUP', cc.has_function('_dup'))
conf.set10('HAVE__FDOPEN', cc.has_function('_fdopen'))
conf.set10('HAVE__FILENO', cc.has_function('_fileno'))
conf.set10('HAVE__FSEEKI64', cc.has_function('_fseeki64'))
conf.set10('HAVE__FSTAT64', cc.has_function('_fstat64'))
conf.set10('HAVE__SETMODE', cc.has_function('_setmode'))
conf.set10('HAVE__STAT64', cc.has_function('_stat64'))
conf.set10('HAVE__SNPRINTF', cc.has_header_symbol('stdio.h', '_snprintf'))
conf.set10('HAVE__SNPRINTF_S', cc.has_header_symbol('stdio.h', '_snprintf_s'))
conf.set10('HAVE__SNWPRINTF_S', cc.has_header_symbol('stdio.h', '_snwprintf_s'))
conf.set10('HAVE__STRDUP', cc.has_function('_strdup'))
conf.set10('HAVE__STRICMP', cc.has_header_symbol('string.h', '_stricmp'))
conf.set10('HAVE__STRTOI64', cc.has_function('_strtoi64'))
conf.set10('HAVE__STRTOUI64', cc.has_function('_strtoui64'))
conf.set10('HAVE__UNLINK', cc.has_function('_unlink'))
conf.set10('HAVE_ARC4RANDOM', cc.has_function('arc4random'))
conf.set10('HAVE_CLONEFILE', cc.has_function('clonefile'))
conf.set10('HAVE_EXPLICIT_BZERO', cc.has_function('explicit_bzero'))
conf.set10('HAVE_EXPLICIT_MEMSET', cc.has_function('explicit_memset'))
conf.set10('HAVE_FCHMOD', cc.has_function('fchmod'))
conf.set10('HAVE_FILENO', cc.has_function('fileno'))
conf.set10('HAVE_FSEEKO', cc.has_function('fseeko'))
conf.set10('HAVE_FTELLO', cc.has_function('ftello'))
conf.set10('HAVE_GETPROGNAME', cc.has_function('getprogname'))
conf.set10('HAVE_GETSECURITYINFO', cc.has_function('GetSecurityInfo'))
conf.set10('HAVE_LOCALTIME_R', cc.has_header_symbol('time.h', 'localtime_r'))
conf.set10('HAVE_LOCALTIME_S', cc.has_header_symbol('time.h', 'localtime_s'))
conf.set10('HAVE_MEMCPY_S', cc.has_function('memcpy_s'))
conf.set10('HAVE_RANDOM', cc.has_function('random'))
conf.set10('HAVE_SETMODE', cc.has_function('setmode'))
conf.set10('HAVE_SNPRINTF', cc.has_header_symbol('stdio.h', 'snprintf'))
conf.set10('HAVE_SNPRINTF_S', cc.has_header_symbol('stdio.h', 'snprintf_s'))
conf.set10('HAVE_STRCASECMP', cc.has_header_symbol('strings.h', 'strcasecmp'))
conf.set10('HAVE_STRDUP', cc.has_function('strdup'))
conf.set10('HAVE_STRERROR_S', cc.has_function('strerror_s'))
conf.set10('HAVE_STRERRORLEN_S', cc.has_function('strerrorlen_s'))
conf.set10('HAVE_STRICMP', cc.has_function('stricmp'))
conf.set10('HAVE_STRNCPY_S', cc.has_function('strncpy_s'))
conf.set10('HAVE_STRTOLL', cc.has_function('strtoll'))
conf.set10('HAVE_STRTOULL', cc.has_function('strtoull'))
conf.set10('HAVE_FTS_H', cc.check_header('sys/types.h') and cc.check_header('sys/stat.h') and cc.check_header('fts.h'))
conf.set10('HAVE_LIB_FTS', false)
if conf.get('HAVE_FTS_H') == 1
    conf.set10('HAVE_FTS_OPEN', cc.has_function('fts_open'))
    if conf.get('HAVE_FTS_OPEN') == 0
        fts = cc.find_library('fts')
        conf.set10('HAVE_LIB_FTS', fts.found())
    endif
endif

FTS_LIB = ''
if conf.get('HAVE_LIB_FTS') == 1
    FTS_LIB = 'fts'
endif

conf.set10('HAVE_STDBOOL_H', cc.check_header('stdbool.h'))
conf.set10('HAVE_STRINGS_H', cc.check_header('strings.h'))
conf.set10('HAVE_UNISTD_H', cc.check_header('unistd.h'))

conf.set10('HAVE_INTTYPES_H_LIBZIP', cc.check_header('inttypes.h'))
conf.set10('HAVE_STDINT_H_LIBZIP', cc.check_header('stdint.h'))
conf.set10('HAVE_SYS_TYPES_H_LIBZIP', cc.check_header('sys/types.h'))

conf.set10('HAVE___PROGNAME', cc.has_header_symbol('stdlib.h', '__progname'))

conf.set('__INT8_LIBZIP', cc.sizeof('__int8'))
conf.set('INT8_T_LIBZIP', cc.sizeof('int8_t', prefix: '#include<stdint.h>'))
conf.set('UINT8_T_LIBZIP', cc.sizeof('uint8_t', prefix: '#include<stdint.h>'))
conf.set('__INT16_LIBZIP', cc.sizeof('__int16'))
conf.set('INT16_T_LIBZIP', cc.sizeof('int16_t', prefix: '#include<stdint.h>'))
conf.set('UINT16_T_LIBZIP', cc.sizeof('uint16_t', prefix: '#include<stdint.h>'))
conf.set('__INT32_LIBZIP', cc.sizeof('__int32'))
conf.set('INT32_T_LIBZIP', cc.sizeof('int32_t', prefix: '#include<stdint.h>'))
conf.set('UINT32_T_LIBZIP', cc.sizeof('uint32_t', prefix: '#include<stdint.h>'))
conf.set('__INT64_LIBZIP', cc.sizeof('__int64'))
conf.set('INT64_T_LIBZIP', cc.sizeof('int64_t', prefix: '#include<stdint.h>'))
conf.set('UINT64_T_LIBZIP', cc.sizeof('uint64_t', prefix: '#include<stdint.h>'))
conf.set('SHORT_LIBZIP', cc.sizeof('short'))
conf.set('INT_LIBZIP', cc.sizeof('int'))
conf.set('LONG_LIBZIP', cc.sizeof('long'))
conf.set('LONG_LONG_LIBZIP', cc.sizeof('long long'))
conf.set('SIZEOF_OFF_T', cc.sizeof('off_t', prefix: '#include<sys/types.h>'))
conf.set('SIZEOF_SIZE_T', cc.sizeof('size_t'))

conf.set('HAVE_FICLONERANGE', cc.compiles('''#include <sys/ioctl.h>
#include <linux/fs.h>
int main(int argc, char *argv[]) { unsigned long x = FICLONERANGE; }'''))

conf.set10('WORDS_BIGENDIAN', host_machine.endian() == 'big')
zlib_dep = dependency('zlib', required: true, version: '>=1.1.2')
deps += zlib_dep

enable_bzip2 = get_option('enable_bzip2')
if not enable_bzip2.disabled()
    bzip2_dep = dependency('bzip2', required: enable_bzip2.enabled())
    conf.set10('HAVE_LIBBZ2', bzip2_dep.found())
    if bzip2_dep.found()
        deps += [bzip2_dep]
    else
        warning('-- bzip2 library not found; bzip2 support disabled')
    endif
endif

enable_lzma = get_option('enable_lzma')
if not enable_lzma.disabled()
    lzma_dep = dependency('liblzma', required: enable_lzma.enabled())
    conf.set10('HAVE_LIBLZMA', lzma_dep.found())
    if lzma_dep.found()
        deps += [lzma_dep]
    else
        warning('-- lzma library not found; lzma/xz support disabled')
    endif
endif

enable_zstd = get_option('enable_zstd')
if not enable_zstd.disabled()
    zstd_dep = dependency('zstd', required: enable_zstd.enabled())
    conf.set10('HAVE_LIBZSTD', zstd_dep.found())
    if zstd_dep.found()
        deps += [zstd_dep]
    else
        warning('-- zstd library not found; zstandard support disabled')
    endif
endif

if not have_crypto
    warning('-- neither Common Crypto, GnuTLS, mbed TLS, OpenSSL, nor Windows Cryptography found; AES support disabled')
endif

if MSVC
    add_project_arguments('-D_CRT_SECURE_NO_WARNINGS', '-D_CRT_NONSTDC_NO_DEPRECATE', language: 'c')
endif

if WIN32 and get_option('enable_uwp')
    add_project_arguments('-DMS_UWP', language: 'c')
endif

install_rpath = get_option('prefix') + '/' + get_option('libdir')

do_install_f = get_option('do_install')
if do_install_f.auto()
    do_install = not meson.is_subproject()
else
    do_install = do_install_f.enabled()
endif

subdir('lib')

if conf.get('HAVE_INTTYPES_H_LIBZIP') == 1
    conf.set('LIBZIP_TYPES_INCLUDE', '''#if !defined(__STDC_FORMAT_MACROS)
#define __STDC_FORMAT_MACROS 1
#endif
#include <inttypes.h>''')
elif conf.get('HAVE_STDINT_H_LIBZIP') == 1
    conf.set('LIBZIP_TYPES_INCLUDE', '#include <stdint.h>')
elif conf.get('HAVE_SYS_TYPES_H_LIBZIP') == 1
    conf.set('LIBZIP_TYPES_INCLUDE', '#include <sys/types.h>')
else
    conf.set('LIBZIP_TYPES_INCLUDE', '')
endif

if conf.get('INT8_T_LIBZIP') != -1
    conf.set('ZIP_INT8_T', 'int8_t')
elif conf.get('__INT8_LIBZIP') != -1
    conf.set('ZIP_INT8_T', '__int8')
else
    conf.set('ZIP_INT8_T', 'signed char')
endif

if conf.get('UINT8_T_LIBZIP') != -1
    conf.set('ZIP_UINT8_T', 'uint8_t')
elif conf.get('__INT8_LIBZIP') != -1
    conf.set('ZIP_UINT8_T', 'unsigned __int8')
else
    conf.set('ZIP_UINT8_T', 'unsigned char')
endif

if conf.get('INT16_T_LIBZIP') != -1
    conf.set('ZIP_INT16_T', 'int16_t')
elif conf.get('__INT16_LIBZIP') != -1
    conf.set('ZIP_INT16_T', '__int16')
elif conf.get('SHORT_LIBZIP') == 2
    conf.set('ZIP_INT16_T', 'short')
endif

if conf.get('UINT16_T_LIBZIP') != -1
    conf.set('ZIP_UINT16_T', 'uint16_t')
elif conf.get('__INT16_LIBZIP') != -1
    conf.set('ZIP_UINT16_T', 'unsigned __int16')
elif conf.get('SHORT_LIBZIP') == 2
    conf.set('ZIP_UINT16_T', 'unsigned short')
endif

if conf.get('INT32_T_LIBZIP') != -1
    conf.set('ZIP_INT32_T', 'int32_t')
elif conf.get('__INT32_LIBZIP') != -1
    conf.set('ZIP_INT32_T', '__int32')
elif conf.get('INT_LIBZIP') == 4
    conf.set('ZIP_INT32_T', 'int')
elif conf.get('LONG_LIBZIP') == 4
    conf.set('ZIP_INT32_T', 'long')
endif

if conf.get('UINT32_T_LIBZIP') != -1
    conf.set('ZIP_UINT32_T', 'uint32_t')
elif conf.get('__INT32_LIBZIP') != -1
    conf.set('ZIP_UINT32_T', 'unsigned __int32')
elif conf.get('INT_LIBZIP') == 4
    conf.set('ZIP_UINT32_T', 'unsigned int')
elif conf.get('LONG_LIBZIP') == 4
    conf.set('ZIP_UINT32_T', 'unsigned long')
endif

if conf.get('INT64_T_LIBZIP') != -1
    conf.set('ZIP_INT64_T', 'int64_t')
elif conf.get('__INT64_LIBZIP') != -1
    conf.set('ZIP_INT64_T', '__int64')
elif conf.get('LONG_LIBZIP') == 8
    conf.set('ZIP_INT64_T', 'long')
elif conf.get('LONG_LONG_LIBZIP') == 8
    conf.set('ZIP_INT64_T', 'long long')
endif

if conf.get('UINT64_T_LIBZIP') != -1
    conf.set('ZIP_UINT64_T', 'uint64_t')
elif conf.get('__INT64_LIBZIP') != -1
    conf.set('ZIP_UINT64_T', 'unsigned __int64')
elif conf.get('LONG_LIBZIP') == 8
    conf.set('ZIP_UINT64_T', 'unsigned long')
elif conf.get('LONG_LONG_LIBZIP') == 8
    conf.set('ZIP_UINT64_T', 'unsigned long long')
endif

configure_file(input: 'config.h.in', output: 'config.h', configuration: conf, format: 'cmake@')
configure_file(input: 'zipconf.h.in', output: 'zipconf.h', configuration: conf, format: 'cmake')

if do_install
    install_headers(meson.current_build_dir() + '/zipconf.h')
    pkg = import('pkgconfig')
    pkg.generate(zip, name: 'libzip', description: 'library for handling zip archives')
endif
