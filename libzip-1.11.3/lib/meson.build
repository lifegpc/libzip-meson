sources = files([
    'zip_add.c',
    'zip_add_dir.c',
    'zip_add_entry.c',
    'zip_algorithm_deflate.c',
    'zip_buffer.c',
    'zip_close.c',
    'zip_delete.c',
    'zip_dir_add.c',
    'zip_dirent.c',
    'zip_discard.c',
    'zip_entry.c',
    'zip_error.c',
    'zip_error_clear.c',
    'zip_error_get.c',
    'zip_error_get_sys_type.c',
    'zip_error_strerror.c',
    'zip_error_to_str.c',
    'zip_extra_field.c',
    'zip_extra_field_api.c',
    'zip_fclose.c',
    'zip_fdopen.c',
    'zip_file_add.c',
    'zip_file_error_clear.c',
    'zip_file_error_get.c',
    'zip_file_get_comment.c',
    'zip_file_get_external_attributes.c',
    'zip_file_get_offset.c',
    'zip_file_rename.c',
    'zip_file_replace.c',
    'zip_file_set_comment.c',
    'zip_file_set_encryption.c',
    'zip_file_set_external_attributes.c',
    'zip_file_set_mtime.c',
    'zip_file_strerror.c',
    'zip_fopen.c',
    'zip_fopen_encrypted.c',
    'zip_fopen_index.c',
    'zip_fopen_index_encrypted.c',
    'zip_fread.c',
    'zip_fseek.c',
    'zip_ftell.c',
    'zip_get_archive_comment.c',
    'zip_get_archive_flag.c',
    'zip_get_encryption_implementation.c',
    'zip_get_file_comment.c',
    'zip_get_name.c',
    'zip_get_num_entries.c',
    'zip_get_num_files.c',
    'zip_hash.c',
    'zip_io_util.c',
    'zip_libzip_version.c',
    'zip_memdup.c',
    'zip_name_locate.c',
    'zip_new.c',
    'zip_open.c',
    'zip_pkware.c',
    'zip_progress.c',
    'zip_rename.c',
    'zip_replace.c',
    'zip_set_archive_comment.c',
    'zip_set_archive_flag.c',
    'zip_set_default_password.c',
    'zip_set_file_comment.c',
    'zip_set_file_compression.c',
    'zip_set_name.c',
    'zip_source_accept_empty.c',
    'zip_source_begin_write.c',
    'zip_source_begin_write_cloning.c',
    'zip_source_buffer.c',
    'zip_source_call.c',
    'zip_source_close.c',
    'zip_source_commit_write.c',
    'zip_source_compress.c',
    'zip_source_crc.c',
    'zip_source_error.c',
    'zip_source_file_common.c',
    'zip_source_file_stdio.c',
    'zip_source_free.c',
    'zip_source_function.c',
    'zip_source_get_dostime.c',
    'zip_source_get_file_attributes.c',
    'zip_source_is_deleted.c',
    'zip_source_layered.c',
    'zip_source_open.c',
    'zip_source_pass_to_lower_layer.c',
    'zip_source_pkware_decode.c',
    'zip_source_pkware_encode.c',
    'zip_source_read.c',
    'zip_source_remove.c',
    'zip_source_rollback_write.c',
    'zip_source_seek.c',
    'zip_source_seek_write.c',
    'zip_source_stat.c',
    'zip_source_supports.c',
    'zip_source_tell.c',
    'zip_source_tell_write.c',
    'zip_source_window.c',
    'zip_source_write.c',
    'zip_source_zip.c',
    'zip_source_zip_new.c',
    'zip_stat.c',
    'zip_stat_index.c',
    'zip_stat_init.c',
    'zip_strerror.c',
    'zip_string.c',
    'zip_unchange.c',
    'zip_unchange_all.c',
    'zip_unchange_archive.c',
    'zip_unchange_data.c',
    'zip_utf-8.c',
])

defs = []
zip_deps = deps

if WIN32
    defs += '-DWIN32_LEAN_AND_MEAN'
    sources += files([
        'zip_source_file_win32.c',
        'zip_source_file_win32_named.c',
        'zip_source_file_win32_utf16.c',
        'zip_source_file_win32_utf8.c',
    ])
    if get_option('enable_uwp')
        sources += files([
            'zip_random_uwp.c',
        ])
    else
        sources += files([
            'zip_source_file_win32_ansi.c',
            'zip_random_win32.c',
        ])
        zip_deps += cc.find_library('advapi32', required: true)
    endif
else
    sources += files([
        'zip_source_file_stdio_named.c',
        'zip_random_unix.c',
    ])
endif

if conf.has('HAVE_LIBBZ2') and conf.get('HAVE_LIBBZ2') == 1
    sources += files(['zip_algorithm_bzip2.c'])
endif

if conf.has('HAVE_LIBLZMA') and conf.get('HAVE_LIBLZMA') == 1
    sources += files(['zip_algorithm_xz.c'])
endif

if conf.has('HAVE_LIBZSTD') and conf.get('HAVE_LIBZSTD') == 1
    sources += files(['zip_algorithm_zstd.c'])
endif

if conf.has('HAVE_COMMONCRYPTO') and conf.get('HAVE_COMMONCRYPTO') == 1
    sources += files(['zip_crypto_commoncrypto.c'])
elif conf.has('HAVE_WINDOWS_CRYPTO') and conf.get('HAVE_WINDOWS_CRYPTO') == 1
    sources += files(['zip_crypto_win.c'])
elif conf.has('HAVE_GNUTLS') and conf.get('HAVE_GNUTLS') == 1
    sources += files(['zip_crypto_gnutls.c'])
elif conf.has('HAVE_OPENSSL') and conf.get('HAVE_OPENSSL') == 1
    sources += files(['zip_crypto_openssl.c'])
elif conf.has('HAVE_MBEDTLS') and conf.get('HAVE_MBEDTLS') == 1
    sources += files(['zip_crypto_mbedtls.c'])
endif

if conf.has('HAVE_CRYPTO') and conf.get('HAVE_CRYPTO') == 1
    sources += files(['zip_winzip_aes.c', 'zip_source_winzip_aes_decode.c', 'zip_source_winzip_aes_encode.c'])
endif

if do_install
    install_headers('zip.h')
endif

cmake = find_program('cmake')
gen_path = meson.project_source_root() + '/cmake/GenerateZipErrorStrings.cmake'
gen_err_str = custom_target(command: [cmake, '-DPROJECT_SOURCE_DIR=' + meson.project_source_root(), '-DCURRENT_BINARY_DIR=' + meson.current_build_dir(), '-P', gen_path], output: 'zip_err_str.c', env: ['PWD=' + meson.current_build_dir()])
sources += gen_err_str

fs = import('fs')
pbdir = fs.parent(meson.current_build_dir())
if pbdir.startswith(meson.global_source_root())
    pbdir = fs.relative_to(pbdir, meson.current_source_dir())
endif
incdir = include_directories(pbdir)

soversion = ''
if get_option('shared_lib_versionning')
    soversion = 5
endif

zip = library('zip',
    sources,
    include_directories: incdir,
    c_static_args: ['-DZIP_STATIC'],
    c_shared_args: ['-DHAVE_SHARED'],
    dependencies: zip_deps,
    c_args: defs,
    gnu_symbol_visibility: 'hidden',
    pic: true,
    install: do_install,
    install_rpath: install_rpath,
    soversion: soversion,
    version: '5.5',
)

libzip_dep = declare_dependency(include_directories: include_directories('.', pbdir), link_with: zip)
