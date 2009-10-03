Summary:	A heuristic autodialer for PPP connections
Name:		wvdial
Version:	1.60
Release:	%{mkrel 2}
Epoch:		1
License:	LGPLv2+
Group:		System/Configuration/Networking
Source0:	http://open.nit.ca/download/%{name}-%{version}.tar.gz
Url:		http://open.nit.ca/wvdial
Patch0: 	wvdial-1.56-bad_analyse.patch
Patch1:		wvdial-1.56-remotename.patch
Patch2:		wvdial-1.60-dirent.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	ppp >= 2.3.7
Buildrequires: 	wvstreams-devel >= 4.2

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
%patch2 -p1 -b .dirent

%build
%make "VERBOSE=1"

%install
rm -rf %{buildroot}
make install \
        PREFIX=%{buildroot}%{_prefix} \
        BINDIR=%{buildroot}%{_bindir} \
        MANDIR=%{buildroot}%{_mandir} \
        PPPDIR=%{buildroot}%{_sysconfdir}/ppp/peers
install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d

%clean
 rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING.LIB FAQ MENUS README TODO
%attr(4755,root,root)	%{_bindir}/%{name}
%attr(0755,root,root)	%{_bindir}/%{name}conf
%attr(0644,root,root)	%{_mandir}/man1/*
%attr(0644,root,root)	%{_mandir}/man5/*
%attr(0644,root,daemon)	%config(noreplace) %{_sysconfdir}/ppp/peers/%{name}
%attr(0644,root,daemon)	%config(noreplace) %{_sysconfdir}/ppp/peers/%{name}-pipe

