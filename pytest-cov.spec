#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-cov
Version  : 2.1.0
Release  : 12
URL      : https://pypi.python.org/packages/source/p/pytest-cov/pytest-cov-2.1.0.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pytest-cov/pytest-cov-2.1.0.tar.gz
Summary  : Pytest plugin for measuring coverage.
Group    : Development/Tools
License  : MIT
Requires: pytest-cov-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================
pytest-cov
===============================
.. list-table::
:stub-columns: 1

%package python
Summary: python components for the pytest-cov package.
Group: Default

%description python
python components for the pytest-cov package.


%prep
%setup -q -n pytest-cov-2.1.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
