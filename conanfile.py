from conans import ConanFile, CMake, tools


class Crc32cConan(ConanFile):
    name = "crc32c"
    version = "1.0.5"
    license = "BSD-3-Clause"
    author = "Kyle Ambroff-Kao <kyle@ambroffkao.com>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Crc32c here>"
    topics = ('conan', 'crc32c')
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], 'fPIC': [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        archive_url = 'https://github.com/google/crc32c/archive/{}.zip'.format(
            self.version)
        checksum = 'a4de99214639bb1530f73bfdba1873b5e7243bb4b5799fc0db1c7fbab5db7c52'
        tools.get(archive_url, sha256=checksum)

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure(
            source_folder='crc32c-{}'.format(self.version),
            defs={
                'CRC32C_BUILD_TESTS': False,
                'CRC32C_BUILD_BENCHMARKS': False,
                'CRC32C_USE_GLOG': False})
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        self.copy("*.h", dst="include", src="hello")
        self.copy("*crc32c.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["crc32c"]
