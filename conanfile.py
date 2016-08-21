from conans import ConanFile, ConfigureEnvironment
from conans.tools import download, unzip, untargz
import os

class FlexConan(ConanFile):
    name = "flex"
    version = "2.6.0"
    url = "https://github.com/lucteo/conan-flex.git"
    license = "GNU General Public License: https://www.gnu.org/licenses/gpl.html"
    settings = "os", "compiler", "build_type", "arch"
    exports = "*"
    requires = "bison/3.0.4@lucteo/stable"
    build_policy = "missing"

    archiveName = "flex-2.6.0.tar.gz"
    folderName = "flex-2.6.0"

    def source(self):
        download("http://sourceforge.net/projects/flex/files/flex-2.6.0.tar.gz/download", self.archiveName)
        untargz(self.archiveName)
        os.unlink(self.archiveName)
        if self.settings.os != "Windows":
            self.run("chmod +x ./%s/configure" % self.folderName)

    def build(self):
        if self.settings.os == "Linux" or self.settings.os == "Macos":
            env = ConfigureEnvironment(self.deps_cpp_info, self.settings)
            env_line = env.command_line
                        
            self.run("cd %s && %s ./configure --prefix=%s/out" % (self.folderName, env_line, self.conanfile_directory))
            self.run("cd %s && %s make" % (self.folderName, env_line))            
            self.run("cd %s && %s make install " % (self.folderName, env_line))            

    def package(self):
        self.copy("*", dst="", src="out")

    def package_info(self):
        # Don't list the libraries generated; flex is mainly used as a tool
        # self.cpp_info.libs = ['fl', 'fl_pic']  # The libs to link against
        # self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
        self.cpp_info.resdirs = ['share/flex']  # Directories where resources, data, etc can be found
        self.cpp_info.bindirs = ['bin']  # Directories where executables and shared libs can be found
