#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Empty module placeholder for other LIGO modules
Summary(pl.UTF-8):	Miejsce na inne moduły LIGO
Name:		python-ligo-common
Version:	1.0.3
Release:	1
License:	GPL v3+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ligo-common/
Source0:	https://files.pythonhosted.org/packages/source/l/ligo-common/ligo-common-%{version}.tar.gz
# Source0-md5:	442b49f8af8d45d68ee0fd0a2c2c693e
URL:		https://pypi.org/project/ligo-common/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Empty module placeholder for other LIGO modules.

%description -l pl.UTF-8
Miejsce na inne moduły LIGO.

%package -n python3-ligo-common
Summary:	Empty module placeholder for other LIGO modules
Summary(pl.UTF-8):	Miejsce na inne moduły LIGO
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-ligo-common
Empty module placeholder for other LIGO modules.

%description -n python3-ligo-common -l pl.UTF-8
Miejsce na inne moduły LIGO.

%prep
%setup -q -n ligo-common-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/ligo
%{py_sitescriptdir}/ligo/__init__.py[co]
%{py_sitescriptdir}/ligo_common-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ligo-common
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/ligo
%{py3_sitescriptdir}/ligo/__init__.py
%{py3_sitescriptdir}/ligo/__pycache__/__init__.cpython-*.py[co]
%{py3_sitescriptdir}/ligo_common-%{version}-py*.egg-info
%endif
