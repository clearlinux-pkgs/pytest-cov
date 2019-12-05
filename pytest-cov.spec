#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-cov
Version  : 2.8.1
Release  : 48
URL      : https://files.pythonhosted.org/packages/13/8a/51f54b43a043c799bceca846594b9a310823a3e52df5ec27109cccba90f4/pytest-cov-2.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/13/8a/51f54b43a043c799bceca846594b9a310823a3e52df5ec27109cccba90f4/pytest-cov-2.8.1.tar.gz
Summary  : Pytest plugin for measuring coverage.
Group    : Development/Tools
License  : MIT
Requires: pytest-cov-license = %{version}-%{release}
Requires: pytest-cov-python = %{version}-%{release}
Requires: pytest-cov-python3 = %{version}-%{release}
Requires: coverage
Requires: pytest
BuildRequires : Sphinx
BuildRequires : Sphinx-python
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : coverage-python
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
========
Overview
========
.. start-badges
.. list-table::
:stub-columns: 1
* - docs
- |docs|
* - tests
- | |travis| |appveyor| |requires|
* - package
- | |version| |conda-forge| |wheel| |supported-versions| |supported-implementations|
| |commits-since|

%package license
Summary: license components for the pytest-cov package.
Group: Default

%description license
license components for the pytest-cov package.


%package python
Summary: python components for the pytest-cov package.
Group: Default
Requires: pytest-cov-python3 = %{version}-%{release}

%description python
python components for the pytest-cov package.


%package python3
Summary: python3 components for the pytest-cov package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytest-cov package.


%prep
%setup -q -n pytest-cov-2.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570381449
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-cov
cp LICENSE %{buildroot}/usr/share/package-licenses/pytest-cov/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-cov/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
