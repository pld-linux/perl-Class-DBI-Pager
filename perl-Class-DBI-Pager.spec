#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI-Pager
Summary:	Class::DBI::Pager - Pager utility for Class::DBI
Name:		perl-Class-DBI-Pager
Version:	0.05
Release:	1
# Same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab4eb2c465318f992308dd2445ae55a9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-DBI >= 0.90
BuildRequires:	perl-Data-Page >= 0.13
BuildRequires:	perl-Exporter-Lite
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::DBI::Pager is a plugin for Class::DBI, which glues Data::Page
with Class::DBI. This module reduces your work a lot, for example when
you have to do something like:
 * retrieve objects from a database
 * display objects with 20 items per page
In addition, your work will be reduced more, when you use
Template-Toolkit as your templating engine.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/DBI/Pager.pm
%{_mandir}/man3/*
