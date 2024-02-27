%define		module	sentry_sdk
%define		mname	sentry-sdk
Summary:	Python sentry-sdk
Summary(pl.UTF-8):	sentry-sdk
Name:		python3-%{mname}
Version:	1.40.6
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download:	https://pypi.org/simple/sentry-sdk/
Source0:	https://files.pythonhosted.org/packages/source/s/sentry-sdk/%{mname}-%{version}.tar.gz
# Source0-md5:	eb66d1810fe87ab742cf33afdfe9df82
URL:		https://pypi.org/project/sentry-sdk/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sentry is on a mission to help developers write better software
faster, so we can get back to enjoying technology.

%prep
%setup -q -n %{mname}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/*/*.py
%{py3_sitescriptdir}/%{module}/*/*/*.py
%{py3_sitescriptdir}/%{module}/*/*/*/*.py
%{py3_sitescriptdir}/%{module}/py.typed
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}/*/__pycache__
%{py3_sitescriptdir}/%{module}/*/*/__pycache__
%{py3_sitescriptdir}/%{module}/*/*/*/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
