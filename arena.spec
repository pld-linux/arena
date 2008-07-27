Summary:	Arena Scripting Language with syntax and library similar to ANSI C
Summary(pl.UTF-8):	Język skryptowy Arena ze składnią i biblioteką podobną do ANSI C
Name:		arena
Version:	0.9.9
Release:	2
License:	distributable	
Group:		Development/Languages
Source0:	http://www.minimalinux.org/arena/%{name}-%{version}.tar.gz
# Source0-md5:	16005f68f784d9062feccfaa83c1ad03
URL:		http://www.minimalinux.org/arena/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arena, a light-weight scripting language. The language uses a syntax
and library similar to that of ANSI C, but adds automatic memory
management and runtime polymorphism on top of that.
The Arena language was designed with the following main features
in mind, most of which were added on top of a very C-like core to
support:
- better ad-hoc scripting: 
- syntax similar to ANSI C
- standard library similar to ANSI C
- automatic memory management
- runtime polymorphism
- support for exceptions
- support for anonymous functions

Additionally, an interpreter for the Arena language can be
implemented to be very compact in terms of both source code size
and memory consumption.

%description -l pl.UTF-8
Arena to lekki język skryptowy. Język wykorzystuje składnię i
bibliotekę podobne do ANSI C, ale dodaje do tego automatyczne
zarządzanie pamięcią i polimorfizm. Język Arena został zaprojektowany
z myślą o następujących cechach, z których większość została dodana
do rdzenia bardzo podobnego do C:
- lepsze tworzenie skryptów ad-hoc
- składnia podobna do ANSI C
- biblioteka standardowa podobna do ANSI C
- automatyczne zarządzanie pamięcią
- polimorfizm
- obsługa wyjątków
- obsługa anonimowych funkcji

Ponadto interpreter języka Arena może być zaimplementowany jako bardzo
zwarty w sensie zarówno rozmiaru kodu źródłowego, jak i wykorzystania
pamięci.

%package examples
Summary:	Examples for Arena Scripting Language
Summary(pl.UTF-8):	Przykłady dla języka skryptowego Arena
Group:		Development/Languages

%description examples
Examples for Arena Scripting Language.

%description examples -l pl.UTF-8
Przykłady dla języka skryptowego Arena.

%prep
%setup -q

%build
%{__autoconf}
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -f doc/manual/transform $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -Rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/CHANGES doc/CREDITS doc/HACKING doc/LICENSE doc/NEWS doc/TODO doc/manual/manual.asc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/arena.1*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
