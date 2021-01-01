from conans import ConanFile, CMake, tools


class BabelcConan(ConanFile):
    name = "babelc"
    version = "0.8.37"
    license = "GPL"
    homepage = "https://github.com/fmtlib/fmt"
    author = "Matias Sjösvärd (mr@seasword.com)"
    url = "https://bitbucket.org/MrSeasword/babelc.git"
    description = "babelc is a tool for using C++ declarations"
    topics = ("dBus", "json", "streams")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://bitbucket.org/MrSeasword/babelc.git babelc_src")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="babelc_src")
        cmake.build()


    def package(self):
        self.copy("babelc",src="./",dst="bin",keep_path=False)
        self.copy("*.pdf",dst="bin",keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["babelc"]

    def deploy(self):
        self.copy("*",src="bin",dst="bin")


