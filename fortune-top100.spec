%define base_name	top100
%define name		fortune-%{base_name}
%define version		1.0
%define release		11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Top 100 things you don't want the sysadmin to say
License:	Public Domain
Group:		Toys
Source:		%{base_name}.tar.bz2
Url:		https://people.redhat.com/andrew/humor/100sys.html
Requires:	fortune-mod
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
The top 100 things you don't want the sysadmin to say in fortune format.

%prep
%setup -q -n %{base_name}

%build

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/fortunes
install -m 644 %{base_name}* %{buildroot}%{_gamesdatadir}/fortunes

%files
%defattr(-,root,root)
%{_gamesdatadir}/fortunes/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2011.0
+ Revision: 618336
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0-9mdv2010.0
+ Revision: 428881
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2009.0
+ Revision: 245329
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0-6mdv2008.1
+ Revision: 125201
- kill re-definition of %%buildroot on Pixel's request
- import fortune-top100


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-6mdv2007.0
- %%mkrel
- clean buildroot before install

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-5mdk 
- spec cleanup

* Wed Jul 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0-4mdk 
- rebuild

* Sat Feb 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0-3mdk
- rebuild

* Sat Jan 04 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0-2mdk
- rebuild

* Mon Nov 19 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0-1mdk
- first Mandrake release
