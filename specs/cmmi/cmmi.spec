# Upstream: Kiyoka Nishiyama <kiyoka$netfort,gr,jp>

Summary: The program which makes convenient installation work of the software using configure script
Name: cmmi
Version: 0.5.2
Release: 1%{?dist}
Group: Development/Tools
Source0: http://prdownloads.sourceforge.net/cmmi/cmmi-%{version}.tar.gz
Patch0: cmmi-0.5.2_conf.patch
URL: http://www.netfort.gr.jp/~kiyoka/cmmi/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: perl >= 5
BuildRequires: perl
BuildArch: noarch
License: GPLv2

%description
Cmmi helps you to simplify your installation process from '.tar.gz' source
archives.You can be a package manager of your local site, if you are not an
expert of your OS.Cmmi can make Debian, RedHat, Slackware and cygwin packages
efficiently.

%prep
%setup -q
%patch0 -p1

%build

%install
%{__rm} -rf %{buildroot}

%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -m0755 cmmi %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING CREDITS README README.ja dot.cmmirc*
%{_bindir}/cmmi

%changelog
* Sun Jan 19 2014 IWAI, Masaharu <iwaim.sub@gmail.com> 0.5.2-1
- initial release

