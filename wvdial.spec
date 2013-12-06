Summary:	A heuristic autodialer for PPP connections
Name:		wvdial
Version:	1.61
Release:	7
Epoch:		1
License:	LGPLv2+
Group:		System/Configuration/Networking
Source0:	http://wvstreams.googlecode.com/files/%{name}-%{version}.tar.gz
Url:		http://alumnit.ca/wiki/index.php?page=WvDial
Patch0: 	wvdial-1.56-bad_analyse.patch
Patch1:		wvdial-1.56-remotename.patch
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

%build
./configure
make "VERBOSE=1"

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



%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.61-2mdv2011.0
+ Revision: 670819
- mass rebuild

* Tue Nov 23 2010 Eugeni Dodonov <eugeni@mandriva.com> 1:1.61-1mdv2011.0
+ Revision: 600275
- Updated to 1.61.
  Drop merged patch.

* Mon Oct 05 2009 Funda Wang <fwang@mandriva.org> 1:1.60-3mdv2010.0
+ Revision: 454001
- rebuild for new wvstreams

* Sat Oct 03 2009 Funda Wang <fwang@mandriva.org> 1:1.60-2mdv2010.0
+ Revision: 453188
- fix build

* Sat Dec 20 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.60-2mdv2009.1
+ Revision: 316619
- rebuild with new wvstreams
- spec clean
- new license policy

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 15 2007 Emmanuel Andry <eandry@mandriva.org> 1:1.60-1mdv2008.1
+ Revision: 120420
- Naw version

* Tue Jul 03 2007 Adam Williamson <awilliamson@mandriva.org> 1:1.5.90-2mdv2008.0
+ Revision: 47665
- fix buildrequires
- new release 1.5.90 (upstream test)

* Sat Apr 28 2007 Olivier Blin <oblin@mandriva.com> 1.56-2mdv2008.0
+ Revision: 18993
- restore remotename patch by rewritting it for new wvargs parsing (wrongly removed in 1.56 upgrade)

* Fri Apr 27 2007 Adam Williamson <awilliamson@mandriva.org> 1.56-1mdv2008.0
+ Revision: 18772
- 1.56, drop remotename patch (appears to have been superseded upstream)


* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 1.54.0-4mdk
- rebuild

* Fri Jul 09 2004 Olivier Blin <blino@mandrake.org> 1.54.0-3mdk
- rebuild for libstdc++6

* Sat Jan 03 2004 Olivier Blin <blino@mandrake.org> 1.54.0-2mdk
- remove bash-completion source, it was merged in bash-completion

* Tue Dec 23 2003 Olivier Blin <blino@mandrake.org> 1.54.0-1mdk
- fix perms on peer options files
- bash completion support :-) (Source1)
- use VERBOSE=1 in make not to lie about options
- rediff -remotename patch
- use %%make
- don't check if $RPM_BUILD_ROOT is / before removing it ...
- fix unitialized and unneeded buffer in analyse_line() (Patch0)
- new release

* Mon Aug 04 2003 Aurelien Lemaire <alemaire@mandrakesoft.com> 1.53-3mdk
- Fix undefined references on crypt lib
- Fix buildrequires with vitual providing name

* Mon Jul 21 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.53-2mdk
- rebuild

* Thu Dec 19 2002 Aurelien Lemaire <alemaire@mandrakesoft.com> 1.53-1mdk
- New version : 1.53
- Update Source
- Add Url
- Add build-requires
- Change Copyright to License
- Document --remotename in the man page
- Remove C++ fix patch

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.42-4mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.42-3mdk
- Automated rebuild with gcc3.2

* Sat Jul 13 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.42-2mdk
- Don't unset alpha opt flags.
- C++ fix.

* Fri Jun 22 2001 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.42-1mdk
- initial mandrake release

* Mon Apr 02 2001 Nalin Dahyabhai <nalin@redhat.com>
- include the actual TODO file in docs, not a dangling symlink to it (#34385)

* Mon Feb 12 2001 Nalin Dahyabhai <nalin@redhat.com>
- Merge in latest -libs patch from rp3.

* Mon Aug 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- Merge in latest -libs patch from rp3.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul 02 2000 Jakub Jelinek <jakub@redhat.com>
- Rebuild with new C++

* Sat Jun 17 2000 Bill Nottingham <notting@redhat.com>
- add %%defattr

* Fri Jun 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- Merge in latest -libs patch from rp3.

* Sun Jun 04 2000 Nalin Dahyabhai <nalin@redhat.com>
- FHS fixes.

* Fri May 05 2000 Bill Nottingham <notting@redhat.com>
- fix build with more strict c++ compiler

* Tue Mar 07 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Fri Jan 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- sync up to copy in rp3's CVS repository for consistency, except for
  changes to Makefiles

* Thu Jan 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.41, backing out patches that are now in mainline source

* Sat Sep 18 1999 Michael K. Johnson <johnsonm@redhat.com>
- improved the speed up dialing patch
- improved the inheritance patch

* Fri Sep 17 1999 Michael K. Johnson <johnsonm@redhat.com>
- added explicit inheritance to wvdial.conf
- speed up dialing

* Mon Sep 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- improved the chat mode fix to allow specifying the remotename
  so that multiple wvdial instances can't step on each other.

* Fri Sep 10 1999 Michael K. Johnson <johnsonm@redhat.com>
- chat mode fix to make CHAP/PAP work with chat mode

* Mon Aug 02 1999 Michael K. Johnson <johnsonm@redhat.com>
- Packaged 1.40

* Wed Jul 28 1999 Michael K. Johnson <johnsonm@redhat.com>
- Initial Red Hat package

