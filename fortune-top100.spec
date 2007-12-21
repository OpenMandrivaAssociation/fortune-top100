%define base_name	top100
%define name		fortune-%{base_name}
%define version		1.0
%define release		%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Top 100 things you don't want the sysadmin to say
License:	Public Domain
Group:		Toys
Source:		%{base_name}.tar.bz2
Url:		http://people.redhat.com/andrew/humor/100sys.html
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

