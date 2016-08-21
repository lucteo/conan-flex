from conans import ConanFile, CMake
import os

############### CONFIGURE THESE VALUES ##################
default_user = "lucteo"
default_channel = "testing"
#########################################################

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)

class TestFlexConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "flex/2.6.0@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.output.info("Running CMake")
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.output.info("Building the flex test project")
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.output.info("Running smoke test")
        if self.settings.os == "Windows":
            self.run('type %s/basic_nr.txt | ./bin/test-flex' % self.conanfile_directory)
        else:
            self.run('cat %s/basic_nr.txt | ./bin/test-flex' % self.conanfile_directory)

