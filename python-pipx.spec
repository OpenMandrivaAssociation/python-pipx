Name:		python-pipx
Version:	1.7.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/pipx/pipx-%{version}.tar.gz
Summary:	Install and Run Python Applications in Isolated Environments
URL:		https://pypi.org/project/pipx/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python%{pyver}dist(hatchling)
BuildRequires:  python%{pyver}dist(installer)
BuildRequires:  python%{pyver}dist(build)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(hatch-vcs)
BuildSystem:	python
BuildArch:	noarch

%description
Install and Run Python Applications in Isolated Environments

%files
%{_bindir}/pipx
%{py_sitedir}/pipx
%{py_sitedir}/pipx-*.*-info
