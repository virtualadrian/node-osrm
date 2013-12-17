{
  'includes': [ 'common.gypi' ],
  'variables': {
      "module_name":"osrm",
      "module_path":"./lib/",
      'cwd%':'<!(pwd)',
      'std%':'ansi'
  },
  'targets': [
    {
      'target_name': '<(module_name)',
      'include_dirs': [
          '<@(cwd)/../Project-OSRM/Library/',
          './src/'
      ],
      'libraries': [
        '-L<@(cwd)/../Project-OSRM/build',
        '-lOSRM',
        '-lboost_program_options',
        '-lboost_regex',
        '-lboost_thread',
        '-lboost_system',
        '-lboost_filesystem',
        '<@(cwd)/../Project-OSRM/build/libUUID.a',
        '<@(cwd)/../Project-OSRM/build/libGITDESCRIPTION.a'
      ],
      'conditions': [
        [ 'OS=="linux"', {
          'libraries+':[
              '-Wl,-rpath=<@(cwd)/../Project-OSRM/build',
          ]}
        ],
        ['std == "c++11"', {
            'cflags_cc' : [
                '-std=c++11',
            ],
            'xcode_settings': {
              'OTHER_CPLUSPLUSFLAGS':['-std=c++11','-stdlib=libc++'],
              'OTHER_CPLUSPLUSFLAGS':['-stdlib=libc++'],
              'OTHER_LDFLAGS':['-stdlib=libc++'],
              'CLANG_CXX_LANGUAGE_STANDARD':'c++11',
              'MACOSX_DEPLOYMENT_TARGET':'10.7'
            }
        }
        ]
      ],
      'sources': [
        "src/node_osrm.cpp"
      ],
      'cflags_cc!': ['-fno-rtti', '-fno-exceptions'],
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS':['-Wno-unneeded-internal-declaration', '-Wno-unknown-pragmas'],
        'GCC_ENABLE_CPP_RTTI': 'YES',
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
      }
    },
    {
      'target_name': 'action_after_build',
      'type': 'none',
      'dependencies': [ '<(module_name)' ],
      'copies': [
          {
            'files': [ '<(PRODUCT_DIR)/<(module_name).node' ],
            'destination': '<(module_path)'
          }
      ]
    }
  ]
}
