%define name      wvdial
%define version   1.54.0
%define release   %mkrel 4

Summary:	A heuristic autodialer for PPP connections
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Configuration/Networking
Source0:	http://open.nit.ca/download/%{name}-%{version}.tar.bz2
Url:		http://open.nit.ca/wvdial
Patch0: 	%{name}-%{version}-bad_analyse.patch
Patch1: 	%{name}-%{version}-remotename.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	ppp >= 2.3.7
Buildrequires: 	libwvstreams-devel >= 3.74.0

%description
WvDial automatically locates and configures modems and can log into
almost any ISP's server without special configuration. You need to
input the username, password, and phone number, and then WvDial will
negotiate the PPP connection using any mechanism needed.
Install wvdial if you need a utility to configure your modem and set
up a PPP connection.

%prep
%setup -q
%patch0 -p1 -b .bad_analyse
%patch1 -p1 -b .remotename

%build
%make "VERBOSE=1"

%install
rm -rf $RPM_BUILD_ROOT
make install \
        PREFIX=${RPM_BUILD_ROOT}%{_prefix} \
        BINDIR=${RPM_BUILD_ROOT}%{_bindir} \
        MANDIR=${RPM_BUILD_ROOT}%{_mandir} \
        PPPDIR=${RPM_BUILD_ROOT}%{_sysconfdir}/ppp/peers
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%clean
 rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES COPYING.LIB FAQ MENUS README TODO
%attr(4755,root,root)	%{_bindir}/%{name}
%attr(0755,root,root)	%{_bindir}/%{name}conf
%attr(0644,root,root)	%{_mandir}/man1/*
%attr(0644,root,root)	%{_mandir}/man5/*
%attr(0644,root,daemon)	%config(noreplace) %{_sysconfdir}/ppp/peers/%{name}
%attr(0644,root,daemon)	%config(noreplace) %{_sysconfdir}/ppp/peers/%{name}-pipe

