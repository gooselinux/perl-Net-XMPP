Name:           perl-Net-XMPP
Version:        1.02
Release:        8%{?dist}
Summary:        Net::XMPP - perl XMPP library

Group:          Development/Libraries
License:        (GPL+ or Artistic) or LGPLv2+
URL:            http://search.cpan.org/dist/Net-XMPP/
Source0:        http://search.cpan.org/CPAN/modules/by-module/Net/Net-XMPP-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch 
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::Stream), perl(Digest::SHA1)
        
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Net::XMPP provides a Perl user with access to the Extensible
Messaging and Presence Protocol (XMPP).

For more information about XMPP visit:

     http://www.xmpp.org

%prep
%setup -q -n Net-XMPP-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf %{buildroot}

./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
# this test seems to have issues with being unable to resolve the builder's
# hostname inside mock.
%{?!_with_network_tests: rm t/roster.t }
./Build test


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README CHANGES examples/ LICENSE.* 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.02-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.02-5
- fix license tag (technically, it was correct before, but this change prevents
  rpmlint from flagging it as bad in a false positive)

* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.02-4
- rebuild for new perl

* Wed Jan 02 2008 Ralf Corsépius <rc040203@freenet.de> 1.02-3
- BR: perl(Test::More) (BZ 419631).
- Spec file cleanup.

* Mon Apr 02 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.02-2
- nix troublesome test that fails due to resolver configuration under
  builder's mock

* Sun Apr 01 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.02-1
- update to 1.02
- note license change:  perl to LGPL
- switched over to Build.PL; misc spec file cleanups

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.0-6
- bump for mass rebuild

* Sun May 28 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.0-5
- disable test suite, per review.

* Thu May 25 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.0-4
- include license text, including generated ones
- include correspondance with the module's author

* Wed May 24 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.0-3
- update license to triple licensed, based on conversations with upstream

* Mon May 15 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.0-2
- include additional files as docs

* Fri May 12 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.0-1
- first f-e spec.
  
