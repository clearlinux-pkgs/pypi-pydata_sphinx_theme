#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pydata_sphinx_theme
Version  : 0.7.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/4b/c4/ad259fbabb4c8e8fc5247290db815d6d905bcfd057c18b06ecb926721a09/pydata-sphinx-theme-0.7.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4b/c4/ad259fbabb4c8e8fc5247290db815d6d905bcfd057c18b06ecb926721a09/pydata-sphinx-theme-0.7.2.tar.gz
Summary  : Bootstrap-based Sphinx theme from the PyData community
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pydata_sphinx_theme-license = %{version}-%{release}
Requires: pypi-pydata_sphinx_theme-python = %{version}-%{release}
Requires: pypi-pydata_sphinx_theme-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(beautifulsoup4)
BuildRequires : pypi(docutils)
BuildRequires : pypi(sphinx)

%description
# pydata-sphinx-theme
![pypi](https://img.shields.io/pypi/v/pydata-sphinx-theme) [![conda-forge](https://img.shields.io/conda/vn/conda-forge/pydata-sphinx-theme.svg)](https://anaconda.org/conda-forge/pydata-sphinx-theme) [![continuous-integration](https://github.com/pydata/pydata-sphinx-theme/actions/workflows/tests.yml/badge.svg)](https://github.com/pydata/pydata-sphinx-theme/actions/workflows/tests.yml) [![docs](https://readthedocs.org/projects/pydata-sphinx-theme/badge/)](https://readthedocs.org/projects/pydata-sphinx-theme/builds/) [![codecov](https://codecov.io/gh/pydata/pydata-sphinx-theme/branch/master/graph/badge.svg?token=NwOObjYacn)](https://codecov.io/gh/pydata/pydata-sphinx-theme)

%package license
Summary: license components for the pypi-pydata_sphinx_theme package.
Group: Default

%description license
license components for the pypi-pydata_sphinx_theme package.


%package python
Summary: python components for the pypi-pydata_sphinx_theme package.
Group: Default
Requires: pypi-pydata_sphinx_theme-python3 = %{version}-%{release}

%description python
python components for the pypi-pydata_sphinx_theme package.


%package python3
Summary: python3 components for the pypi-pydata_sphinx_theme package.
Group: Default
Requires: python3-core
Provides: pypi(pydata_sphinx_theme)
Requires: pypi(beautifulsoup4)
Requires: pypi(docutils)
Requires: pypi(packaging)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-pydata_sphinx_theme package.


%prep
%setup -q -n pydata-sphinx-theme-0.7.2
cd %{_builddir}/pydata-sphinx-theme-0.7.2
pushd ..
cp -a pydata-sphinx-theme-0.7.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656397454
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pydata_sphinx_theme
cp %{_builddir}/pydata-sphinx-theme-0.7.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pydata_sphinx_theme/7e48d15dafb129b7437e96100ed0d5e7f04b4082
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pydata_sphinx_theme/7e48d15dafb129b7437e96100ed0d5e7f04b4082

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
