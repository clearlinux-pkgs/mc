#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mc
Version  : 4.8.24
Release  : 24
URL      : http://ftp.midnight-commander.org/mc-4.8.24.tar.xz
Source0  : http://ftp.midnight-commander.org/mc-4.8.24.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: mc-bin = %{version}-%{release}
Requires: mc-data = %{version}-%{release}
Requires: mc-libexec = %{version}-%{release}
Requires: mc-license = %{version}-%{release}
Requires: mc-locales = %{version}-%{release}
Requires: mc-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : check
BuildRequires : flex
BuildRequires : glib-dev
BuildRequires : libssh2-dev
BuildRequires : slang-dev
Patch1: 0001-Support-stateless-fallback-of-mc-configuration.patch

%description
Contents
--------
Introduction
Dependencies
Features
Mini-documentation
Where to get more information
Reporting problems

%package bin
Summary: bin components for the mc package.
Group: Binaries
Requires: mc-data = %{version}-%{release}
Requires: mc-libexec = %{version}-%{release}
Requires: mc-license = %{version}-%{release}

%description bin
bin components for the mc package.


%package data
Summary: data components for the mc package.
Group: Data

%description data
data components for the mc package.


%package extras
Summary: extras components for the mc package.
Group: Default

%description extras
extras components for the mc package.


%package libexec
Summary: libexec components for the mc package.
Group: Default
Requires: mc-license = %{version}-%{release}

%description libexec
libexec components for the mc package.


%package license
Summary: license components for the mc package.
Group: Default

%description license
license components for the mc package.


%package locales
Summary: locales components for the mc package.
Group: Default

%description locales
locales components for the mc package.


%package man
Summary: man components for the mc package.
Group: Default

%description man
man components for the mc package.


%prep
%setup -q -n mc-4.8.24
cd %{_builddir}/mc-4.8.24
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579627008
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static PYTHON=/usr/bin/python3
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1579627008
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mc
cp %{_builddir}/mc-4.8.24/COPYING %{buildroot}/usr/share/package-licenses/mc/fb6d282f2a4a3dacd3195c711a812f44a2b06e96
cp %{_builddir}/mc-4.8.24/doc/COPYING %{buildroot}/usr/share/package-licenses/mc/fb6d282f2a4a3dacd3195c711a812f44a2b06e96
%make_install
%find_lang mc
## install_append content
mkdir -p %{buildroot}/usr/share
mv %{buildroot}/etc/mc/* %{buildroot}/usr/share/mc/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mc
/usr/bin/mcdiff
/usr/bin/mcedit
/usr/bin/mcview

%files data
%defattr(-,root,root,-)
/usr/share/mc/edit.indent.rc
/usr/share/mc/examples/macros.d/macro.0.sh
/usr/share/mc/examples/macros.d/macro.1.sh
/usr/share/mc/examples/macros.d/macro.3.sh
/usr/share/mc/examples/macros.d/macro.4.sh
/usr/share/mc/examples/macros.d/macro.5.sh
/usr/share/mc/examples/macros.d/macro.6.sh
/usr/share/mc/examples/macros.d/macro.7.sh
/usr/share/mc/filehighlight.ini
/usr/share/mc/help/mc.hlp
/usr/share/mc/help/mc.hlp.es
/usr/share/mc/help/mc.hlp.hu
/usr/share/mc/help/mc.hlp.it
/usr/share/mc/help/mc.hlp.pl
/usr/share/mc/help/mc.hlp.ru
/usr/share/mc/help/mc.hlp.sr
/usr/share/mc/hints/mc.hint
/usr/share/mc/hints/mc.hint.af
/usr/share/mc/hints/mc.hint.ar
/usr/share/mc/hints/mc.hint.az
/usr/share/mc/hints/mc.hint.be
/usr/share/mc/hints/mc.hint.bg
/usr/share/mc/hints/mc.hint.br
/usr/share/mc/hints/mc.hint.ca
/usr/share/mc/hints/mc.hint.cs
/usr/share/mc/hints/mc.hint.da
/usr/share/mc/hints/mc.hint.de
/usr/share/mc/hints/mc.hint.de_CH
/usr/share/mc/hints/mc.hint.el
/usr/share/mc/hints/mc.hint.en_GB
/usr/share/mc/hints/mc.hint.eo
/usr/share/mc/hints/mc.hint.es
/usr/share/mc/hints/mc.hint.et
/usr/share/mc/hints/mc.hint.eu
/usr/share/mc/hints/mc.hint.fa
/usr/share/mc/hints/mc.hint.fi
/usr/share/mc/hints/mc.hint.fr
/usr/share/mc/hints/mc.hint.fr_CA
/usr/share/mc/hints/mc.hint.ga
/usr/share/mc/hints/mc.hint.gl
/usr/share/mc/hints/mc.hint.he
/usr/share/mc/hints/mc.hint.hr
/usr/share/mc/hints/mc.hint.hu
/usr/share/mc/hints/mc.hint.ia
/usr/share/mc/hints/mc.hint.id
/usr/share/mc/hints/mc.hint.ie
/usr/share/mc/hints/mc.hint.it
/usr/share/mc/hints/mc.hint.it_IT
/usr/share/mc/hints/mc.hint.ja
/usr/share/mc/hints/mc.hint.ka
/usr/share/mc/hints/mc.hint.kk
/usr/share/mc/hints/mc.hint.ko
/usr/share/mc/hints/mc.hint.lt
/usr/share/mc/hints/mc.hint.lv
/usr/share/mc/hints/mc.hint.mn
/usr/share/mc/hints/mc.hint.nb
/usr/share/mc/hints/mc.hint.nl
/usr/share/mc/hints/mc.hint.pl
/usr/share/mc/hints/mc.hint.pt
/usr/share/mc/hints/mc.hint.pt_BR
/usr/share/mc/hints/mc.hint.ro
/usr/share/mc/hints/mc.hint.ru
/usr/share/mc/hints/mc.hint.sk
/usr/share/mc/hints/mc.hint.sl
/usr/share/mc/hints/mc.hint.sr
/usr/share/mc/hints/mc.hint.sv
/usr/share/mc/hints/mc.hint.sv_SE
/usr/share/mc/hints/mc.hint.szl
/usr/share/mc/hints/mc.hint.ta
/usr/share/mc/hints/mc.hint.te
/usr/share/mc/hints/mc.hint.tr
/usr/share/mc/hints/mc.hint.uk
/usr/share/mc/hints/mc.hint.uz
/usr/share/mc/hints/mc.hint.vi
/usr/share/mc/hints/mc.hint.wa
/usr/share/mc/hints/mc.hint.zh
/usr/share/mc/hints/mc.hint.zh_CN
/usr/share/mc/hints/mc.hint.zh_TW
/usr/share/mc/mc.charsets
/usr/share/mc/mc.default.keymap
/usr/share/mc/mc.emacs.keymap
/usr/share/mc/mc.ext
/usr/share/mc/mc.keymap
/usr/share/mc/mc.lib
/usr/share/mc/mc.menu
/usr/share/mc/mcedit.menu
/usr/share/mc/sfs.ini
/usr/share/mc/skins/dark.ini
/usr/share/mc/skins/darkfar.ini
/usr/share/mc/skins/default.ini
/usr/share/mc/skins/double-lines.ini
/usr/share/mc/skins/featured-plus.ini
/usr/share/mc/skins/featured.ini
/usr/share/mc/skins/gotar.ini
/usr/share/mc/skins/gray-green-purple256.ini
/usr/share/mc/skins/gray-orange-blue256.ini
/usr/share/mc/skins/julia256.ini
/usr/share/mc/skins/mc46.ini
/usr/share/mc/skins/modarcon16-defbg.ini
/usr/share/mc/skins/modarcon16.ini
/usr/share/mc/skins/modarcon16root-defbg.ini
/usr/share/mc/skins/modarcon16root.ini
/usr/share/mc/skins/modarin256-defbg.ini
/usr/share/mc/skins/modarin256.ini
/usr/share/mc/skins/modarin256root-defbg.ini
/usr/share/mc/skins/modarin256root.ini
/usr/share/mc/skins/nicedark.ini
/usr/share/mc/skins/sand256.ini
/usr/share/mc/skins/seasons-autumn16M.ini
/usr/share/mc/skins/seasons-spring16M.ini
/usr/share/mc/skins/seasons-summer16M.ini
/usr/share/mc/skins/seasons-winter16M.ini
/usr/share/mc/skins/xoria256.ini
/usr/share/mc/skins/yadt256-defbg.ini
/usr/share/mc/skins/yadt256.ini
/usr/share/mc/syntax/PKGBUILD.syntax
/usr/share/mc/syntax/Syntax
/usr/share/mc/syntax/ada95.syntax
/usr/share/mc/syntax/as.syntax
/usr/share/mc/syntax/aspx.syntax
/usr/share/mc/syntax/assembler.syntax
/usr/share/mc/syntax/awk.syntax
/usr/share/mc/syntax/c.syntax
/usr/share/mc/syntax/cabal.syntax
/usr/share/mc/syntax/changelog.syntax
/usr/share/mc/syntax/cmake.syntax
/usr/share/mc/syntax/cs.syntax
/usr/share/mc/syntax/css.syntax
/usr/share/mc/syntax/cuda.syntax
/usr/share/mc/syntax/cxx.syntax
/usr/share/mc/syntax/cython.syntax
/usr/share/mc/syntax/d.syntax
/usr/share/mc/syntax/debian-changelog.syntax
/usr/share/mc/syntax/debian-control.syntax
/usr/share/mc/syntax/debian-description.syntax
/usr/share/mc/syntax/debian-sources-list.syntax
/usr/share/mc/syntax/diff.syntax
/usr/share/mc/syntax/dlink.syntax
/usr/share/mc/syntax/dos.syntax
/usr/share/mc/syntax/ebuild.syntax
/usr/share/mc/syntax/eiffel.syntax
/usr/share/mc/syntax/erlang.syntax
/usr/share/mc/syntax/f90.syntax
/usr/share/mc/syntax/filehighlight.syntax
/usr/share/mc/syntax/fortran.syntax
/usr/share/mc/syntax/glsl.syntax
/usr/share/mc/syntax/go.syntax
/usr/share/mc/syntax/haskell.syntax
/usr/share/mc/syntax/hive.syntax
/usr/share/mc/syntax/html.syntax
/usr/share/mc/syntax/idl.syntax
/usr/share/mc/syntax/ini.syntax
/usr/share/mc/syntax/j.syntax
/usr/share/mc/syntax/jal.syntax
/usr/share/mc/syntax/java.syntax
/usr/share/mc/syntax/js.syntax
/usr/share/mc/syntax/latex.syntax
/usr/share/mc/syntax/lisp.syntax
/usr/share/mc/syntax/lkr.syntax
/usr/share/mc/syntax/lsm.syntax
/usr/share/mc/syntax/lua.syntax
/usr/share/mc/syntax/m4.syntax
/usr/share/mc/syntax/mail.syntax
/usr/share/mc/syntax/makefile.syntax
/usr/share/mc/syntax/markdown.syntax
/usr/share/mc/syntax/meson.syntax
/usr/share/mc/syntax/ml.syntax
/usr/share/mc/syntax/named.syntax
/usr/share/mc/syntax/nemerle.syntax
/usr/share/mc/syntax/nroff.syntax
/usr/share/mc/syntax/octave.syntax
/usr/share/mc/syntax/opencl.syntax
/usr/share/mc/syntax/osl.syntax
/usr/share/mc/syntax/pascal.syntax
/usr/share/mc/syntax/perl.syntax
/usr/share/mc/syntax/php.syntax
/usr/share/mc/syntax/po.syntax
/usr/share/mc/syntax/povray.syntax
/usr/share/mc/syntax/procmail.syntax
/usr/share/mc/syntax/properties.syntax
/usr/share/mc/syntax/protobuf.syntax
/usr/share/mc/syntax/puppet.syntax
/usr/share/mc/syntax/python.syntax
/usr/share/mc/syntax/r.syntax
/usr/share/mc/syntax/ruby.syntax
/usr/share/mc/syntax/rust.syntax
/usr/share/mc/syntax/sh.syntax
/usr/share/mc/syntax/slang.syntax
/usr/share/mc/syntax/smalltalk.syntax
/usr/share/mc/syntax/spec.syntax
/usr/share/mc/syntax/sql.syntax
/usr/share/mc/syntax/strace.syntax
/usr/share/mc/syntax/swig.syntax
/usr/share/mc/syntax/syntax.syntax
/usr/share/mc/syntax/tcl.syntax
/usr/share/mc/syntax/texinfo.syntax
/usr/share/mc/syntax/ts.syntax
/usr/share/mc/syntax/tt.syntax
/usr/share/mc/syntax/unknown.syntax
/usr/share/mc/syntax/verilog.syntax
/usr/share/mc/syntax/vhdl.syntax
/usr/share/mc/syntax/xml.syntax
/usr/share/mc/syntax/yabasic.syntax
/usr/share/mc/syntax/yaml.syntax
/usr/share/mc/syntax/yum-repo.syntax
/usr/share/mc/syntax/yxx.syntax

%files extras
%defattr(-,root,root,-)
/usr/libexec/mc/extfs.d/s3+
/usr/libexec/mc/extfs.d/uc1541

%files libexec
%defattr(-,root,root,-)
/usr/libexec/mc/cons.saver
/usr/libexec/mc/ext.d/archive.sh
/usr/libexec/mc/ext.d/doc.sh
/usr/libexec/mc/ext.d/image.sh
/usr/libexec/mc/ext.d/misc.sh
/usr/libexec/mc/ext.d/package.sh
/usr/libexec/mc/ext.d/sound.sh
/usr/libexec/mc/ext.d/text.sh
/usr/libexec/mc/ext.d/video.sh
/usr/libexec/mc/ext.d/web.sh
/usr/libexec/mc/extfs.d/README
/usr/libexec/mc/extfs.d/README.extfs
/usr/libexec/mc/extfs.d/a+
/usr/libexec/mc/extfs.d/apt+
/usr/libexec/mc/extfs.d/audio
/usr/libexec/mc/extfs.d/bpp
/usr/libexec/mc/extfs.d/changesetfs
/usr/libexec/mc/extfs.d/deb
/usr/libexec/mc/extfs.d/deba
/usr/libexec/mc/extfs.d/debd
/usr/libexec/mc/extfs.d/dpkg+
/usr/libexec/mc/extfs.d/gitfs+
/usr/libexec/mc/extfs.d/hp48+
/usr/libexec/mc/extfs.d/iso9660
/usr/libexec/mc/extfs.d/lslR
/usr/libexec/mc/extfs.d/mailfs
/usr/libexec/mc/extfs.d/patchfs
/usr/libexec/mc/extfs.d/patchsetfs
/usr/libexec/mc/extfs.d/rpm
/usr/libexec/mc/extfs.d/rpms+
/usr/libexec/mc/extfs.d/trpm
/usr/libexec/mc/extfs.d/u7z
/usr/libexec/mc/extfs.d/uace
/usr/libexec/mc/extfs.d/ualz
/usr/libexec/mc/extfs.d/uar
/usr/libexec/mc/extfs.d/uarc
/usr/libexec/mc/extfs.d/uarj
/usr/libexec/mc/extfs.d/ucab
/usr/libexec/mc/extfs.d/uha
/usr/libexec/mc/extfs.d/ulha
/usr/libexec/mc/extfs.d/ulib
/usr/libexec/mc/extfs.d/urar
/usr/libexec/mc/extfs.d/uzip
/usr/libexec/mc/extfs.d/uzoo
/usr/libexec/mc/fish/README.fish
/usr/libexec/mc/fish/append
/usr/libexec/mc/fish/chmod
/usr/libexec/mc/fish/chown
/usr/libexec/mc/fish/fexists
/usr/libexec/mc/fish/get
/usr/libexec/mc/fish/hardlink
/usr/libexec/mc/fish/info
/usr/libexec/mc/fish/ln
/usr/libexec/mc/fish/ls
/usr/libexec/mc/fish/mkdir
/usr/libexec/mc/fish/mv
/usr/libexec/mc/fish/rmdir
/usr/libexec/mc/fish/send
/usr/libexec/mc/fish/unlink
/usr/libexec/mc/fish/utime
/usr/libexec/mc/mc-wrapper.csh
/usr/libexec/mc/mc-wrapper.sh
/usr/libexec/mc/mc.csh
/usr/libexec/mc/mc.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mc/fb6d282f2a4a3dacd3195c711a812f44a2b06e96

%files man
%defattr(0644,root,root,0755)
/usr/share/man/es/man1/mc.1
/usr/share/man/hu/man1/mc.1
/usr/share/man/it/man1/mc.1
/usr/share/man/man1/mc.1
/usr/share/man/man1/mcedit.1
/usr/share/man/man1/mcview.1
/usr/share/man/pl/man1/mc.1
/usr/share/man/ru/man1/mc.1
/usr/share/man/sr/man1/mc.1

%files locales -f mc.lang
%defattr(-,root,root,-)

