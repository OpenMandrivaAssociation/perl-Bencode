%define upstream_name Bencode
%define upstream_version 1.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Summary:	BitTorrent serialization format
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Bencode/
Source0:	http://www.cpan.org/authors/id/A/AR/ARISTOTLE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module implements the BitTorrent bencode serialization format as
described in http://www.bittorrent.org/protocol.html.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/%{upstream_name}.3pm.xz


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.400.0-2mdv2011.0
+ Revision: 657386
- rebuild for updated spec-helper

* Wed Mar 09 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.400.0-1
+ Revision: 643106
- import perl-Bencode

