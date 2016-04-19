#
# Conditional build:
%bcond_with	tests		# build without tests

Summary:	Travis CI client
Name:		travis
Version:	1.8.2
Release:	1
License:	MIT
Group:		Development/Building
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	f488280a4a10f0d036daaed64dfc3bd9
URL:		https://github.com/travis-ci/travis.rb
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-rack-test < 1
BuildRequires:	ruby-rack-test >= 0.6
BuildRequires:	ruby-rspec < 3
BuildRequires:	ruby-rspec >= 2.12
BuildRequires:	ruby-sinatra < 2
BuildRequires:	ruby-sinatra >= 1.3
%endif
Requires:	ruby-%{name} = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLI client for Travis CI.

%package -n ruby-%{name}
Summary:	Ruby client library for Travis CI
Group:		Development/Languages
Requires:	ruby-backports
Requires:	ruby-faraday < 1
Requires:	ruby-faraday >= 0.9
Requires:	ruby-faraday_middleware < 1
Requires:	ruby-faraday_middleware >= 0.9.1
Requires:	ruby-gh < 1
Requires:	ruby-gh >= 0.13
Requires:	ruby-highline < 2
Requires:	ruby-highline >= 1.6
Requires:	ruby-launchy < 3
Requires:	ruby-launchy >= 2.1
Requires:	ruby-modules >= 1:1.9
Requires:	ruby-pusher-client < 1
Requires:	ruby-pusher-client >= 0.4
#Requires:	ruby-typhoeus < 1
#Requires:	ruby-typhoeus >= 0.6.8

%description -n ruby-%{name}
Ruby client library for Travis CI.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/travis

%files -n ruby-%{name}
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/travis.rb
%{ruby_vendorlibdir}/travis
%{ruby_specdir}/%{name}-%{version}.gemspec
