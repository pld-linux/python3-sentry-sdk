#
# Conditional build:
%bcond_with	tests	# unit tests [missing conftest.py in sdist]

Summary:	Python client for Sentry
Summary(pl.UTF-8):	Pythonowy klient usługi Sentry
Name:		python3-sentry-sdk
Version:	1.40.6
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download:	https://pypi.org/simple/sentry-sdk/
Source0:	https://files.pythonhosted.org/packages/source/s/sentry-sdk/sentry-sdk-%{version}.tar.gz
# Source0-md5:	eb66d1810fe87ab742cf33afdfe9df82
URL:		https://pypi.org/project/sentry-sdk/
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-certifi
BuildRequires:	python3-executing
BuildRequires:	python3-gevent
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-forked
BuildRequires:	python3-urllib3 >= 1.26.11
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sentry is on a mission to help developers write better software
faster, so we can get back to enjoying technology.

This package is the official Python SDK for Sentry
<http://sentry.io/>.

%description -l pl.UTF-8
Misją Sentry jest pomagać programistom pisać szybciej lepsze
oprogramowanie, dzięki czemu można z powrotem cieszyć się
technologią.

Ten pakiet jest oficjalnym pythonowym SDK dla usługi Sentry
<http://sentry.io/>.

%prep
%setup -q -n sentry-sdk-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_forked \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sentry_sdk
%{py3_sitescriptdir}/sentry_sdk-%{version}-py*.egg-info
