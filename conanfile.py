from conans import ConanFile, CMake, tools


class Crc32cConan(ConanFile):
    name = "crc32c"
    version = "1.0.5"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Crc32c here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        archive_url = 'https://github.com/google/crc32c/archive/{}.zip'.format(self.version)
        checksum = 'a4de99214639bb1530f73bfdba1873b5e7243bb4b5799fc0db1c7fbab5db7c52'
        tools.get(archive_url, sha256=checksum)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="crc32c")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*crc32c.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["crc32c"]
