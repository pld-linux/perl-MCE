#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MCE
Summary:	MCE - Many-Core Engine for Perl providing parallel processing capabilities
Summary(pl.UTF-8):	MCE - silnik Many-Core Engine dla Perla zapewniający możliwość przetwarzania równoległego
Name:		perl-MCE
Version:	1.808
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MA/MARIOROY/MCE-%{version}.tar.gz
# Source0-md5:	5e76a7afde92d3f0c7161711fe4be303
URL:		http://search.cpan.org/dist/MCE/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Storable >= 2.04
BuildRequires:	perl-Test-Simple >= 0.88
%endif
Requires:	perl-Storable >= 2.04
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Many-Core Engine (MCE) for Perl helps enable a new level of
performance by maximizing all available cores.

%description -l pl.UTF-8
Many-Core Engine (MCE), czyli silnik wielordzeniowy dla Perla
pomaga osiągnąć nowy poziom wydajności maksymalizując wykorzystanie
wszystkich dostępnych rdzeni.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/MCE.pod \
	$RPM_BUILD_ROOT%{perl_vendorlib}/MCE/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Credits README.md
%{perl_vendorlib}/MCE.pm
%{perl_vendorlib}/MCE
%{_mandir}/man3/MCE.3pm*
%{_mandir}/man3/MCE::*.3pm*
