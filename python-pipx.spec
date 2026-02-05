%define module pipx

Name:		python-pipx
Version:	1.8.0
Release:	1
Summary:	Install and Run Python Applications in Isolated Environments
URL:		https://pypi.org/project/pipx/
# The pypi sources do not provide scipts used in man generation are not provided as part of
# the pypi source tarball
Source0:	https://github.com/pypa/pipx/archive/%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	python%{pyver}dist(build)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(installer)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
# BRs for generating completions and man pages
BuildRequires:	python%{pyver}dist(argcomplete)
BuildRequires:	python%{pyver}dist(argparse-manpage)
BuildRequires:	python%{pyver}dist(userpath) >= 1.6
Requires:	python%{pyver}dist(userpath) >= 1.6

%description
Install and Run Python Applications in Isolated Environments.

%build -p
# required for git tarball as it cannot discern its own version, provide it
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%build -a
# Generate man pages for binaries
PYTHONPATH="${PWD}/src" %{__python3} scripts/generate_man.py
# As per the output of running 'pipx completions' in order to generate shell
# completions as described in its documentation:
# https://pipx.pypa.io/stable/installation/#shell-completion
for sh in bash tcsh fish zsh
do
	# this works without having to import the module
	register-python-argcomplete --shell "${sh}" pipx > "pipx.${sh}"
done

%install -a
# install man page
install -p -m 0644 -D -t %{buildroot}%{_mandir}/man1 pipx.1
# install shell completions
install -Dpm 0644 pipx.bash %{buildroot}%{_datadir}/bash-completion/completions/pipx
install -Dpm 0644 pipx.fish %{buildroot}%{_datadir}/fish/completions/pipx.fish
install -Dpm 0644 pipx.zsh %{buildroot}%{_datadir}/zsh/site-functions/_pipx
# no system path to install the tcsh completions, leave this in pipx's datadir
# for any users of that shell to have them available.
install -Dpm 0644 pipx.tcsh %{buildroot}%{_datadir}/pipx/pipx-completion.tcsh

%files
%{_bindir}/%{module}
%{_datadir}/bash-completion/completions/%{module}
%{_datadir}/fish/completions/%{module}.fish
%{_datadir}/zsh/site-functions/_%{module}
%{_datadir}/%{module}/%{module}-completion.tcsh
%{_mandir}/man1/%{module}.1.zst
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
