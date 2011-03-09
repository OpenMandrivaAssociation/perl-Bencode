%define upstream_name Bencode
%define upstream_version 1.4

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1
Summary:        BitTorrent serialization format
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Bencode/
Source0:        http://www.cpan.org/authors/id/A/AR/ARISTOTLE/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)


%description
This module implements the BitTorrent bencode serialization format as
described in http://www.bittorrent.org/protocol.html.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/%{upstream_name}.3pm.xz
