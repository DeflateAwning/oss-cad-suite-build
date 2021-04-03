from src.base import SourceLocation, Target

# dfu-util

SourceLocation(
	name = 'dfu-util',
	vcs = 'git',
	location = 'https://git.code.sf.net/p/dfu-util/dfu-util',
	revision = 'origin/master'
)

Target(
	name = 'dfu-util',
	sources = [ 'dfu-util' ],
	license_file = 'dfu-util/COPYING',
)

# ecpdap

SourceLocation(
	name = 'ecpdap',
	vcs = 'git',
	location = 'https://github.com/adamgreig/ecpdap',
	revision = 'origin/master',
)

Target(
	name = 'ecpdap',
	sources = [ 'ecpdap' ],
	license_file = 'ecpdap/LICENSE-MIT',
)

# ecpprog

SourceLocation(
	name = 'ecpprog',
	vcs = 'git',
	location = 'https://github.com/gregdavill/ecpprog',
	revision = 'origin/master'
)

Target(
	name = 'ecpprog',
	sources = [ 'ecpprog' ],
	license_file = 'ecpprog/COPYING',
)

# fujprog

SourceLocation(
	name = 'fujprog',
	vcs = 'git',
	location = 'https://github.com/kost/fujprog',
	revision = 'origin/master'
)

Target(
	name = 'fujprog',
	sources = [ 'fujprog' ],
	patches = [ 'Toolchain-mingw64.cmake' ],
	license_file = 'fujprog/LICENSE',
)

# openfpgaloader

SourceLocation(
	name = 'openfpgaloader',
	vcs = 'git',
	location = 'https://github.com/trabucayre/openFPGALoader',
	revision = 'origin/master',
)

Target(
	name = 'openfpgaloader',
	sources = [ 'openfpgaloader' ],
	license_file = 'openfpgaloader/LICENSE',
)

# python based programmers

SourceLocation(
	name = 'black-iceprog',
	vcs = 'git',
	location = 'https://github.com/jpenalbae/black-iceprog',
	revision = 'origin/master',
)

SourceLocation(
	name = 'icefunprog',
	vcs = 'git',
	location = 'https://github.com/pitrz/icefunprog',
	revision = 'origin/master',
)

SourceLocation(
	name = 'tinyfpgab',
	vcs = 'git',
	location = 'https://github.com/tinyfpga/TinyFPGA-B-Series',
	revision = 'origin/master',
)

SourceLocation(
	name = 'tinyprog',
	vcs = 'git',
	location = 'https://github.com/tinyfpga/TinyFPGA-Bootloader',
	revision = 'origin/master',
)

Target(
	name = 'python-programmers',
	sources = [ 'black-iceprog', 'icefunprog', 'tinyfpgab', 'tinyprog'],
    dependencies = [ 'python3' ],
	patches = [ 'python3_package.sh' ],
	resources = [ 'python3' ],
)

# openocd

SourceLocation(
	name = 'openocd',
	vcs = 'git',
	location = 'https://repo.or.cz/openocd.git',
	revision = 'origin/master',
)

Target(
	name = 'openocd',
	sources = [ 'openocd' ],
	patches = [ 'openocd.diff' ],
	license_file = 'openocd/COPYING',
)

# icesprog

SourceLocation(
	name = 'icesprog',
	vcs = 'git',
	location = 'https://github.com/wuxx/icesugar',
	revision = 'origin/master',
	no_submodules = True,
)

Target(
	name = 'icesprog',
	sources = [ 'icesprog' ],
)
