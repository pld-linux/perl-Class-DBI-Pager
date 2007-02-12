#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	DBI-Pager
Summary:	Class::DBI::Pager - pager utility for Class::DBI
Summary(pl.UTF-8):   Class::DBI::Pager - narzędzie stronicujące dla Class::DBI
Name:		perl-Class-DBI-Pager
Version:	0.08
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d6b462ecc6439728a209ec5ec0192b0c
Patch0:		%{name}-versionedep.patch
URL:		http://search.cpan.org/dist/Class-DBI-Pager/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor-Chained
BuildRequires:	perl-Class-DBI >= 0.90
BuildRequires:	perl-Data-Page >= 0.13
BuildRequires:	perl-Exporter-Lite
%endif
# Not caught by autodeps
Requires:	perl-Class-Accessor-Chained
# Need versioned dep
Requires:	perl-Class-DBI >= 0.90
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::DBI::Pager is a plugin for Class::DBI, which glues Data::Page
with Class::DBI. This module reduces your work a lot, for example when
you have to do something like:
 - retrieve objects from a database
 - display objects with 20 items per page In addition, your work will
   be reduced more, when you use Template-Toolkit as your templating
   engine.

%description -l pl.UTF-8
Class::DBI::Pager to wtyczka dla Class::DBI, która skleja Data::Page z
Class::DBI. Ten moduł oszczędza wiele pracy, na przykład kiedy robimy
coś w rodzaju:
 - odczytanie obiektów z bazy danych
 - wyświetlenie obiektów po 20 elementów na stronie. Ponadto jeszcze
   więcej pracy można oszczędzić przy użyciu Template-Toolkitu jako
   silnika szablonów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
