Summary: autoconf-252 - Generate configuration scripts
%define AppProgram autoconf
%define AppVersion 2.52
%define AppRelease 20100930
%define AppSuffix  -252
# $Id: ac252.spec,v 1.5 2010/09/30 23:57:29 tom Exp $
Name: ac252
Version: %{AppVersion}
Release: %{AppRelease}
License: GPLv2
Group: Applications/Development
URL: ftp://invisible-island.net/%{AppProgram}
Source0: %{AppProgram}-%{AppVersion}-%{AppRelease}.tgz
Packager: Thomas E. Dickey <dickey@invisible-island.net>

%description
This is a stable version of autoconf, used by all of my applications.

%prep

%setup -q -n %{AppProgram}-%{AppVersion}-%{AppRelease}

%build

INSTALL_PROGRAM='${INSTALL}' \
	./configure \
		--program-suffix=%{AppSuffix} \
		--target %{_target_platform} \
		--prefix=%{_prefix} \
		--bindir=%{_bindir} \
		--mandir=%{_mandir} \
		--datadir=%{_datadir}/%{AppProgram}%{AppSuffix} \
		--infodir=%{_infodir}

make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make install                    DESTDIR=$RPM_BUILD_ROOT

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*%{AppSuffix}
%{_mandir}/man1/*%{AppSuffix}*
%{_datadir}/%{AppProgram}%{AppSuffix}*
#%{_infodir}/*%{AppSuffix}*
%{_infodir}/*

%changelog
# each patch should add its ChangeLog entries here

* Tue Sep 28 2010 Thomas E. Dickey
- initial version
